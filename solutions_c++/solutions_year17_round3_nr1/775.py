#include <iostream>
#include <string.h>
#include <cstdio>
#include <set>
#include <vector>
#include <map>
#include <cmath>
using namespace std;

typedef long long lint;
int N, K;
//lint H[2000], R[2000];
pair<lint, lint> A[2000]; // H, R

const lint INF = 1LL<<60;
const double PI = acos(-1);

lint dp[1100][1100];

lint rec(int p, int k) {
    if (k == K) {
        return 0;
    }
    if (p == N) {
        return -INF;
    }
    if (dp[p][k] != -INF) {
        return dp[p][k];
    }
    // with
    lint cur1 = rec(p + 1, k + 1);
    if (cur1 != -INF) {
        cur1 += A[p].first * A[p].second;
    }
    // without
    lint cur2 = rec(p + 1, k);
    lint res = max(cur1, cur2);
    return dp[p][k] = res;
}


void solve(int tst) {
    cin >> N >> K;
    for (int i = 0; i < N; ++i) {
        cin >> A[i].first >> A[i].second;
    }
    for (int i = 0; i <= N; ++i) {
        for (int j = 0; j <= K; ++j) {
            dp[i][j] = -INF;
        }
    }
    sort(A, A + N);
    reverse(A, A + N);
    double ans = -1e30;
    for (int i = 0; i < N; ++i) {
        lint cur = rec(i + 1, 1);
        if (cur == -INF) continue;
        double r = A[i].first;
        double h = A[i].second;
        double d = cur * 2 * PI + 2 * PI * r * h + PI * r * r;
        ans = max(ans, d);
    }
	printf("Case #%d: %0.12lf\n", tst, ans);
}

int main() {
	freopen("/Users/ryuzmukhametov/gcj/input.txt", "r", stdin);
	freopen("/Users/ryuzmukhametov/gcj/output.txt", "w", stdout);
	int tst;
	cin >> tst;
	for (int i = 1; i <= tst; ++i) {
		solve(i);
	}
	return 0;
}
