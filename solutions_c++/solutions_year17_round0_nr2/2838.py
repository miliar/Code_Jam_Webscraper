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
#include <cassert>

using namespace std;

bool check(int n) {
	string s = to_string(n);
	for (int i = 1; i < s.size(); i++) {
		if (s[i] < s[i - 1]) {
			return false;
		}
	}

	return true;
}

int naive(int n) {
	while (!check(n)) {
		n--;
	}

	return n;
}

string solve(string s) {
	for (int i = 1; i < s.size(); i++) {
		if (s[i] < s[i - 1]) {
			for (i = i - 1; i >= 0; i--) {
				if (s[i] > '1') {
					break;
				}
			}
			if (i >= 0) {
				s[i]--;
				for (i = i + 1; i < s.size(); i++) {
					s[i] = '9';
				}
			}
			else {
				s.pop_back();
				for (auto& e : s) {
					e = '9';
				}
			}
			s = solve(s);
			break;
		}
	}

	return s;
}

int main()
{
	ifstream fin("B-large.in");
	ofstream fout("out.out");
	int testNumber;
	fin >> testNumber;

	for (int test_i = 0; test_i < testNumber; test_i++) {
		string ans, input;

		fin >> input;
		
		ans = solve(input);
		
		fout << "Case #" << test_i + 1 << ": " << ans << endl;
	}

	return 0;
}