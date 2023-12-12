# FastAPI-Gradio Collaborators Interface

This project is a FastAPI application integrated with Gradio to create an interactive web interface. It allows users to select a collaborator from a dropdown list and view relevant data, which is fetched from an Excel file.

## Features

- FastAPI backend for serving collaborator data.
- Gradio interface for interactive user experience.
- Reading and parsing data from an Excel file.

## Installation & Setup

Make sure you have Python 3.6+ installed on your system. If you don't, you can download it from [python.org](https://www.python.org/downloads/).

### Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://your-repository-url-here.git
cd FastAPI-Gradio-Colaboradores
```



### Create a Virtual Environment
To create a new virtual environment, run:
```
python3 -m venv patagonian
```

### Activate the Virtual Environment
Before working on the project, you need to activate the corresponding environment:


# On macOS and Linux:
```
source patagonian/bin/activate
```
# On Windows:
```
patagonian\Scripts\activate
```

You'll know the virtual environment is active because its name will appear in parentheses in your terminal.

# Install Dependencies
With the virtual environment activated, install the project dependencies:

```
pip install -r requirements.txt
```
This command reads the requirements.txt file and installs all the necessary packages.

# Running the Application
Once the setup is done, you can run the FastAPI application using Uvicorn:
```
uvicorn main:app --reload
```

The --reload flag is optional and makes the server restart after code changes.

The FastAPI server will start, and you should see output similar to:

# INFO:
     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
Now, you can open your web browser and go to http://127.0.0.1:8000 to see the API in action.

To interact with the Gradio interface, navigate to the URL provided in the terminal, usually http://127.0.0.1:7860.


# Project Structure

main.py: The FastAPI application entry point.
data_processing.py: Contains logic to read and process data from the Excel file.
gradio_interface.py: Defines the Gradio interface for the application.
Staff Feedback - PX _ Specialists _ RRHH.xlsx: The Excel file with collaborator data.
