try:
    with open("week 4/example.txt", "r") as file:
        data = file.read()
        print(data)
except Exception as e:
    print(f"An error occurred: {e}")
