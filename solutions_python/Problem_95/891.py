#!/usr/bin/python
# -*- coding: utf-8 -*-
 
def decode(ciphertext, key="ynficwlbkuomxsevzpdrjgthaq", 
                  alphabet="abcdefghijklmnopqrstuvwxyz"):
    dic={}  
    for i in range(0,len(key)):  
        dic[key[i]] = alphabet[i]  
  
    plaintext=""  
    for l in ciphertext:  
        if l in dic:  
            l=dic[l]  
        plaintext+=l
  
    return plaintext 

if __name__ == "__main__":
	testcases = input()
	 
	for caseNr in xrange(0, testcases):
		cipher = raw_input()
		print("Case #%i: %s" % (caseNr+1, decode(cipher)))

