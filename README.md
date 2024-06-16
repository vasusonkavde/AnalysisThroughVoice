# AnalysisThroughVoice
This project offers an innovative web-based application that enables users to analyze sales data through natural language processing and voice commands. Developed with Python, Flask, and Bootstrap, it leverages the Web Speech API to capture and process spoken instructions, providing an intuitive, hands-free data exploration experience. The application supports 26 distinct analysis methods, allowing users to perform a variety of tasks such as generating sales summaries, analyzing revenue and profit by different segments (year, country, product), and examining customer demographics. Results are dynamically displayed on the web interface, either in table format or as plain text, based on the type of analysis requested. The backend employs Python's difflib library to match user voice commands with the closest predefined analysis methods, ensuring a seamless interaction even if the commands are not perfectly accurate. To use the application, clone the repository, install the necessary dependencies, place your sales data CSV file (sales_data.csv) in the project directory, and run the application. 

# Installation
   git clone https://github.com/vasusonkavde/AnalysisThroughVoice.git
   cd AnalysisThroughVoice
   
# Install dependencies:
   pip install -r requirements.txt
   
# Prepare your data:
   Place your sales data CSV file as sales_data.csv in the project directory.

# Usage
   1. Run the application:
        python main.py
   2. Access the application:
        Open your web browser and go to 'local host URL'
      
# Features
   1. Voice Command Integration: Utilizes Web Speech API for voice recognition.
   2. Dynamic Data Display: Presents results as tables or text based on the analysis.
   3. Fuzzy Command Matching: Uses difflib for accurate voice command interpretation.

# Libraries Used
   1. Flask: Web framework for Python.
   2. Pandas: Data manipulation and analysis.
   3. Bootstrap: Frontend framework for responsive design.
   4. difflib: Fuzzy matching for voice command recognition.
   5. SpeechRecognition: Library for speech recognition functionality.
