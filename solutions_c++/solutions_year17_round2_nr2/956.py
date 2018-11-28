#include <iostream>
#include <sstream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <iomanip>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <bitset>
#include <assert.h>
#include <deque>
using namespace std;

typedef unsigned long long UL;
typedef long long LL;
#define LP(i, a, b) for (int i = int(a); i < int(b); i++)
#define LPE(i, a, b) for (int i = int(a); i <= int(b); i++)
typedef pair<int, int> PII;
typedef vector<vector<PII> > WAL;
typedef vector<vector<int> > SAL;
#define Ep 1e-7

#define INF 1e16

/*
 while (ans.size() < bl + re + ye) {
 sort(nc, nc + 3);

 char maxC = nc[2].second;

 if (maxC == prevC) {

 char sC = nc[1].second;
 ans.push_back(sC);
 prevC = sC;

 int sCN = nc[1].first - 1;
 nc[1] = pair<int, char>(sCN, sC);

 } else {
 ans.push_back(maxC);
 prevC = maxC;

 int maxCN = nc[2].first - 1;
 nc[2] = pair<int, char>(maxCN, maxC);
 }
 }
 */
int N, R, O, Y, G, B, V;

void pr(char fc, char sc, int c) {
	LP(i, 0, c)
	{
		cout << fc << sc;
	}
}

void solve(int bl, int re, int ye) {
	char prevC = '?';

	vector<char> ans;

	pair<int, char> nc[3];

	nc[0] = pair<int, char>(bl, 'B');
	nc[1] = pair<int, char>(re, 'R');
	nc[2] = pair<int, char>(ye, 'Y');

	sort(nc, nc + 3);

	if (nc[0].first + nc[1].first < nc[2].first) {
		cout << "IMPOSSIBLE" << endl;
		return;
	}

	while (nc[0].first + nc[1].first > nc[2].first) {
		ans.push_back(nc[2].second);
		nc[2].first -= 1;
		ans.push_back(nc[1].second);
		nc[1].first -= 1;
		ans.push_back(nc[0].second);
		nc[0].first -= 1;
	}

	while (nc[1].first) {
		ans.push_back(nc[2].second);
		nc[2].first -= 1;
		ans.push_back(nc[1].second);
		nc[1].first -= 1;
	}

	while (nc[0].first) {
		ans.push_back(nc[2].second);
		nc[2].first -= 1;
		ans.push_back(nc[0].second);
		nc[0].first -= 1;
	}

	int bsf = 0, rsf = 0, ysf = 0;

	LP(i, 0, ans.size())
	{
		cout << ans[i];
		if ('B' == ans[i]) {
			bsf++;
			if (bsf == bl) {
				pr('O', 'B', O);
			}
		} else if ('R' == ans[i]) {
			rsf++;
			if (rsf == re)
				pr('G', 'R', G);
		} else {
			ysf++;
			if (ysf == ye)
				pr('V', 'Y', V);
		}
	}
	cout << endl;
}

int main() {

	ios_base::sync_with_stdio(false);
	//freopen("/Users/george/A_1.in", "r", stdin);
	freopen("/Users/george/Downloads/B-large.in", "r", stdin);
	freopen("/Users/george/Downloads/B_large.out", "w", stdout);
	int T;
	cin >> T;

	LPE(cn, 1, T)
	{
		cout << "Case #" << cn << ": ";
		cin >> N >> R >> O >> Y >> G >> B >> V;
		if (O > B || G > R || V > Y) {
			cout << "IMPOSSIBLE" << endl;

		} else if (O && O == B) {
			if (O + B == N) {
				pr('O', 'B', O);
				cout << endl;
			} else {
				cout << "IMPOSSIBLE" << endl;
			}
		} else if (G && G == R) {
			if (G + R == N) {
				pr('G', 'R', G);
				cout << endl;
			} else {
				cout << "IMPOSSIBLE" << endl;
			}
		} else if (V && V == Y) {
			if (V + Y == N) {
				pr('V', 'Y', V);
				cout << endl;
			} else {
				cout << "IMPOSSIBLE" << endl;
			}
		} else {
			//cout << B-O << " " << R - G << " " << Y - V << endl;
			solve(B - O, R - G, Y - V);
		}
	}

	return 0;
}
