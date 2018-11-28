#include <iostream>
#include <fstream>
using namespace std;

int minFlip(bool* b, int size, int k) {
	if(size == 0)
		return 0;
	if(size < k)
		return -10000;

	if(size == k)
	{
		bool allPlus = true, allMinus = true;
		for(int i = 0; i < size && (allMinus || allPlus); i++) {
			if(b[i])
				allMinus = false;
			else
				allPlus = false;
		}
		if(allPlus)
			return 0;
		if(allMinus)
			return 1;
		return -1000;
	}

	for(int i = 1; i <= k; i++)
		b[size-i] = !b[size-i];
	while(b[size-1])
		size--;
	
	return 1 + minFlip(b, size, k);
}

int main() {
	ifstream fin;
	fin.open("A-large.in");
//	fin.open("A-small-attempt0.in");
//	fin.open("A-small-practice.in");
//	fin.open("A-large-practice.in");
	
	ofstream fout;
	fout.open("A-large.out");
//	fout.open("A-small-attempt0.out");
//	fout.open("A-small-practice.out");
//	fout.open("A-large-practice.out");

	int t;
	fin >> t;
	for (int i = 1; i <= t; ++i) {
		string s;
		fin >> s;

		int k;
		fin >> k;

		int size = s.size();
		while(size > 0 && s[size-1] == '+')
			size--;
		bool b[size];
		for(int j = 0; j < size; j++)
			b[j] = (s[j] == '+') ? 1 : 0;
		int flip = minFlip(b, size, k);
		if(flip < 0)
			fout << "Case #" << i << ": IMPOSSIBLE" << endl;
		else
			fout << "Case #" << i << ": " << flip << endl;
	}
	fin.close();
	fout.close();
	return 0;
}

