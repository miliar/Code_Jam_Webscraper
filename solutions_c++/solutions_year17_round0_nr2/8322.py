#include <iostream>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>

using namespace std;

unsigned t;
string n;

bool isTidy(string s) {
	for (unsigned i = 1; i < s.size(); i++) 
		if (s[i] < s[i - 1]) 
			return false;
	return true;
}

void nine(int p) {
	for (unsigned i = p; i < n.size(); i++) {
		n[i] = '9';
	}
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	cin >> t;
	for (unsigned cas = 1; cas <= t; cas++) {
		cin >> n;
		unsigned p = 1;
		for (; p < n.size(); p++) {
			if (n[p - 1] > n[p]) {
				break;
			}
		}
		if (p != n.size()) {
			nine(p);
			for (p--; p > 0; p--) {
				n[p]--;
				if (n[p - 1] <= n[p]) {
					break;
				}
				nine(p);
			}
			if (p == 0) {
				nine(p + 1);
				n[p]--;
			}
			if (n[0] == '0') {
				n = n.substr(1);
			}
		}
		cout << "Case #" << cas << ": " << n << endl;
	}
	return 0;
}