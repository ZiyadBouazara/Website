from website import create_app

app = create_app()

if __name__ == '__main__':  # Run the server only if we run this file (main)
    app.run(debug=True)
    # Each time we make a change in the code, the server will be rerunned.
    # This will be turned off when website will be fully functional.
    # but for now, we dont want to rerun the server manually each time.
