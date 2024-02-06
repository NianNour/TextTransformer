# TextTransformer
Well, I'm at the beginning of my way of learning python. 
I'm going to upload mini-projects.
I'm going to upload mini-projects during the journey. 
I hope you follow up.

Here's a description of the code:

1. Input:

The code starts by prompting the user to enter a statement using the input() function.
2. Vowel List Creation:

It defines a list called vowels containing all lowercase and uppercase vowels to be used for replacement later.
3. Whitespace Removal:

It removes any whitespace characters (spaces, tabs, etc.) from the statement using the replace(" ", "") method, ensuring a consistent text format.
4. Case Swapping:

It inverts the case of each character in the statement using the swapcase() method, making uppercase letters lowercase and vice versa.
5. Vowel Replacement:

It iterates through each character in the statement:
If the character is found in the vowels list, it's replaced with a dot (".") using the replace() method.
6. Output:

Finally, it prints the modified statement with vowels replaced by dots, whitespaces removed, and case inverted.
