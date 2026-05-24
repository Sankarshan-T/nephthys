from nephthys.utils.env import env
from nephthys.views.home.components.header import get_header


def get_loading_view(home_type: str):
    return {
        "type": "home",
        "blocks": [
            *get_header(user=None, current=home_type),
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":hourglass_flowing_sand: loading...",
                },
            },
            {
                "type": "image",
                "image_url": "https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif",
                "alt_text": "Loading...",
            },
        ],
    }
