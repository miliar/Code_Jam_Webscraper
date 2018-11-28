#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <fstream>
#include <algorithm>

using namespace std;

typedef long long LL;
typedef vector<LL> VLL;
typedef vector< VLL > matrix;

string str;
VLL parse;

bool isOk(string&);

int main() {
	LL T;

	FILE* fr;
	FILE* fo;
	ifstream fin;
	ofstream fout;

	fin.open("B-small-attempt3.in");
	fout.open("output3.txt");

	fin >> T;

	for (LL cnt = 1; cnt <= T; cnt++) {
		str.clear();
		fout << "Case #" << cnt << ": ";
		fin >> str;
		LL num = stoi(str);
		
		while (!isOk(str)) {
			char buffer[333] = { 0, };
			num = stoi(str);
			num--;
			str = itoa(num,buffer,10);
		}
		fout << num << endl;


	}
	return 0;
}

bool isOk(string& str) {
	for (int i = 0; i < str.size() - 1; i++) {
		if (str[i]>str[i + 1]) {
			return false;
		}
	}
	return true;
}