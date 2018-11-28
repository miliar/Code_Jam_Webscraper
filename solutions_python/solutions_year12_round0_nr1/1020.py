import sys

dict = {
	 'a': 'y',
	 'b': 'h',
	 'c': 'e',
	 'd': 's',
	 'e': 'o',
	 'f': 'c',
	 'g': 'v',
	 'h': 'x',
	 'i': 'd',
	 'j': 'u',
	 'k': 'i',
	 'l': 'g',
	 'm': 'l',
	 'n': 'b',
	 'o': 'k',
	 'p': 'r',
	 'q': 'z',
	 'r': 't',
	 's': 'n',
	 't': 'w',
	 'u': 'j',
	 'v': 'p',
	 'w': 'f',
	 'x': 'm',
	 'y': 'a',
	 'z': 'q',
	 'A': 'Y',
	 'B': 'H',
	 'C': 'E',
	 'D': 'S',
	 'E': 'O',
	 'F': 'X',
	 'G': 'V',
	 'H': 'X',
	 'I': 'D',
	 'J': 'U',
	 'K': 'I',
	 'L': 'G',
	 'M': 'L',
	 'N': 'B',
	 'O': 'K',
	 'P': 'R',
	 'Q': 'Z',
	 'R': 'T',
	 'S': 'N',
	 'T': 'W',
	 'U': 'J',
	 'V': 'P',
	 'W': 'F',
	 'X': 'M',
	 'Y': 'A',
	 'Z': 'Q'
}

def translate(word):
 word_list = []
 for letter in list(word):
   if letter.isalpha():
     word_list.append(dict[letter])
   else:
     word_list.append(letter)  
 return ''.join(str(n) for n in word_list)
  
def test_case(t):
 g_words = raw_input().split()
 e_words = []
 for g in g_words:
   e_words.append(translate(g))
 t += 1
 print "Case", "#%d:"%t, 
 for e in e_words:
   print e, 
 print     

def main():
 T = int(raw_input())
 for t in range(0, T):
  test_case(t)

if __name__=="__main__":
 main()