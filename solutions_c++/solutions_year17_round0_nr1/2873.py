#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <fstream>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <tuple>
#include <algorithm>
#include <iterator>
#include <string>
#include <iostream>
#include <fstream>

using namespace std;

bool flip(std::string& s, int pos, int n) {
	if (s.size() - pos < n) {
		return false;
	}
	for (int i = 0; i < n; i++) {
		if (s[pos + i] == '+') {
			s[pos + i] = '-';
		}
		else {
			s[pos + i] = '+';
		}
	}

	return true;
}

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int testNumber;
	fin >> testNumber;
	for (int test_i = 0; test_i < testNumber; test_i++) {
		string s;
		int k;
		fin >> s >> k;
		int n = s.size();

		string ans = "";

		int counter = 0;

		for (int i = 0; i < n; i++) {
			if (s[i] == '-') { 
				if (!flip(s, i, k)) {
					ans = "IMPOSSIBLE";
					break;
				}
				counter++;
			}
		}

		fout << "Case #" << test_i+1 << ": " << (ans != "IMPOSSIBLE" ? to_string(counter) : ans) << endl;
	}

	return 0;
}