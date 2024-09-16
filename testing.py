# file used for testing.
# empty at the moment.
while True:
    try:
        exec(input(">>> "))
    except Exception as e:
        print(f"Exception:\n{e}")