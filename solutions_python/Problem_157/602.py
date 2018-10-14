import os
import random
import time

def read_input():
	file_name = "%s/small.in" % os.getcwd()
	return open(file_name, "r")

def multiply(last, c):
	n1, n2 = to_number[last], to_number[c]
	abs_n1, abs_n2 = abs(n1), abs(n2)
	ans = matrix[abs_n1-1][abs_n2-1]
	if (n1 > 0 and n2 < 0) or (n1 < 0 and n2 > 0):
		ans = -ans
	return to_symbol[ans]

def find_let(string, let, start):
	ans = []
	last = ""
	for index in range(start, len(string)):
		c = string[index]
		if len(last) > 0: last = multiply(last, c)
		else: last = c
		if last == let: ans.append(index)
	return ans

def find_is(string):
	return find_let(string, "i", 0)

def find_js(string, start):
	return find_let(string, "j", start)

def find_ks(string):
	ans = {}
	last = ""
	for index in range(len(string)-1, -1, -1):
		c = string[index]
		if len(last) > 0: last = multiply(c, last)
		else: last = c
		if last == "k": ans[index] = True
	return ans

def get_ans(string, num):
	i_s = find_is(string)
	k_s = find_ks(string)

	for i_pos in i_s:
		j_s = find_js(string, i_pos+1)
		for j_pos in j_s:
			if j_pos+1 in k_s:
				return "Case #%d: YES" % num

	return "Case #%d: NO" % num

def make_output(ans):
	file_name = "%s/small.out" % os.getcwd()
	f = open(file_name, "w")
	f.write(ans)
	f.close()

def main():
	ans = ""
	f = read_input()
	
	T = int(f.readline())
	for i in range(T):
		print i
		L, X = (int(x) for x in f.readline().split())
		string = X * f.readline().split()[0]
		ans += get_ans(string, i+1)
		if i < T-1: ans += "\n"

	f.close()
	make_output(ans)

to_symbol = {
	 1:  "1",  2:  "i",  3:  "j",  4:  "k",
	-1: "-1", -2: "-i", -3: "-j", -4: "-k"
}

to_number = {
	 "1":  1,  "i":  2,  "j":  3,  "k":  4,
	"-1": -1, "-i": -2, "-j": -3, "-k": -4
}

matrix = [
	[1,  2,  3,  4],
	[2, -1,  4, -3],
	[3, -4, -1,  2],
	[4,  3, -2, -1]
]

start_time = time.time()

main()

# L, X = 2, 1
# string = X * "ik"
# print get_ans(string, 1)
# L, X = 3, 1
# string = X * "ijk"
# print get_ans(string, 2)
# L, X = 3, 1
# string = X * "kji"
# print get_ans(string, 3)
# L, X = 2, 6
# string = X * "ji"
# print get_ans(string, 4)
# L, X = 1, 10000
# string = X * "i"
# print get_ans(string, 5)

