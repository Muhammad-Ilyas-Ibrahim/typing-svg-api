# Typing SVG API

🎯 Create beautiful animated typing text for your GitHub profile README or website! This Flask-based API generates dynamic SVG animations that make your profile stand out.

<p align="center">
  <img src="https://typing-svg-api.onrender.com/typing-svg?lines=Welcome%20to%20Typing%20SVG%20API;Make%20your%20GitHub%20profile%20dynamic!&font=Fira%20Code&color=%23bfcfde&size=22&width=440&height=45&theme=dark">
</p>

## ✨ Features

- 🎨 Fully customizable animated typing SVGs
- 📝 Support for multiple text lines with custom delays
- 🎯 Perfect for GitHub READMEs and personal websites
- 🌓 Light and dark theme support
- 🚀 Easy deployment on Render
- 💯 Free and open source

## 🚀 Quick Start

### 1️⃣ Using the API

Simply add this to your README.md:

```markdown
<p align="center">
  <img src="https://typing-svg-api.onrender.com/typing-svg?lines=Your%20Text%20Here;Another%20Line&theme=dark">
</p>
```

### 2️⃣ Customization Options

The API endpoint is `/typing-svg` with these parameters:

| Parameter | Description | Default | Example |
|-----------|-------------|---------|---------|
| `lines` | Semicolon-separated text lines | `Welcome` | `Hello%20World;I'm%20a%20Developer` |
| `font` | Font family | `Fira Code` | `Arial` |
| `color` | Text color (hex) | `#bfcfde` | `%23ffffff` |
| `size` | Font size (pixels) | `22` | `20` |
| `width` | SVG width (pixels) | `440` | `500` |
| `height` | SVG height (pixels) | `45` | `50` |
| `theme` | Background theme | `light` | `dark` |
| `delay` | Delay between lines (seconds) | `0.5` | `1.0` |

### 3️⃣ Example URLs

**Dark Theme**:
```
https://typing-svg-api.onrender.com/typing-svg?lines=Full-Stack%20Developer;Open%20Source%20Enthusiast&theme=dark&delay=1.0
```

**Custom Style**:
```
https://typing-svg-api.onrender.com/typing-svg?lines=Hello%20World&font=Arial&color=%23ff0000&size=30&width=300&height=50&theme=light
```

## 💻 Run Locally

1. **Clone and Setup**:
   ```bash
   git clone https://github.com/Muhammad-Ilyas-Ibrahim/typing-svg-api.git
   cd typing-svg-api
   pip install -r requirements.txt
   ```

2. **Run the Server**:
   ```bash
   python app.py
   ```

3. **Test it Out**:
   Visit: `http://localhost:5000/typing-svg?lines=Hello%20World&theme=dark`

## API Usage

The API endpoint is `/typing-svg`. It accepts the following query parameters:

| Parameter | Description | Default | Example |
|-----------|-------------|---------|---------|
| `lines` | Semicolon-separated text lines | None | `Data%20Science;AI` |
| `font` | Font family | `Fira Code` | `Arial` |
| `color` | Text color (hex) | `#bfcfde` | `#ffffff` |
| `size` | Font size (pixels) | `22` | `20` |
| `width` | SVG width (pixels) | `440` | `500` |
| `height` | SVG height (pixels) | `45` | `50` |
| `theme` | Background theme | `light` | `dark` |
| `delay` | Delay between lines (seconds) | `0.5` | `1.0` |

**Example Request**:
```
https://typing-svg-api.onrender.com/typing-svg?lines=Data%20Science%20Enthusiast;Learning%20AI&font=Fira%20Code&color=%23bfcfde&size=22&width=440&height=45&theme=dark
```

**Add to GitHub README**:
```markdown
<p align="center">
  <img src="https://typing-svg-api.onrender.com/typing-svg?lines=Your%20Text;Another%20Line&font=Fira%20Code&color=%23bfcfde&size=22&width=440&height=45&theme=dark">
</p>
```

## Deployment on Render

1. **Push to GitHub**:
   Ensure your repository (`https://github.com/your_username/typing-svg-api`) contains:
   - `app.py`
   - `requirements.txt`
   - `Procfile`
   - `runtime.txt`
   - `.gitattributes`

2. **Create a Render Web Service**:
   - Sign in to [Render](https://render.com) with GitHub.
   - Click **New** > **Web Service**, connect to `your_username/typing-svg-api`, and select the `main` branch.
   - Configure:
     - **Name**: `typing-svg-api`
     - **Environment**: Python
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app`
     - **Instance Type**: Free
     - **Auto-Deploy**: Enable
   - Click **Create Web Service**.

3. **Get the URL**:
   After deployment (5–10 minutes), Render provides a URL (e.g., `https://typing-svg-api.onrender.com`). Update the README with this URL.

## Project Structure

```
typing-svg-api/
├── app.py              # Flask API code
├── requirements.txt    # Python dependencies
├── Procfile            # Render deployment config
├── runtime.txt         # Python version
├── .gitattributes      # Line ending config
└── README.md           # Project documentation
```

## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit changes (`git commit -m 'Add YourFeature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License.
