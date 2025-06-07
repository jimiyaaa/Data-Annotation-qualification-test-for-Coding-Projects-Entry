import requests
from bs4 import BeautifulSoup
import re

def data (url):
    #gets the data from given url and return it as string
    source = requests.get(url)
    html = source.text

    #parses the html string and specifically selects lines with <tr> tag and return it as lists
    soup = BeautifulSoup(html, "html.parser")
    table = soup.select('tr')

    #identifies the coordinates. This gave us a list (coors) containing lists of coordinate from table data we fetched before
    coors = []
    for i in [i.text for i in table[1:]]:
        coors.append(re.findall("\d+", i))

    #identifise the character. This will store our character as string inside a list tha is wrapped again in the chars list
    chars = []
    for i in [i.text for i in table[1:]]:
        chars.append(re.findall("\D+", i))

    #gets every character out of achars list and just store it as strings inside a new list because we need to iterate through this later
    charstring = [i[0] for i in chars]

    #converts coordiante strings to integers. this is necessary because we neeed to do math operation later
    coorsint = [(int(x), int(y)) for x, y in coors]

    #finds the largest x and y
    max_x = max(x for x, y in coorsint)+1
    max_y = max(y for x, y in coorsint)+1

    #creates the grid layout or the mainboard with space
    grid = [[' ' for g in range(max_x)] for g in range(max_y)]

    #places the respective character according to its coordinate
    for coor in coorsint:
        for char in charstring:
            grid[coor[1]][coor[0]]=char

    #print out the output letter with the grid being reversed to make (0,0) coordinate sits at bottom left of the terminal
    for letter in reversed(grid):
        print("".join(letter))