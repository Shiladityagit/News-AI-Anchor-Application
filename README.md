# AI News Anchor

## Overview

**AI News Anchor** is an automated news channel application built using Python, Streamlit, and D-ID's API. The application fetches the latest news based on a selected category and generates a video featuring an AI-driven news anchor delivering the news. The AI anchor's speech is dynamically generated, making it a unique and engaging way to consume news.

## Features

- **Automated News Retrieval:** Fetches the latest news based on user-defined categories.
- **AI News Anchor:** Generates videos of an AI news anchor reading out the news.
- **Customizable:** Users can select the number of news items to be read and customize the news category.
- **Interactive UI:** A user-friendly interface powered by Streamlit.

## Setup and Installation

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher installed on your local machine.
- `pip` package manager.
- [D-ID API Key](https://www.d-id.com) for video generation.
- [News API Key](https://newsapi.org/) for fetching news.

### Installation

1. **Clone the Repository:**

2. **Create and Activate a Virtual Environment (optional but recommended):**

3. **Install the Required Packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables:**

    Create a `.env` file in the root directory of your project with the following content:

    ```plaintext
    NEWS_API_KEY=your_news_api_key_here
    BEARER_TOKEN=your_did_bearer_token_here
    ```

5. **Run the Application:**

    ```bash
    streamlit run app.py
    ```

    This command will start the application, and you can access it through your browser at `http://localhost:8501`.

## Usage

1. **Enter News Category:** Type the desired news category (e.g., "Technology," "Sports").
2. **Select Number of News Items:** Use the slider to choose how many news items you want the AI anchor to read.
3. **Generate Video:** Click the "Generate" button to fetch the news and generate the AI news anchor video.
4. **View the Video:** Watch the generated video directly in the browser.

## File Structure

- **`app.py`:** The main application file.
- **`news_api.py`:** Contains the `NewsAPI` class for interacting with the News API.
- **`news_video.py`:** Contains the `VideoGenerator` class for generating videos with the D-ID API.
- **`requirements.txt`:** Lists all the required Python packages.
- **`.env`:** Stores environment variables (not included in the repo for security reasons).

## Customization

- **Logo:** Update the `logo_url` in `app.py` to point to your logo image.
- **Anchor Image:** Update the `image_url` to change the anchor's image.
- **Voice:** Customize the AI anchor's voice by modifying the `voice_id` in the `VideoGenerator` class.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any improvements or bug fixes.
