// OI.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <map>
using namespace std;

int T;
string s;
int k;

int main() {	
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	fin >> T;
	for (int cse = 1; cse <= T; cse++) {
		fin >> s >> k;
		int ans = 0;
		for (int i = 0; i <= s.size() - k; i++) {
			if (s[i] == '-') {
				for (int j = i; j < i + k; j++) {
					if (s[j] == '-') s[j] = '+';
					else s[j] = '-';
				}
				ans++;
			}
		}
		for (auto c : s) {
			if (c == '-')
				ans = -1;
		}
		fout << "Case #" << cse << ": ";
		if (ans == -1)
			fout << "IMPOSSIBLE" << endl;
		else
			fout << ans << endl;
	}
	return 0;
}

