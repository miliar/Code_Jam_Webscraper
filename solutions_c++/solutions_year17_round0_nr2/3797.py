#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:256000000")
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <bitset>
#include <unordered_map>
#include <unordered_set>

using namespace std;

typedef long long ll;

#define forn(i, n) for (int i = 0; i < (int)n; i++)
#define for1(i, n) for (int i = 1; i <= (int)n; i++)
#define forq(i, s, t) for (int i = s; i <= (int)t; i++)
#define ford(i, s, t) for (int i = s; i >= (int)t; i--)
#define all(v) v.begin(), v.end()
#define TIME clock() * 1.0 / CLOCKS_PER_SEC

const double EPS = 1e-15;
const double PI = acos(-1.0);
const int MAXN = (int)1000 + 7;
const int INF = (int)1e9 + 7;
const int MOD = (int)1e9 + 7;
const ll P = 239017;

#define TASK ""

int solve();

int main()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	freopen("test.txt", "w", stderr);
	double tstart = TIME;
#else
	//freopen(TASK".in", "r", stdin), freopen(TASK".out", "w", stdout);
#endif
	solve();
#ifdef _DEBUG
	double tend = TIME;
	cerr << tend - tstart << " s.\n";
#endif
	return 0;
}


int solve() {
	int n;
	cin >> n;
	for (int t = 0; t < n; t++) {
		string s;
		cin >> s;
		int ind = -1;
		for (int i = 0; i + 1 < s.size(); i++) {
			if (s[i] > s[i + 1]) {
				ind = i; break;
			}
		}

		if (ind == -1) {
			cout << "Case #" << t + 1 << ": " << s << '\n';
			continue;
		}
		
		string ans = "";
    	int newind = ind;
		int newc = s[ind] - 1;
		for (int i = ind - 1; i >= 0; i--) {
			if (s[i] <= newc) { break; }
			newind = i;
		}
		if (newind == 0 && s[0] == '1') { ans.assign(s.size() - 1, '9'); }
		else {
			for (int i = 0; i < newind; i++) ans += s[i];
			ans += s[newind] - 1;
			for (int i = newind + 1; i < s.size(); i++) ans += '9';
		}
		cout << "Case #" << t + 1 << ": " << ans << '\n';
	}
	return 0;
}