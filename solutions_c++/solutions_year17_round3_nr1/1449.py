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

int const MaxSize = 1000 + 10;
LL R[MaxSize], H[MaxSize], N, K;

long double solve(int bi) {
	LL bSur = R[bi] * R[bi];
	LL bSide = 2 * R[bi] * H[bi];

	vector<LL> hs;

	LP(i, 0, N)
	{
		if (i != bi) {
			LL oSide = 2 * R[i] * H[i];
			hs.push_back(-oSide);
		}
	}

	sort(hs.begin(), hs.end());

	LL total = 0;
	LP(i, 0, K - 1)
	{
		//cout << hs[i] << " ";
		total -= hs[i];
	}
	//cout << endl;

	total += bSur;
	total += bSide;

	//cout << bi << " " << total << endl;

	return (long double) 3.1415926 * (long double) total;
}

int main() {

	ios_base::sync_with_stdio(false);
	//freopen("/Users/george/A_1.in", "r", stdin);
	freopen("/Users/george/Downloads/A-large.in", "r", stdin);
	freopen("/Users/george/Downloads/A_large.out", "w", stdout);
	int T;
	cin >> T;

	LPE(cn, 1, T)
	{
		cout << "Case #" << cn << ": ";
		cin >> N >> K;
		LP(i, 0, N)
		{
			cin >> R[i] >> H[i];
		}

		long double ans = 0;
		LP(bi, 0, N)
		{
			long double curAns = solve(bi);
			ans = max(ans, curAns);
		}

		cout << setprecision(10) << fixed;
		cout << ans << endl;
	}

	return 0;
}
