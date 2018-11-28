#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <tuple>
#include <algorithm>
#include <set>
#include <functional>
using namespace std;

#define sz(a) ((int)((a).size()))
#define fi(a,b) for(int i = (a); i < (b); ++i)
#define fj(a,b) for(int j = (a); j < (b); ++j)
#define all(a) (a).begin(), (a).end()
typedef long long ll;

bool check(string & s) {
	return (s.find('-') == string::npos);
}

char getRev(char f) {
	return ((f == '-') ? '+' : '-');
}

void flip(string &s, int k) {
	for(int i = 0; i < sz(s) - k + 1; ++i) {
		if(s[i] == '-') {
			fj(0, k) {
				s[i + j] = getRev(s[i + j]);
			}
			return;
		}
	}
}

void solve() {
	string s;
	int k;
	cin >> s;
	cin >> k;
	int ans = 0;
	while(!check(s)) {
		flip(s, k);
		++ans;
		if(ans > sz(s)) {
			break;
		}
	}
	if(ans > sz(s)) {
		cout << "IMPOSSIBLE";
		return;
	}
	cout << ans;
}

int main() {
#ifdef MY_DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output1.txt", "w", stdout);
#endif
	int nT;
	cin >> nT;
	fi(0, nT) {
		cout << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
	}
	return 0;
}