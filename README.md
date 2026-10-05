---
title: AI Student Assistant
emoji: 🎓
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 5.49.1
app_file: app.py
pinned: false
---

# 🎓 AI Student Assistant

A simple AI Student Assistant built with Python and Gradio.

## Features

- School-related questions
- Attendance questions
- Homework help
- General academic questions
- LLM-powered responses

## Deployment

This project is designed for Hugging Face Spaces.

### Required Secret

Add this secret in your Space:

`OPENROUTER_API_KEY`

The application reads the API key from the environment and does not store it in the source code.

## Architecture

Browser → Gradio → Python → OpenRouter → LLM

## Future versions

- V2: School policy PDF + RAG
- V3: PostgreSQL student database
- V4: AI Agent + MCP
