import sys
import os

sys.setrecursionlimit(200000)

def main():
    s = ''.join(sys.stdin.readlines()).split()
    os.close(0)
    T = int(s[0])
    s = s[1:]
    for i in range(T):
        word = s[0]
        s = s[1:]
        unique = set([])
        for j in word:
            unique.add(j)
        base = len(unique)
        if base == 1:
            base = 2
        digits = "1023456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        used = {}
        newWord = ""
        for j in range(len(word)):
            if used.has_key(word[j]):
                newWord += str(used[word[j]])
            else:
                newWord += str(digits[0])
                used[word[j]] = digits[0]
                digits = digits[1:]
        print "Case #" + str(i+1) + ": " + str(BaseBToNum(newWord, base))

            
def NumToBaseB(N, B):
	''' converts a decimal integer N into a base-B string'''
	if N==0: return ""
	else: return NumToBaseB(N/B,B) + DecToB36Digit(N%B)

def BaseBToNum(S,B):
	''' converts a Base-B string S into a decimal integer'''
	if S == "": return 0
	else: return B * BaseBToNum(S[:-1],B) + B36DigitToDec(S[-1])
	
def BaseToBase(B1, B2, S):
	''' converts a base-B1 string S into a base-B2 string '''
	return NumToBaseB(BaseBToNum(S,B1),B2)

def add(S1, S2):
	''' Adds two binary strings '''
	return NumToBaseB(BaseBToNum(S1,2) + BaseBToNum(S2,2), 2)
	
def DecToB36Digit(N):
	''' converts a decimal digit into a digit of a base up to B36 '''
	if 0 <= N <= 9: return str(N)
	elif 10<=N<=35: return chr(ord('A')+N-10)
	else: return '0'
	
def B36DigitToDec(S):
	''' converts a digit of a base up to B36 into a decimal digit '''
	if "0" <= S <= "9": return int(S)
	elif "A" <= S <= "Z": return ord(S)+10-ord('A')
        elif "a" <= S <= "z": return ord(S)+10-ord('a')
	else: 
            print "error: ",S
            return 0
	    



if __name__ == "__main__":
 	main()

