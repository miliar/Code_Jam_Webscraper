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
int D, N, K[MaxSize], S[MaxSize];

bool good(double speed) {

	LP(i, 0, N)
	{
		if (speed <= S[i])
			continue;

		double dt = (double) (D - K[i]) / (double) S[i];
		double dv = speed - (double) S[i];

		if (dv * dt > K[i])
			return false;
	}

	return true;
}

double maxSpeed(double l, double h) {
	if (h - l <= Ep)
		return h;

	double mid = (l + h) / 2.0;

	if (good(mid)) {
		if (good(mid + Ep))
			return maxSpeed(mid + Ep, h);
		else
			return mid;
	} else {
		return maxSpeed(l, mid - Ep);
	}

	return 0;
}

int main() {

	ios_base::sync_with_stdio(false);
	//freopen("/Users/george/A_1.in", "r", stdin);
	freopen("/Users/george/Downloads/A-large.in", "r", stdin);
	freopen("/Users/george/Downloads/A_large.out", "w", stdout);
	int T;

	cout << setprecision(10) << fixed;
	cin >> T;
	LPE(cn, 1, T)
	{
		cout << "Case #" << cn << ": ";
		cin >> D >> N;

		int maxS = 0;
		double minS = 1e13;
		LP(i, 0, N)
		{
			cin >> K[i] >> S[i];
			double dt = (double) (D - K[i]) / (double) S[i];
			double dS = (double) K[i] / dt;
			double cs = dS + (double) S[i];

			maxS = max(maxS, S[i]);
			minS = min(minS, cs);
		}

		//cout << D << " " << N << endl;
		cout << minS << endl;

		//cout << maxSpeed(minS, 1e13) << endl;
	}

	return 0;
}
