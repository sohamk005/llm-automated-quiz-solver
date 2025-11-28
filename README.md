# TDS Project 2: LLM Analysis Quiz Bot

This project is an automated agent designed to solve data analysis quizzes presented via a web interface. It utilizes FastAPI for the endpoint, Playwright for headless browser scraping, and an LLM (OpenAI/GPT) to interpret questions and generate Python code for data processing.

## Project Structure

- `main.py`: The FastAPI application entry point. Handles the `/run` POST request, validates the secret, and triggers the background task.
- `utils.py`: Contains the core logic:
  - **Scraping:** Uses Playwright to extract text from the quiz URL.
  - **Reasoning:** Sends the page content to an LLM to identify the question and write a solution script.
  - **Execution:** Executes the generated Python code to derive the answer.
  - **Submission:** Submits the answer to the quiz API and handles the loop if a next task URL is returned.
- `Dockerfile`: Configuration for deploying the application with Python and Playwright dependencies.

## Features

- **Asynchronous Processing:** Uses FastAPI `BackgroundTasks` to handle long-running scraping/LLM tasks without timing out the initial API request.
- **Dynamic Solving:** The agent writes its own code to solve data problems (CSV parsing, calculation, etc.).
- **Automatic Navigation:** Handles chained quiz questions (solving one question leads to the next URL).

## Setup & Deployment

The project is designed to be deployed on a platform supporting Docker (e.g., Render.com).

### Environment Variables

The application requires the following environment variables:

- `AIPROXY_TOKEN`: The API token for the LLM service (or `OPENAI_API_KEY` if using direct OpenAI).
