import os
import gradio as gr
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ.get("OPENROUTER_API_KEY")
)

def ask_student_assistant(message, history):
    try:
        response = client.chat.completions.create(
            model="inclusionai/ling-3.1-flash",
            messages=[
                {
                    "role": "system",
                    "content": """
You are an AI Student Assistant.

Help students with:
- School rules
- Attendance
- Homework
- General academic questions

Give simple and clear answers suitable for students.
"""
                },
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"


demo = gr.ChatInterface(
    fn=ask_student_assistant,
    title="🎓 AI Student Assistant",
    description="Ask questions about school, attendance, homework and academics.",
    examples=[
        "What is the minimum attendance requirement?",
        "How can I prepare for my exams?",
        "Explain photosynthesis in simple words."
    ]
)

demo.launch()
