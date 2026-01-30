# Brijesh Careers Website

## Overview
A Flask-based careers website that displays job listings and allows users to view job details.

## Project Structure
```
├── app.py              # Main Flask application
├── templates/          # Jinja2 HTML templates
│   ├── base.html       # Base template with header/footer
│   ├── home.html       # Homepage with job listings
│   └── job.html        # Individual job detail page
├── static/
│   └── style.css       # CSS styles
├── pyproject.toml      # Python dependencies (managed by uv)
└── README.md           # Project description
```

## Running the Application
The application runs on port 5000 using Flask's built-in development server.

```bash
python app.py
```

## Routes
- `/` - Homepage displaying all job listings
- `/job/<id>` - Individual job detail page

## Dependencies
- Flask - Web framework

## Recent Changes
- January 30, 2026: Initial setup with Flask, templates, and styling
