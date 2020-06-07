import webbrowser

# You can change the link to whatever link you want to use
link = 'https://teamtreehouse.com/michaelcronk'  # You can insert your desired link here


def run_website():
    try:
        webbrowser.open(link, new=2, autoraise=True)
        print(link)
    except ValueError:
        print("That's not a valid link. Please try again.")


run_website()
