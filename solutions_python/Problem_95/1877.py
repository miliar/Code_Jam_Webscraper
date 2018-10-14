>>> def decode(string):
	a = ""
	dictionary = {'a':'y', 'b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q', ' ': ' '}
	for i in range(len(string)):
	    a += dictionary[string[i]]
	return a

>>> def answer():
	a = input()
	b = a.split('\n')
	iterations = int(b[0])
	for i in range(1,iterations+1):
	    print("Case #" + str(i) + ": " + decode(b[i]))

>>> answer()
[Insert input here]
[output will print]