# L, X = 5046, 1
# string = X * "kkijkjjjjkijkkkjjjjkikijijjkjkkkjjikijiikkjjijkijkjikjjkjkjijijkkijkkiijijkkijjjjjjjkijjkikikkikkiiijkjkiijjjjiijiijikkijkkjikkjiikiijiiikikijikiiikkjkkijjjjjiikkijjkkkkkkijkjkkjkkjjjkijkikjkiijkijjijjijjjijikjikikikjjiikjijjiiikijijiikikijkijkjjjkjjjkikiijkiikikkjjiiikkjkjjikkjikjjiikijiiijikjijkijjikiiijijiijjjiiijjjikkikjkkjkijikjjjjjkkikjiijijiikjjjijkjkkkjkjkkikijijkijkkiiijkkijjjkkiikjjjikijiiikijkjikjikijkkijjiikijikkikkiijikikjkijkjkiiiijjjjkkjiiikjikiikkikiijkijikijjjjjjjikkijjiijkjjikjiijjkkkikkikjijijjijkiikjjkijijkkiiijjikjjkkkkkikkikkikikkkikijjjiijijkkkkjkikiijkkjjjiijijjkjjkjijkkiikjikjjjjiiiijijkiikjijkijkkkkjjjkkiiijkjjkjkkkjjkjjjkijijjjkkjikkkjkijiiiiiikjkjikiiikkjjkjkikjjkjjkijjkkjikkkjkkkjijkkjkkjkiijjijiiiikkjiikjikijiiijkkjkikijjkkkijjjjjikjjjkijiiijjjijjkiikjjikkkkjikjkiiiiiikjiijkkjjjkjkkjjiikjikkkiikkikjijikjkijijjkjjjkijijjjkiijikkiikijkkkkjjjiiikiikikjkjjjjijkjijikjikkkiiiijiikiikkiikkikiikijikjikikiijikjjjijiiikikkkijkijjjiikkkkjkjikijkikiijjkikkjkikikiijkkkkikijkikkiikikjjiijiijkijkkikiijijkikiikjiikkijkijjkiiikjiijijijkjjjjjjjiikijikkkkkiiikiiijiijjkiikjjkikjjkjjijikkijkjijkjjjjijikkikijijikjikkjikikkijijjiikjjijikjkijkiijijkkkjikjjjjkjkjiikjikkijkkjikjijijijjkikkjkjkkiikkijkiikijiiijkjjijkjjkjikjikikjkijkjkkjijjiikkjjjkijjkjjikjjkkkjkikiijikjikijiiiikkjjikikiiijjkkkikikkkiijijikjjjjkijikjijijkiijiijijkjjiiiikjjikjiikiiiikikjjijkkkikkikijjkjjjjjjjkkjjjjijjijkjjkkiikkiikjiiikiijkjiiikjikjiikkkikkkkjjjjikijiijjkjjjkkiiikjkjjiiikjiiiijjkjjjijkkkkjjkikikkikkkkijjjkjiiijkiikjiijjjikjjjjkjikkkjjikjkikkikikkjkjkjikikjjijkkiikkkkkkjkkkijikjkkjkkjkjjikjkkjijijkikjijikjkikjjkiijjikjkiiikijijjjiiikjikjikjkkjikijikkijjjkiiijjijkjkjikjkjjjikjkkjjjkjikijjikijjjkkjijkikjikiikjiijjjjiikjijjiiijkkjkkjikkjjjijijikkjijijiiikkkjijikiijjiijijiijkkkjkkjiikikjkiijjjkiikjjikkiiijikkjjkkkkikjjijkjjijijkjjkikijiiiikjijijkjkkikjkijjiijkkjjjiijjkiijjkiiiiikjjkjjiijjkkkkjjjjkkiijkkikjjkkkikjkjjikiiijijijjiiiiiikjkjijkkjkkikkiiiikjjikijkjjiiikijkkjjjjjkijkikiikikikjijjjkijkkkijikiiijikkkkjikikkkkikkjjiiiijkikjjkjkiiiiijiiiijkjkjkkikkkijjjiiikjjkikkjkijjjkiiiijiijjjijiikkkjkkkjkiikikjkkjijkjkiikjjkiiiiijikikkjiiikikkkiiijiikjikkjjjkjikkjiiikjjiikijkijkjkkjikikkkkijjjjkkkkjjijiiikjkjkkiikijjkiiikjjkkkkjjkjkikkkikkikjkjkjjiikjjkijjkijjjkjkkjkjjjikikjijkiiikiijjjkjjjiiiijkijiijjjkkkjjjijjiijkiiiikikiijkkikjkjjjijkkjjkkiiikjijijkkjkiikjkkiijjkiikijiiikikjkkkjjikjkjjkjjjkkijiijikikjjjikjikiijjkkkjkkkkikjkikjjijjkiijijkkijkkikkjkikjikiikkiijiiikjjkkkiijjkkkkikijkjkjkkikkikjkkijkkiiijjijjiikiikjiijkjkkkikiijkiijjjjikjjkkkjjkjjiijijikkkjkjikikiiiiikkikjjkkjjikkkiijjijkkjkjkkiiiikkiijjjiijikkkjkiijjikikiijkjiikjjkiijjjiiiijjkijijkkikiikjjkikijijjkjjjjikjikikikkkjiijijikjkjjjjiiiikjjkkjikikikikkijkiikjikiiijijjkiikkijjijkiikijkkijikjkiijjkkjiijkiikijkkjiijjiiijiikikkjijiikjiiijkijkkjkiijjijjkikijkkjikkjkiijjkkjjijijiiiikkkkiikjkjkkjikkjkkkkkjkkkikikikiijijkikkijjkkjkkkikkijkjjjiiijiijkjkjjkikikkjjijkjjjkijkjjkkijjjkiiiijkkjijiijikjjijjjkkiijkijkkkkijkikjiijikjjikjkiiiiiijkkjjiikikijjjijkjiiiiikijjkjiiiiijjjijkijjijjiiiiiikjiiikjikjkkjjjjkjkkijkjkjiiikijikkijjkkijkijiikjijjkkkkjkijkiijjjjkkkikkkkkijjkkkjkiiijjkkikikkijijjkikijkkjkijjijiijiikijkijkkiijijkjikjkijjkijkikkkkiiikjjkikjjkjkkkiiijiijikijjjikiijjijkiijkjijkiikjkijjkkiikkiikiiijjjkiikkiijjikijikijijjijkijjiiijkkkjjiikjiijkkkjkkikikikkkjkiikijkjkkiijjjjkjijikjkkijjkijkjjjikjjjiiikjjikjjikjiikkiijkkijjijiiikiiikkjjiijjjijjkikjkjjkjijkkkjjijijikijijjkkijijkjikjkjijikkkjikkiiikiiiijkijjikikkjjjkikjijijkkiikkkijijjjjkkkikikkijjjkkkjjijkikjkjjijjkikkiikkjjjiijkkkkkkijikkijkijjikkiiikkkikkikikikkikkijkkkjkkikiikjjijkjkkkkjkkjikjkjjkiiikkikjikkikjikikikikijjkjkkijiijkikkjkkiiiikijjkijikkkkjijjijkjikkkjkijjjiikikjikkjkkkjiijiiiikjjjijkijijjjjjjjkiiijkiiikkkkjkjjkikkjkijikkjijjjjjkkjikijkjiijiikjkikkjkikjjkkjjijjkkijikiijkkjjkkjjkjjiijjjjiikkikjjikiikjjikkkkikkkkkjkjikkjkikkjkjijijijkjkjiikkkikikkiijjjijjikjjkjikjjiikkikjjjjkikjkjjjjiiijjkikkikjikjjjikjikiikkjjijjkjijkijkjjijjkjjikjjiijkkjijikjjiijkkiijiikjiijiiijkkjkjkkkkjiiikjkjijjkkjkkikjijkkkkjjiikkiijkijijjjikjjikiikjjikjiijiiijkjjjkjikiikkjkjiikiijjijkjjkkjjkjjkikkjiijjijkijkkikiikikkkkjkjjikkikiiikjijjjjjkkiikikkjkijkjjjkiikikkijjjijkkikkjjkikikkjkkjkkkkjkikkikikjjiikjkjijiikijkkiijjkkikikiijjiijkkikijjikjikkkikjjjikkjkkjjiiikiiijjijiiiikjkkiiikjjjjkjkijkijijkikjikiiikjikkjjjjkkikjjikkjijijkkjkijkiiikijjjijkjkkjjjjkjjijjijkjijjkjikikijkijjjkjkikjjkkkiijjjijiijiikikkjjkkjijjikjjkjjjjkkkjjkikjkkjjijiiiikkkjkjikjjijijkikjkiiijijijjjkkkjjjjikikkikjkjkkkiiijjijkkiiijkkkjjiikjjkkikjiiijkiijkijiiiikjjkjkjkkkkkikkjjjikjikjkijijikiiiikkijjkiijiijjikikkjiiikijjiijjijjkkkjkkiijjjijkkkkkkikiiijiiiijjiijkjjjjiikjkjjijikikikkkjkikkkiikkiijijjjkkjjijkjijkkijiikkjikkkikjikjjiiiikiikjikkkjikkkjjiijkiikiiikikkijkjkkijiijjjkjjiijikkiikkjikjkjkkijkjkiiiikkkikkiiiikikiijkikikjkjjjkjjjkkkjikjkkiikijjkikiikijjkjkjkkikjjjkijikkjiikkjjjkkikjijjiijkijkijikkijiijjiikkkkkikikjjijkkikiikkjkkkkkjkijjiiiikijjijkikkkiikjkjkjiikjjijkkijjjkjikijiijikkjkjjjikikkkjkikkjjjjijikiiikkkiikjjjikijjkkkjikjjjjiijjkjkkijkiikjiikiijkjjkkijjkjjkiikjkikiiikikjijkjijjjiijjijjkijijkijkkkkjjkikiijikiikjjkk"
# print get_ans(string, 6)

print("--- %s seconds ---" % (time.time() - start_time))




