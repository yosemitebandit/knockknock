def webhook(request):
    if request.method == "POST":
        event_data = request.get_json()
        print("Received event:", event_data)
        # Add any logic here to process the event
        return "Event received", 200
    else:
        return "Only POST method accepted", 405
