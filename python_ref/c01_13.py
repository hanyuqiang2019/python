def print_matches(matchtext):
    print("Looking for", matchtext)
    while True:
        line = (yield)
        if matchtext in line:
            print(line)

matcher = print_matches("python")
matcher.__next__()
matcher.send("Hello World")
matcher.send("python is cool")
matcher.send("yow!")
matcher.close()
