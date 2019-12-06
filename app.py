"""Main app file."""
from eventbrite import Eventbrite
import config

# import json


def main():
    """Main."""
    # location = input("Enter a city to find out events for this week: ")
    # print(location)
    get_eventbrite_events()


def get_eventbrite_events():
    """Get events from eventbrite."""
    eb = Eventbrite(config.EVENTBRITE_TOKEN)
    # me = eb.event_search(**{"user.id": eb.get_user()["id"]})
    # print(json.dumps(me))

    has_more = True
    events = []
    while has_more:
        search_results = eb.event_search(
            **{"location.address": "New+York", "location.within": "5mi"}
        )
        has_more = search_results.get("pagination", "").get(
            "has_more_items", False
        )
        for i in search_results.get("events", []):
            events.append(
                {
                    "id": i.get("id"),
                    "name": i.get("name").get("text"),
                    "description": i.get("description").get("text"),
                    "summary": i.get("summary"),
                    "start": i.get("start").get("local"),
                    "end": i.get("end").get("local"),
                    "status": i.get("status"),
                    "url": i.get("url"),
                }
            )

    return search_results["events"]


if __name__ == "__main__":
    main()
