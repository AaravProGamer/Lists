l = []
for _ in range(int(input())):
    cmd, *args = input().split()
    if cmd == "insert":
        l.insert(int(args[0]), int(args[1]))
    elif cmd == "print":
        print(l)
    elif cmd == "remove":
        l.remove(int(args[0]))
    elif cmd == "append":
        l.append(int(args[0]))
    elif cmd == "sort":
        l.sort()
    elif cmd == "pop":
        l.pop()
    elif cmd == "reverse":
        l.reverse()
