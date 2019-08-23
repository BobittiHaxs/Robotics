numLines = int(input("Number of lines: "))
startLine = input("Start line: ")
print(startLine)
for i in range(numLines-1):
    newLine = []
    for j in range(len(startLine)):
        left = startLine[j-1]
        right = startLine[j+1-len(startLine)]
        if left == ".":
            if right == ".":
                newLine.append(".")
            else:
                newLine.append("*")
        else:
            if right == ".":
                newLine.append("*")
            else:
                newLine.append(".")
    startLine = ''.join(newLine)
    print(startLine)
