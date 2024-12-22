# feeds.py

import feedparser

# List of RSS feed URLs
rss_feeds = [
    "https://www.detroitbadboys.com/rss/current.xml",
    "https://www.wxyz.com/sports/basketball/pistons.rss",
    "https://sports.yahoo.com/nba/teams/detroit/rss.xml",
    "https://www.hoopsrumors.com/detroit-pistons/feed",
    "https://hoopshype.com/team/detroit-pistons/feed/",
    "https://pistonpowered.com/feed/",
    "https://www.palaceofpistons.com/feed/",
    "https://rssfeeds.detroitnews.com/detroit/pistons"
]

# Store articles in a list
articles = []

# Function to fetch and parse RSS feed
def fetch_feed(url):
    return feedparser.parse(url)

# Function to update feeds
def update_feeds():
    global articles
    articles = []  # Clear previous articles
    for feed_url in rss_feeds:
        feed = fetch_feed(feed_url)
        for entry in feed.entries:
            articles.append({
                "title": entry.title,
                "link": entry.link,
                "published": entry.published,
                "summary": entry.summary,
                "source": feed.feed.title
            })
    print("Feeds updated")

# Function to search articles by keyword
def search_articles(keyword):
    result = [article for article in articles if keyword.lower() in article["title"].lower() or keyword.lower() in article["summary"].lower()]
    return result
