#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;

string lastTidyNumber(int* b, int size) {
	for(int i = size-1; i > 0; i--)
		if(b[i-1] > b[i]) {
			b[i-1]--;
			int j = i;
			while(j < size)
				b[j++] = 9;
		}

	ostringstream s;
	int first = 0;
	while(b[first] == 0)
		first++;
	for(int i = first; i < size; i++)
		s << b[i];
	return s.str();
}

int main() {
	ifstream fin;
	fin.open("B-large.in");
//	fin.open("B-small-attempt0.in");
//	fin.open("B-small-practice.in");
//	fin.open("B-large-practice.in");
	
	ofstream fout;
	fout.open("B-large.out");
//	fout.open("B-small-attempt0.out");
//	fout.open("B-small-practice.out");
//	fout.open("B-large-practice.out");

	int t;
	fin >> t;
	for (int i = 1; i <= t; ++i) {
		string s;
		fin >> s;

		int size = s.size();
		while(size > 0 && s[size-1] == '+')
			size--;
		int b[size];
		for(int j = 0; j < size; j++)
			b[j] = (int)s[j] - (int)'0';
		fout << "Case #" << i << ": " << lastTidyNumber(b, size) << endl;
	}
	fin.close();
	fout.close();
	return 0;
}

