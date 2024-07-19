# Python script to generate 24 HTML files based on user input for the level

# Template HTML content
html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ESL Learning Portal - Choose Your Activity</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            background-color: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        h1 {
            color: #333;
            margin-bottom: 1.5rem;
        }
        .activity-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 1rem;
            margin-top: 2rem;
        }
        .activity-button {
            padding: 1rem;
            font-size: 1.2rem;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .activity-button:hover {
            opacity: 0.8;
        }
        .activity-button.vocabulary {
            background-color: #007bff;
        }
        .activity-button.grammar {
            background-color: #28a745;
        }
        .activity-button.listening {
            background-color: #ffc107;
            color: black;
        }
        .activity-button.reading {
            background-color: #dc3545;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Choose Your Activity</h1>
        <p>Please select the type of activity you want to do:</p>
        <div class="activity-grid">
            <button class="activity-button vocabulary" onclick="selectActivity('v')">Vocabulary</button>
            <button class="activity-button grammar" onclick="selectActivity('g')">Grammar</button>
            <button class="activity-button listening" onclick="selectActivity('l')">Listening</button>
            <button class="activity-button reading" onclick="selectActivity('r')">Reading</button>
        </div>
    </div>

    <script>
        function selectActivity(activityKey) {
            // Get the current filename
            const path = window.location.pathname;
            const currentFile = path.substring(path.lastIndexOf('/') + 1);

            // Extract the level, week, and day from the filename
            const match = currentFile.match(/^(\w+)(activity_options_w\d+d\d+)\.html$/);

            if (!match) {
                alert('Filename format is incorrect!');
                return;
            }

            const level = match[1];
            const weekDay = match[2];

            // Construct the new filename
            const filename = `${level}${weekDay}${activityKey}1.html`;

            console.log("Redirecting to:", filename);  // Debugging statement
            window.location.href = filename;
        }
    </script>
</body>
</html>'''

def create_html_files(level):
    for week in range(1, 13):
        for day in range(1, 3):
            filename = f"{level}activity_options_w{week}d{day}.html"
            with open(filename, 'w') as file:
                file.write(html_content)
            print(f"Created file: {filename}")

if __name__ == "__main__":
    level = input("Enter the level (e.g., A1, B2): ")
    create_html_files(level)