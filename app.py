from flask import Flask, render_template
import feedparser
import schedule
import time

app = Flask(__name__)

@app.route('/')
def index():
    query = "example query"
    results = search_articles(query)
    return render_template('index.html', articles=results, query=query)

def search_articles(query):
    # Example function to search articles
    return []

def update_feeds():
    # Function to update RSS feeds
    pass

# Schedule the update every 2 hours
schedule.every(2).hours.do(update_feeds)

# Initial feed update
update_feeds()

# Run Flask app in a separate thread to allow schedule to run
if __name__ == '__main__':
    from threading import Thread

    def run_schedule():
        while True:
            schedule.run_pending()
            time.sleep(1)

    schedule_thread = Thread(target=run_schedule)
    schedule_thread.start()

    app.run(debug=True)