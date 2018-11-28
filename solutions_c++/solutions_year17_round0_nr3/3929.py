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

#define all(v) v.begin(), v.end()
#define TIME clock() * 1.0 / CLOCKS_PER_SEC

const double EPS = 1e-15;
const double PI = acos(-1.0);
const int MAXN = (int)1023;
const int INF = (int)((ll)(1 << 31) - 1);
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

vector<int> curL, curR;
multiset<int> S;
int solve() {

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n, t, k;
	cin >> t;
	for (int tt = 0; tt < t; tt++) {
		cin >> n >> k;
		S.clear();
		S.insert(-n);
		int Sl, Sr;
		for (int i = 0; i < k - 1; i++) {
			int pp = *S.begin();
			Sl = max(0, -(pp + 1) / 2);
			Sr = max(0, -(pp + 1) - Sl);
			S.erase(S.begin());
			S.insert(-Sl);
			S.insert(-Sr);
		}

		int pp = *S.begin();
		Sl = max(0, -(pp + 1) / 2);
		Sr = max(0, -(pp + 1) - Sl);
		cout << "Case #" << tt + 1 << ": ";
		cout << max(Sl, Sr) << ' ' << min(Sl, Sr) << '\n';
	}
	return 0;
}