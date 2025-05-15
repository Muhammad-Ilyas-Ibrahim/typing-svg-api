from flask import Flask, request, Response
import xml.etree.ElementTree as ET
import urllib.parse

app = Flask(__name__)

def create_typing_svg(texts, font, color, size, width, height, theme):
    # Default values
    font = font or "Fira Code"
    color = color or "#bfcfde"
    size = int(size) if size and size.isdigit() else 22
    width = int(width) if width and width.isdigit() else 440
    height = int(height) if height and height.isdigit() else 45
    theme = theme or "light"
    bg_color = "#ffffff" if theme == "light" else "#1a1a1a"

    # Split texts if provided as semicolon-separated
    text_list = texts.split(";") if texts else ["Welcome to my profile"]

    # Create SVG root
    svg = ET.Element("svg", width=str(width), height=str(height), xmlns="http://www.w3.org/2000/svg")
    svg.set("style", f"background-color: {bg_color};")

    # Add text elements with animation
    y_pos = height / 2
    total_duration = 0
    for i, text in enumerate(text_list):
        text = urllib.parse.unquote(text.strip())
        text_len = len(text)
        duration = text_len * 0.1 + 1  # Typing duration + pause

        # Create text element
        text_elem = ET.SubElement(svg, "text", x="10", y=str(y_pos), fill=color)
        text_elem.set("font-family", font)
        text_elem.set("font-size", str(size))
        text_elem.text = text

        # Add typing animation
        animate = ET.SubElement(text_elem, "animate", attributeName="opacity")
        animate.set("values", "0;1;1;0")
        animate.set("dur", f"{duration}s")
        animate.set("begin", f"{total_duration}s")
        animate.set("repeatCount", "indefinite")

        total_duration += duration + 0.5  # Add gap between animations

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

    # Generate SVG
    svg_content = create_typing_svg(texts, font, color, size, width, height, theme)

    # Return SVG response
    return Response(svg_content, mimetype="image/svg+xml")

if __name__ == "__main__":
    app.run(debug=True)