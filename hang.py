import random
words=("apple" "banana" "cherry" "date" "elderberry" "fig" "grape" "honeydew")
hangman_art={0:("   ",
                "   ",
                "   "), 
             1:(" o ",
                "   ",
                "   "), 
             2:(" o ",
                " | ",
                "   "), 
             3:(" o ",
                "/| ",
                "   "), 
             4:(" o ",
                "/|\\",
                "   "), 
             5:(" o ",
                "/|\\ ",
                "/  "), 
             6:(" o ",
                "/|\\ ",
                "/ \\")}
#print(hangman_art[6])
for line in hangman_art[6]:
    print(line)