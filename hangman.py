import random
from words import word_list
def get_word():
    word= random.choice(word_list)
    return word.upper()

# creating variables that will keep updating after each turn by the player
def play(word):
    word_progress= "_" * len(word)
    #will show initial status of the word(unguessed letters are represented by _)
    guessed= False
    guessed_letters= []
    guessed_words= []
    tries= 6
    print("Let's play the hangman game!!")
    print(hangman(tries))
    print(word_progress)
    #displaying initial states of the hangman and the unguessed word
    print("\n")
    while not guessed and tries>0:
        guess= input("Please guess a letter or a word: ").upper()
        if len(guess)==1 and guess.isalpha():
            if guess in guessed_letters:
                print("You have already guessed",guess)
                print(word_progress)
            elif guess not in word:
                print("oops",guess,"is not in the word :(")
                tries-= 1
                guessed_letters.append(guess)
                print(word_progress)
                print(hangman(tries))
            else:
                print("Congratulations! You guessed the right letter")
                guessed_letters.append(guess)
                #now showing all the positions of the guessed letter in the word
                word_aslist= list(word_progress)
                #to index it freely
                indices= [i for i, letter in enumerate(word) if letter==guess]
                for index in indices:
                    word_aslist[index]= guess
                    word_progress= "".join(word_aslist)
                    if "_" not in word_progress:
                        guessed= True   
                print(word_progress)
        elif len(guess)== len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You've already guessed the word :/",guess)
            elif guess !=word:
                print("Bummer.", guess, "is not the word :(")
                tries -=1
                guessed_words.append(guess)
                print(hangman(tries))
            else:
                guessed= True
                word_progress= word
              
        else:
            print("Not a valid guess :/")
            print(hangman(tries))
            print(word_progress)
            print("\n")
    if guessed:
        print("Hurray!! You correctly guessed the word, YOU WIN :)")
    else:
        print("OOPS! Sorry, you ran out of tries :(, the word was "+word)

def hangman(tries):
    stages= [ """
                 ---------
                 |    |
                 |    0
                 |  \   /
                 |    |
                 |   / \
             """,
              """
                 ---------
                 |    |
                 |    0
                 |  \   /
                 |    |
                 |   / 
             """,
              """
                 ---------
                 |    |
                 |    0
                 |  \   /
                 |    |
                 |    
             """,
              """
                 ---------
                 |    |
                 |    0
                 |  \   /
                 |    
                 |   
             """,
              """
                 ---------
                 |    |
                 |    0
                 |  \   
                 |    
                 |    
             """,
              """
                 ---------
                 |    |
                 |    0
                 |    
                 |    
                 |    
             """,
              """
                 ---------
                 |    |
                 |    
                 |    
                 |    
                 |    
             """
        ]
    return stages[tries]


def main():
    word= get_word()
    play(word)
    while input("Play again? (Y/N) ").upper()== "Y":
        word= get_word()
        play(word)

if __name__ == '__main__':
    main()
