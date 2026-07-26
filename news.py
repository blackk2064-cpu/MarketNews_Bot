import feedparser

RSS_URL = "https://www.investing.com/rss/news.rss"


def get_news():
    feed = feedparser.parse(RSS_URL)

    news = []

    for entry in feed.entries:
        news.append(
            {
                "title": entry.title,
                "link": entry.link,
            }
        )

    return news
