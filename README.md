# AI Math Tutor

A small Streamlit web app that acts as an AI-powered math tutor for middle-school students (5th–7th grade). The app presents grade-specific math topics, lets the student choose a topic, and a Large Language Model (LLM) generates multiple-choice practice questions. It is designed to be extended with an LLM such as OpenAI or Claude Anthropic to dynamically generate questions and feedback.

Features
- Grade-level topic selection (5th, 6th, 7th grade)
- Browse common math topics for each grade
- Select a topic and generate a sample multiple-choice question which gives feedback once an answer is submitted
- Lightweight Streamlit UI and simple session-state navigation between topic list and question view

Why this repo
This project is a minimal starting point for an AI tutor focused on math fundamentals. The code is intentionally small so you can:

- Hook up an LLM (OpenAI, local LLM) to generate adaptive questions and explanations
- Add correctness checking, scoring, and progress tracking
- Improve UX and add multimedia (images, equations)

Contents
- `app.py` — main Streamlit application (topic selection, question generation placeholder)
- `requirement.txt` — Python dependencies
- `README.md` — this file

Quick start (local)

1. Create a virtual environment (Ran and Tested on Python 3.13.7) and activate it (Windows PowerShell):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirement.txt
```

3. Configure your OpenAI API key (optional, required to enable LLM question generation):

- The app expects the OpenAI API key to be provided via Streamlit secrets or by uncommenting the assignment in `app.py`.
- Recommended: create a `secrets.toml` under `~/.streamlit/` or in the repo (for local testing) with the following content:

```toml
# ~/.streamlit/secrets.toml
OPENAI_API_KEY = "your_openai_api_key_here"
```

Alternatively, you can set the environment variable `OPENAI_API_KEY` or directly assign `openai.api_key` in `app.py` (less secure).

4. Run the app:

```powershell
streamlit run app.py
```

5. Open the browser at the URL printed by Streamlit (usually http://localhost:8501).

How the app works (based on `app.py`)
- On first load the app shows a grade selector (5th–7th) and a list of common math topics for that grade.
- Clicking a topic switches the view to a question page for that topic. The code currently shows a placeholder sample question when "Generate Question" is pressed.
- The app uses `st.session_state` to track the current view (`topic_selection` vs `question_page`) and the `selected_topic`.

Where to extend (suggestions)
- Integrate with OpenAI (or another LLM):
	- Un-comment and adapt the `generate_question` function in `app.py` to call OpenAI's API and return a formatted multiple-choice question.
	- Send the selected grade and topic in the prompt so the model tailors difficulty and vocabulary.
- Add answer checking & feedback:
	- Store the correct answer alongside the generated question, present options as radio buttons, and show immediate feedback.
- Add persistence and user accounts:
	- Save user progress, scores, and history to a small database (SQLite for local testing) or cloud backend.
- Improve safety and appropriateness:
	- Sanitize model output, add content filters, and limit generation length and temperature.

Notes on security and costs
- If you enable OpenAI calls, monitor usage to avoid unexpected cost. Use low temperature and token limits for deterministic short questions.
- Never commit API keys to source control. Use `secrets.toml`, environment variables, or your cloud provider's secret manager.

Troubleshooting
- "Module not found": ensure you installed dependencies into the active virtual environment.
- Streamlit fails to start: ensure you activated the venv and `streamlit` is installed. On Windows PowerShell, execution policy may block running scripts; use `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` if necessary (requires admin privileges).

License and contribution
This repository is a learning/demo project. Feel free to open issues or submit pull requests to improve question generation, add tests, or expand topics.

Contact
If you want help integrating a specific LLM, adding unit tests, or designing a learning tracking schema, open an issue or reach out via the project contact info.

---

Last Modified on: 2025-09-29

