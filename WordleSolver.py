class WordleSolver:
    def __init__(self):
        self.wordList = []
        self.remainingWords = []
        self.wordHash = {}
        file_path = "C:\\Users\\siden\\Desktop\\Textbooks\\Misc Hacks\\NYT\\valid-wordle-words.txt"
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                self.wordList.append(line)
                self.remainingWords.append(line)
                self.wordHash[line] = set(line)
        print(f"Our Word List has {len(self.remainingWords)} words in it.")

    def play(self):
        print("Welcome to the Wordle solver.")
        print(f"The optimal starting words are SLATE, CRANE, TRACE, CRATE, and CARTE.")
            
        turn = 1
        while turn < 6:
            result = input(f"Please input the results of guess #{turn} as a list: ")
            result = result.lower().split(" ")
            
            self.pareList(result)
            print(self.remainingWords)
            print(f"{len(self.remainingWords)} remain.")
            if len(self.remainingWords) == 1:
                print("You win!")
                return
            
            optimalWord, expectedPartitionSize = self.findOptimalWord()
            print("The optimal word is: "+optimalWord)
            print("The expected partition size with the optimal word is: "+str(expectedPartitionSize))
            
            turn += 1

        print("Sorry! Game failed.")

    def pareList(self, result):
        # Count how many times each letter appears as green or yellow
        confirmedLetters = {}
        
        validLetters = []
        for i, letter in enumerate(result):
            if len(letter) == 2:  # Yellow or green
                validLetters.append([letter[1], letter[0], i])  # y/g, Letter, position
                confirmedLetters[letter[0]] = confirmedLetters.get(letter[0], 0) + 1  # Just the character
            else:  # Grey letter
                validLetters.append(["b", letter, i])
        
        print(validLetters)
        
        afterPare = []
        for word in self.remainingWords:
            stillValid = True
            for validLetter in validLetters:
                color, letter, pos = validLetter
                if color == 'y':  # Yellow
                    if word[pos] == letter or letter not in self.wordHash[word]:
                        stillValid = False
                        break
                elif color == 'g':  # Green
                    if word[pos] != letter:
                        stillValid = False
                        break
                else:  # Grey - only eliminate if letter count exceeds confirmed count
                    confirmedCount = confirmedLetters.get(letter, 0)
                    actualCount = word.count(letter)
                    if actualCount > confirmedCount:
                        stillValid = False
                        break
            
            if stillValid:
                afterPare.append(word)
        
        self.remainingWords = afterPare

    def findOptimalWord(self):
        bestScore = float('inf')
        bestWord = None
        wordToSize = []
        for word in self.wordList: # For all the possible words there are
            patternFreqs = {}
            # Makes the patternFreq dictionary
            for possibleAnswer in self.remainingWords: # For all the possible answers
                pattern = self.getPattern(word, possibleAnswer)
                patternFreqs[pattern] = patternFreqs.get(pattern, 0) + 1
            
            expectedSize = 0 # Expected size of the partitions given this guess
            numRemaining = len(self.remainingWords)
            for pattern in patternFreqs:
                expectedSize += (patternFreqs[pattern]**2 / numRemaining)
                if expectedSize > bestScore:
                    break
            
            if expectedSize < bestScore:
                bestScore = expectedSize
                bestWord = word

        return [bestWord, bestScore]
            
    def getPattern(self, guess, answer):
        toReturn = [None]*5
        answerCounts = {}
        
        for ch in answer:
            answerCounts[ch] = answerCounts.get(ch, 0) + 1

        # Mark the greens
        for i in range(5):
            if guess[i] == answer[i]:
                toReturn[i] = "G"
                answerCounts[guess[i]] -= 1

        # Mark the yellows and greys
        for i in range(5):
            if toReturn[i] == None:
                if guess[i] in answerCounts and answerCounts[guess[i]] > 0:
                    toReturn[i] = "Y"
                    answerCounts[guess[i]] -= 1
                else: # It's not equal or in the word elsewhere, so Grey
                    toReturn[i] = "B" # B for Bad

        return "".join(toReturn)



solver = WordleSolver()
solver.play()