/*AMETHYSTS*/
#pragma comment(linker, "/STACK:1000000000")
#include <cstdio>
#include <iostream>
#include <ctime>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <set>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <bitset>
#include <deque>
#include <stack>
#include <climits>
#include <string>
#include <queue>
#include <memory.h>
#include <map>            
#define ll long long
#define ld double
#define mp make_pair

using namespace std;

const double PI = 3.14159265358979323846;
const int maxn = (int)101;
const ll mod = (ll)1e9 + 7;
const ll inf = (ll)1e18 + 7;
const double eps = 1e-6;

int n, k, t, was[100][10];
string s;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	cin >> t;
	for (int ii = 0; ii < t; ii++) {
		cin >> s;
		printf("Case #%d: ", ii + 1);
		if (s.length() == 1) {
			cout << s << endl;
			continue;
		}
		memset(was, 0, sizeof was);
		for (int i = s.length() - 1; i >= 0; i--) {
			for (int j = 0; j <= 9; j++) {
				was[i][j] = was[i + 1][j];
			}
			for (int j = s[i] - '0' + 1; j <= 9; j++) {
				was[i][j] = 1;
			}
		}
		string tans = "";
		for (int i = 0; i < s.length() - 1; i++) {
			tans += '9';
		}
		string tmp = "";
		for (int i = 0; i < s.length(); i++) {
			if (i != 0 && s[i] - '0' < s[i - 1] - '0') {
				break;
			}
			if (i == s.length() - 1) {
				tmp = s;
				break;
			}
			if (was[i + 1][s[i + 1] - '0']) {
				if (s[i + 1] == '0') {
					break;
				}
				if (s[i] <= s[i + 1] - 1) {
					tmp = s;
					tmp[i + 1]--;
					for (int j = i + 2; j < tmp.length(); j++) {
						tmp[j] = '9';
					}
					break;
				}
				else {
					break;
				}
			}
		}
		if (tmp == "") {
			if (s[0] != '1') {
				s[0]--;
				for (int i = 1; i < s.length(); i++) {
					s[i] = '9';
				}
				cout << s << endl;
			}
			else {
				cout << tans << endl;
			}
		}
		else {
			cout << tmp << endl;
		}
	}
	return 0;
}