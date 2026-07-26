import json
import os

FILE_NAME = "posted.json"


def load_posts():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []


def save_posts(posts):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(posts, f)


def is_posted(link):
    posts = load_posts()
    return link in posts


def mark_posted(link):
    posts = load_posts()

    if link not in posts:
        posts.append(link)
        save_posts(posts)
