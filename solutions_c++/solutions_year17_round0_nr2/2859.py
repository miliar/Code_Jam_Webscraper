#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <ctime>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>
#include <vector>
#include <cassert>
#include <iostream>

using namespace std;

const double eps = 1e-9;
const int inf = 1e9 + 23;

const int size = 1000;

const int N = 4;


int main (void){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int n;

	int t;
	cin >> t;
	for (int it = 0; it < t; it++) {
		cout << "Case #" << it + 1 << ": ";
		int n;
		string s;
		cin >> s;
		n = s.length();
		int k = 0;
		if (n == 1) {
			cout << s << endl;
			continue;
		}
		while (k < n - 1) {
			if (s[k] <= s[k + 1])
				k++;
			else break;
		}
		if (k == n - 1) {
			cout << s << endl;
			continue;
		}
		int l = k;
		while (l > 0) {
			if (s[l] == s[l - 1])
				l--;
			else break;
		}
		for (int i = 0; i < l; i++) {
			cout << s[i];
		}
		if (s[l] == '1') {
			assert(l == 0);
			for (int i = 0; i < n - 1; i++) {
				cout << 9;
			}
			cout << endl;
			continue;
		} else {
			cout << (s[l] - '0') - 1;
			for (int i = l + 1; i < n; i++) {
				cout << 9;
			}
			cout << endl;
			continue;
		}
	}

	return 0;
}