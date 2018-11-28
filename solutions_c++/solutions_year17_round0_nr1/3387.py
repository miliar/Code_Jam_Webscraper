#include <iostream>
#include <fstream>
#include <cstring>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

int n;
int a[1111];

int process(string str, int k) {
	n = str.length();
	for (int i = 0; i < n; ++i) {
		if (str[i] == '+') {
			a[i] = 1;
		} else {
			a[i] = 0;
		}
	}
	int res = 0;
	for (int i = 0; i < n; ++i) {
		if (a[i] == 0) {
			if (i + k - 1 < n) {
				++res;
				for (int j = i; j <= i + k - 1; ++j) {
					a[j] = (a[j] + 1) % 2;
				}
			}
		}
	}
	for (int i = 0; i < n; ++i) {
		if (a[i] == 0) {
			return -1;
		}
	}
	return res;
}

int main(int argc, char **argv) {
	string line;
	getline(cin, line);
	int nTests = atoi(line.c_str());
	for (int test = 1; test <= nTests; ++test) {
		getline(cin, line);
		string str1 = "";
		int j;
		for (int i = 0; i < line.size(); ++i) {
			if (line[i] == ' ') {
				j = i;
				break;
			}
			str1 += line[i];
		}
		string str2 = "";
		for (int i = j + 1; i < line.size(); ++i) {
			str2 += line[i];
		}
		int k = atoi(str2.c_str());
		int res = process(str1, k);
		if (res == -1) {
			cout << "Case #" << test << ": IMPOSSIBLE" << endl;
		} else {
			cout << "Case #" << test << ": " << res << endl;
		}
	}
	return 0;
}