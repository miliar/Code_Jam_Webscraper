#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <string>
#include <cmath>
#include <cstdio>
#include <limits>

using namespace std;

#define REP(i, a, b)		for(i = int(a); i <= int(b); i++)
#define FOR(i, N)			REP(i, 0, N-1)

#define REPI(it, a, b)		for(it = (a); it != (b); it++)
#define FORI(it, v)			REPI(it, All(v))

#define All(v)				v.begin(), v.end()

#define VI					vector<long long>
#define VVI					vector<VI>

#define VD					vector<double>
#define VVD					vector<VD>

#define II					pair<int, int>

const double INF = numeric_limits<double>::infinity();
const double PI = 3.14159265358979323846;
const double EPS = 1e-9;

int main() {
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int t, T;
	cin >> T;
	REP(t, 1, T) {
		int i, j;
		int N, K;
		double U;
		cin >> N >> K;
		cin >> U;

		VD P(N);
		FOR(i, N) cin >> P[i];

		sort(All(P));
		i = 0;

		FOR(i, P.size()) {
			double pNxt = (i == (P.size() - 1)) ? 1.0 : P[i + 1];
			int cnt = i + 1;
			double diff = pNxt - P[i];
			double inc = min(diff * cnt, U) / cnt;
			FOR(j, cnt) {
				P[j] += inc;
				U -= inc;
			}
			if (U < EPS)
				break;
		}

		double ans = 1.0;
		FOR(i, P.size())
			ans *= P[i];

		char Ans[100];
		sprintf(Ans, "Case #%d: %.6f", t, ans);
		cout << Ans << endl;
	}
}