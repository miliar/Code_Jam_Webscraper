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

#define DD					pair<double, double>
#define RR					first
#define HH					second
#define VDD					vector<DD>

const double INF = numeric_limits<double>::infinity();
const double PI = 3.14159265358979323846;

int N, K;
VDD V;
VVD dp;

double cal(int cur, int k) {
	if (cur == N) return 0;
	if (k == 0) return 0;
	if (N - cur < k) return 0;
	if (dp[cur][k] > -0.5) return dp[cur][k];

	double val1 = 0;
	if (k == K) val1 += PI * V[cur].RR * V[cur].RR;
	val1 += (2 * PI * V[cur].RR * V[cur].HH) + cal(cur + 1, k - 1);

	double val2 = 0;
	val2 += cal(cur + 1, k);

	return dp[cur][k] = max(val1, val2);
}

int main() {
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int t, T;
	cin >> T;
	REP(t, 1, T) {
		int i;
		cin >> N >> K;

		V = VDD(N);
		FOR(i, N) cin >> V[i].RR >> V[i].HH;
		sort(All(V));
		reverse(All(V));

		dp = VVD(N, VD(K + 1, -1));
		char ans[100];
		sprintf(ans, "Case #%d: %.6f", t, cal(0, K));
		cout << ans << endl;
	}
}