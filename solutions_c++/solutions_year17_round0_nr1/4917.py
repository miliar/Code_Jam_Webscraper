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

int n, k, t;
string s;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	cin >> t;
	for (int ii = 0; ii < t; ii++) {
		cin >> s >> k;
		n = s.length();
		int ans = 0;
		bool was = true;
		for (int i = 0; i < s.length(); i++) {
			if (s[i] == '-' && i <= n - k) {
				ans++;
				for (int j = i; j < i + k; j++) {
					if (s[j] == '-') {
						s[j] = '+';
					}
					else {
						s[j] = '-';
					}
				}
			}
			else if (s[i] == '-') {
				was = false;
			}
		}
		printf("Case #%d: ", ii + 1);
		if (was) {
			cout << ans << endl;
		}
		else {
			cout << "IMPOSSIBLE\n";
		}
	}
	return 0;
}