"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    # contents = open(file_path).read()
    

    return open(file_path).read()


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    
    # your code goes here
    
    words = text_string.split()
    
    for i in range(len(words) - 2):
        if (words[i], words[i + 1]) not in chains:
            chains[(words[i], words[i + 1])] = []
        chains[(words[i], words[i + 1])].append(words[i + 2])
        # else:
        #     chains[(words[i], words[i + 1])].append(words[i + 2])
        # let’s create a list as the value and append words into it.
    
    return chains


def make_text(chains):
    """Return text from chains."""
    
    # key from our dictionary 
    # and a random word from the list of words that follow it
    # Put in list
    # Join in return
    
# Make a new key out of the second word in the first key and the random word you pulled out from the list of words that followed it.
# Look up that new key in the dictionary, and pull a new random word out of the new list.
# Keep doing that until your program raises a KeyError.
    
    # Pull out random key from dictionary 
    
    #random.choice(varible)
    #chains
    words = []
    

    # for chain in chains:
    # random_chain = choice(chains) #random_chain = key
    random_chain = ('Would', 'you')
    words.append(random_chain[0])
    words.append(random_chain[1])
    while True:   
        random_word = choice(chains[random_chain]) 
        words.append(random_word)
        new_key = (random_chain[1], random_word)
        random_chain = new_key
        if new_key == ("I", "am?"):
            break
      
    
    
        
        
        
    # Select a random word from the value of that key

    # words = []

    # # your code goes here
    # for i in range()

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
