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

 */

int const MaxSize = 1e6 + 10;

LL N, K;
int pr[MaxSize];
int ne[MaxSize];
priority_queue<pair<PII, int> > cand;

void calcNext(int l, int r) {
	int ni = (l + r) / 2;
	int ls = ni - l - 1;
	int rs = r - ni - 1;

	pr[ni] = l;
	ne[ni] = r;

	cand.push(pair<PII, int>(PII(min(ls, rs), max(ls, rs)), -ni));
}
void solve() {
	calcNext(0, N + 1);

	LPE(i, 1, K)
	{
		pair<PII, int> toFill = cand.top();
		cand.pop();
		int ci = -toFill.second;

		if (i == K) {
			cout << toFill.first.second << " " << toFill.first.first << endl;
			return;
		}

		calcNext(pr[ci], ci);
		calcNext(ci, ne[ci]);
	}
}

int main() {

	ios_base::sync_with_stdio(false);
	//freopen("/Users/george/A_1.in", "r", stdin);
	freopen("/Users/george/Downloads/C-small-2-attempt0.in", "r", stdin);
	freopen("/Users/george/Downloads/C_small_2.out", "w", stdout);
	int T;
	cin >> T;
	LPE(cn, 1, T)
	{
		cin >> N >> K;
		cout << "Case #" << cn << ": ";
		memset(pr, -1, sizeof(pr));
		memset(ne, -1, sizeof(ne));
		while (!cand.empty())
			cand.pop();

		solve();
	}

	return 0;
}
