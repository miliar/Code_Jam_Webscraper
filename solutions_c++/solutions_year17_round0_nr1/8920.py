#include<iostream>
#include<cstring>
#include<fstream>
using namespace std;

ifstream fin("1A.in");
ofstream fout("1A.out");

string s;
int k = 0;

void flip (string &s, int p) {
	for (int i = 0; i < k; i++) {
		if (s[p + i] == '-') {
			s[p + i] = '+';
		} else {
			s[p + i] = '-';
		}
	}
}

int main () {
	int t;
	fin >> t;
	int count;
	bool psb;
	for (int i = 1; i <= t; i++) {
		psb = true;
		count = 0;
		fin >> s >> k;
		int len = s.length();
		int j;
		for (j = 1; j <= len - k + 1; j++) {
			if (s[j - 1] == '-') {
				count ++;
				flip(s, j - 1);
			}
		}
		for (int b = j - 1; b < len; b++) {
			if (s[b] == '-') {
				psb = false;
			}
		}
		fout << "Case #" << i << ": ";
		if (!psb) {
			fout << "IMPOSSIBLE" << endl;
		} else {
			fout << count << endl;
		}
	}
	return 0;
}
