#include <bits/stdc++.h>
#include <string.h>
#include <cmath>
#define mp make_pair
#define pb push_back
#define f first
#define s second
#define lb lower_bound
#define ub upper_bound

typedef long long int ll;
typedef unsigned long long int ull;

const int N = 1e5 + 50;
const int INF = 0x3f3f3f3f;
const long long int INFL = 0x3f3f3f3f3f3f3f3f;
const double pi = atan(1.0)*4.0;

double maxd(double a, double b) {
	if (a > b) return a;
	return b;
}

int main(void) {
	int t, n;
	double d;
	
	scanf("%d", &t);
	
	double p, v;
	for(int test = 1; test <= t; test++) {
		scanf("%lf %d", &d, &n);
		double maxt = 0.0;
		while(n--) {
			scanf("%lf %lf", &p, &v);
			maxt = maxd(maxt, (d-p)/v);
		}
		printf("Case #%d: %.6lf\n", test, d/maxt);
	}

	return 0;
}