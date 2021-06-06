characters = []
with open("JJK.txt") as f:
    for line in f:
        characters.append(line.strip())

for val in characters:
    print(val)
