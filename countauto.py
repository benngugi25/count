filename = input("Enter file name: ")

total = 0

with open(filename, "r") as file:
    for line in file:
        parts = line.split()
        if parts:
            try:
                total += int(parts[-1])
            except ValueError:
                pass   # ignore lines without numbers

print("Total =", total)
