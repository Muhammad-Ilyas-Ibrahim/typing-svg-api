from flask import Flask, request, Response
import xml.etree.ElementTree as ET
import urllib.parse

app = Flask(__name__)

def create_typing_svg(texts, font, color, size, width, height, theme, delay, speed):
    # Default values
    font = font or "Fira Code"
    color = color or "#bfcfde"
    size = int(size) if size and size.isdigit() else 22
    width = int(width) if width and width.isdigit() else 440
    height = int(height) if height and height.isdigit() else 45
    theme = theme or "light"
    # Convert delay to seconds (from milliseconds)
    delay = float(delay) / 1000 if delay and delay.replace(".", "").isdigit() else 0.5
    # Animation speed (characters per second)
    speed = float(speed) if speed and speed.replace(".", "").isdigit() else 10
    bg_color = "#ffffff" if theme == "light" else "#1a1a1a"

    # Split texts if provided as semicolon-separated
    text_list = texts.split(";") if texts else ["Welcome to my profile"]

    # Create SVG root
    svg = ET.Element("svg", width=str(width), height=str(height), xmlns="http://www.w3.org/2000/svg")
    svg.set("style", f"background-color: {bg_color};")

    # Add defs for animations
    defs = ET.SubElement(svg, "defs")
    
    # Calculate animation timing per character based on speed
    char_duration = 1 / speed
    
    # Calculate durations for each text and total cycle time
    text_durations = []
    for text in text_list:
        text = urllib.parse.unquote(text.strip())
        # Duration based on speed
        duration = len(text) * char_duration
        text_durations.append(duration)
    
    # Calculate each animation segment start and end times
    animation_segments = []
    current_time = 0
    
    for i, duration in enumerate(text_durations):
        display_time = duration + 1  # Show text for duration + 1s
        
        start_time = current_time
        end_time = start_time + display_time
        
        animation_segments.append((start_time, end_time))
        current_time = end_time + delay  # Add delay between segments
    
    total_cycle_time = animation_segments[-1][1] + delay

    # Create clip paths for typing animations
    for i, text in enumerate(text_list):
        text = urllib.parse.unquote(text.strip())
        clip_path = ET.SubElement(defs, "clipPath", id=f"clip{i}")
        clip_rect = ET.SubElement(clip_path, "rect", x="0", y="0", width="0", height=str(height))
        
        # Get animation timing
        start_time, end_time = animation_segments[i]
        
        # Add typing animation to clip rectangle
        animate = ET.SubElement(clip_rect, "animate", attributeName="width")
        animate.set("from", "0")
        animate.set("to", str(width))
        duration = text_durations[i]
        animate.set("dur", f"{duration}s")
        animate.set("begin", f"{start_time}s;{start_time + total_cycle_time}s")
        animate.set("fill", "freeze")
        animate.set("repeatCount", "indefinite")

    # Add text elements with animation
    y_pos = height / 2 + size / 3  # Better vertical centering
    for i, text in enumerate(text_list):
        text = urllib.parse.unquote(text.strip())
        
        # Get animation timing
        start_time, end_time = animation_segments[i]
        display_duration = end_time - start_time
        
        # Group for text and its animations
        g = ET.SubElement(svg, "g")
        g.set("clip-path", f"url(#clip{i})")
        
        # Create text element
        text_elem = ET.SubElement(g, "text", x="10", y=str(y_pos), fill=color)
        text_elem.set("font-family", font)
        text_elem.set("font-size", str(size))
        text_elem.text = text
        print(i, " : ", text)
        # Add display animation to control visibility
        # Initial opacity is 0 to hide all text elements at the start
        g.set("opacity", "0")
        
        # Visibility animation - only show during this text's segment
        animate_opacity = ET.SubElement(g, "animate", attributeName="opacity")
        animate_opacity.set("values", "0;1;1;0")
        animate_opacity.set("keyTimes", f"0;0.01;0.99;1")  # Quick fade in/out
        animate_opacity.set("dur", f"{display_duration}s")
        animate_opacity.set("begin", f"{start_time}s;{start_time + total_cycle_time}s")
        animate_opacity.set("fill", "freeze")  # Keep final state
        animate_opacity.set("repeatCount", "indefinite")

    # Convert SVG to string
    return ET.tostring(svg, encoding="unicode")

@app.route("/typing-svg")
def generate_svg():
    # Get query parameters
    texts = request.args.get("lines", "")
    font = request.args.get("font", "Fira Code")
    color = request.args.get("color", "#bfcfde")
    size = request.args.get("size", "22")
    width = request.args.get("width", "440")
    height = request.args.get("height", "45")
    theme = request.args.get("theme", "light")
    delay = request.args.get("delay", "1000")  # Default 1000ms delay
    speed = request.args.get("speed", "10")   # Default speed of 10 chars per second

    # Generate SVG
    svg_content = create_typing_svg(texts, font, color, size, width, height, theme, delay, speed)

    # Return SVG response
    return Response(svg_content, mimetype="image/svg+xml")

if __name__ == "__main__":
    app.run(debug=True)