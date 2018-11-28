#include<cstdio>
#include<cassert>
#include<cstring>
#include<map>
#include<set>
#include<time.h>
#include<algorithm>
#include<stack>
#include<queue>
#include<utility>
#include<cmath>
#include<iostream>
#include<string>
#include<vector>
#include <limits>

using namespace std;

typedef pair <int, int> ii;
const long long INF = 1e9 + 7;
const long long INF9 = 1e9 + 9;

long long gcd(long long b, long long s){
	return (s != 0) ? gcd(s, b%s) : b;
}

long long pw(long long a, long long b, long long c) {
	if (b == 0) return 1;
	else if (b == 1) return a%c;
	else {
		long long A = pw(a, b / 2, c);
		A = (A*A) % c;
		if (b & 1) A = (A*a) % c;
		return A;
	}

}

const int N = 1002;
double k[N], s[N], t[N];
ii p[N];

void solve() {

	double d;
	int n;
	scanf("%lf %d", &d, &n);

	for (int i = 1; i <= n; i++) {
		scanf("%lf %lf", k + i, s + i);
		p[i] = ii(k[i], s[i]);
	}
	sort(p + 1, p + n + 1);

	for (int i = 1; i <= n; i++) {
		k[i] = p[i].first;
		s[i] = p[i].second;
	}
	
	for (int i = n; i >= 1; i--) {
		t[i] = (d - k[i]) / s[i];
		for (int j = i + 1; j <= n; j++) {
			if (s[j] < s[i]) {
				double q = (k[j] - k[i]) / (s[i] - s[j]);
				if (q <= t[i]) {
					t[i] = -1;
					break;
				}
			}
		}
	}

	double ans = 0.0;
	for (int i = 1; i <= n; i++)
		ans = max(ans, t[i]);
	printf("%.10lf\n", d / ans);
}


int main() {
//	freopen("in.txt", "r", stdin);
//	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int R = 1; R <= T; R++) {
		printf("Case #%d: ", R);
		solve();
	}

}