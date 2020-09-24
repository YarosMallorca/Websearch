import eel
import webbrowser
import sys

@eel.expose
def search(query, engine):
    query = query.replace(" ", "+")
    if engine == "Google":
        webbrowser.open("https://www.google.com/search?q=" + query)

    elif engine == "YouTube":
        webbrowser.open("https://www.youtube.com/results?q=" + query)

    elif engine == "Amazon":
        webbrowser.open("https://www.amazon.com/s?k=" + query)

    elif engine == "Wikipedia":
        query = query.replace(" ", "_")
        webbrowser.open("https://www.wikipedia.org/wiki/" + query)

eel.init("static")
eel.start('index.html', size=(800, 400))
