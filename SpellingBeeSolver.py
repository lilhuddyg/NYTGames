class SpellingBeeSolver:
    
    def __init__(self):
        self.center = input("Welcome to the Spelling Bee Solver. Please tell us the center letter: ").lower()
        self.outer = set(input("Now tell us the other letters, separated by spaces: ").lower().split(" "))
        letterSet = self.outer.copy()
        letterSet.add(self.center)
        self.wordList = []
        self.wordHashes = {}

        file_path = "C:\\Users\\siden\\Desktop\\Textbooks\\Misc Hacks\\NYT\\words_alpha_len4.txt"
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                setOfWord = set(line)

                # If the center letter is in the word, and the word is a subset of all the letters
                if self.center in setOfWord and setOfWord <= letterSet:
                    self.wordList.append(line)
                    self.wordHashes[line] = setOfWord 

        print(f"Our word list has {len(self.wordList)} words in it.")
    
    # Prints the words in longest to shortest order
    def printLongest(self):
        self.wordList = sorted(self.wordList, key = len, reverse=True)
        
        for word in self.wordList:
            print(word)
        print(len(self.wordList))

solver = SpellingBeeSolver()
solver.printLongest()