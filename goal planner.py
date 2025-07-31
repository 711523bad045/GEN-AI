# ✅ Step 1: Install Gradio (only needed once)
!pip install -q gradio

# ✅ Step 2: Define your Goal Planner function
def generate_plan(goal):
    # You can make this smarter later – for now just a simple reply
    goal = goal.strip()
    if not goal:
        return "❌ Please enter a goal first."
    
    # Simple mock plan
    return f"""🎯 Action Plan for: {goal}

1. Break the goal into 3 key steps.
2. Assign deadlines for each step.
3. Track your daily progress using a journal or app.
4. Review weekly and adjust plan if needed.
5. Celebrate success! 🎉
"""
# ✅ Step 3: Launch with Gradio
import gradio as gr

gr.Interface(
    fn=generate_plan,
    inputs=gr.Textbox(placeholder="Enter your goal, e.g., 'Improve my coding skills'"),
    outputs="text",
    title="🚀 Goal Planner",
    description="Convert your goals into a simple action plan."
).launch()
