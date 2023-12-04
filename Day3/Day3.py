'''
--- Day 3: Gear Ratios ---
You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?
'''
from datetime import datetime

def getNumAndIndex(i, j, lines):
    curChar = lines[i][j]
    curNum = ""
    while (curChar.isdigit()):
        curNum += curChar
        if (isValidIndex(i, j+1, lines)):
            j += 1
            curChar = lines[i][j]
        else:
            return [int(curNum), j]

    return [int(curNum), j-1]

def checkAdjSymbol(i, startJ, endJ, lines):
    j = startJ
    while j <= endJ:
        for adj in adjIndices:
            for symbol in symbols:
                if isValidIndex(i+adj[0], j+adj[1], lines):
                    if lines[i+adj[0]][j+adj[1]] == symbol:
                        return True
        j += 1
    return False

def isValidIndex(i, j, lines):
    if (i >= 0 and i < len(lines)):
        if (j >= 0 and j < len(lines[0])): 
            return True
    return False

p1start = datetime.now()
adjIndices = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [0, -1], [1, -1], [1, 0], [1, 1]]
symbols = ['=', '+', '-', '@', '#', '$', '%', '&', '*', '/']
schematic = open("AdventOfCode2023\Day3\engine.txt", "r")
lines = schematic.readlines()
sum = 0
i = 0
while (i < len(lines)):
    j = 0
    while (j < len(lines[i])):
        curChar = lines[i][j]
        if curChar.isdigit():
            startIndex = j
            curNum = getNumAndIndex(i, j, lines)[0]
            endIndex = getNumAndIndex(i, j, lines)[1]
            j = getNumAndIndex(i, j, lines)[1]
            if (checkAdjSymbol(i, startIndex, endIndex, lines)):
                sum += curNum
        j += 1
    i += 1
print(sum)
p1end = datetime.now()
print("Part 1: " + str(p1end-p1start))
