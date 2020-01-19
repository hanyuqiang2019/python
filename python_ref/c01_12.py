def countdown(n):
    print("Counting down!")
    while n > 0:
        yield n
        n -= 1

c=countdown(5)
i = c.__next__()
print("i = %d" % i)
c.close()

for i in countdown(5):
    print("i = %d" % i)
