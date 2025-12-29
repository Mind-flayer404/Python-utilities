import webbrowser
import logging
import time

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def open_links_in_browser(links, delay=2):
    for link in links:
        try:
            logger.info(f"Opening link: {link}")
            webbrowser.open_new_tab(link)
            time.sleep(delay)
        except Exception as e:
            logger.error(f"Failed to open link {link}: {e}")


if __name__ == "__main__":
    # Replace the sample links with your desired URLs to open
    sample_links = [
        "https://www.github.com",
        "https://www.google.com",
        "https://www.youtube.com"
    ]
    
    # Time delay of 3 seconds between opening each link to not overwhelm the browser
    open_links_in_browser(sample_links, delay=3)