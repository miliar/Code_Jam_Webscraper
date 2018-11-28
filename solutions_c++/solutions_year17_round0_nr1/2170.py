#define _CRT_SECURE_NO_WARNINGS
#include <iostream> 
#include <vector>
#include <algorithm>
#include <map> 
#include <string>
#include <set> 
#include <iterator> 
#include <deque>
#include <iomanip>
#include <string> 
#include <math.h> 
#include <time.h>
#include <queue> 
#include <stdio.h>
#include <valarray>
#include <stack>

#define mp(x, y) make_pair(x, y)
#define all(x) x.begin(), x.end() 
#define det(a, b, c, d) a*d - b*c

typedef long long ll;

using namespace std;

struct Item {
	int p, q;
	Item(int p = 0, int q = 0):p(p), q(q){}
	bool operator > (const Item & i) const {
		return p*i.q > i.p*q;
	}
	bool operator < (const Item & i) const {
		return p*i.q < i.p*q;
	}
};

int main() {
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		string s;
		cin >> s;
		int k;
		cin >> k;
		int n = s.length();
		int ans = 0;
		for (int j = 0; j <= n - k; j++) {
			if (s[j] == '-') {
				ans++;
				for (int h = 0; h < k; h++) {
					if (s[j + h] == '-') {
						s[j + h] = '+';
					} else{
						s[j + h] = '-';
					}
				}
			}
		}
		bool fl = 0;
		for (int j = n - k; j < n; j++) {
			if (s[j] == '-') {
				fl = 1;
				break;
			}
		}
		if (!fl) {
			cout << "Case #" << i << ": " << ans << endl;
		}
		else {
			cout << "Case #" << i << ": IMPOSSIBLE" << endl;
		}
	}
	return 0;
}
