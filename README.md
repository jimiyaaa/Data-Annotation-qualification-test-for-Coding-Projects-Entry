  This is a function to answer the problem given on DataAnnotation.tech (a webapp for AI model trainer) on qualification test for Coding Projects Entry. 
  
  My code works by first getting the HTML data from the given URL, then selecting the table presented in the HTML text to extract its text contents. Then, using regex, it 
will store the coordinate values inside the "coors" list and the characters inside the "chars" list before reconstructing their structure. "chars" list is flattened and 
the string values are stored inside a new list, "charstring" on line 25, which also can also be written with "chars" like the existing one to save memory, but I wrote it 
as a new list to avoid confusion and increase readability.  Next, the items inside "coors" list (the coordinates) will be cast to integer because the data were strings. 
And again the values is stored in a new list "coorsint" to avoid confusion. 

  Then using the coordinates it will find the largest x and y values to determine the size of the grid before creating the grid with space character. Then, it will place 
the character accordingly by iterating through "coorsint" list to get the coordinates values, and iterating through  "charstring" list to get the characters to be placed.
Then it will iterate through the reversed "grid" list and join the item. The "grid" list is reversed because the coordinate (0,0) needs to be put on the bottom let of 
the grid.
