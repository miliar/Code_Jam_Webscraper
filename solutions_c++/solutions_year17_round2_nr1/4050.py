#include <bits/stdc++.h>

#define N 1000007
#define it(i, n) for(i = 0; i < n; ++i)
#define pb push_back
#define eps 1e-9
#define all(x) x.begin(), x.end() 

using namespace std;
typedef long long ll;

struct horse {
	double p;
	double v;
	bool operator< (horse h) const {
		return p < h.p;
	}
};

horse h[107];
int n;

// double solve(int i) {
// 	double vm;
// 	if(p == n-1) return h[i].v;
// 	r = solve(i+1);
// 	if(h[i].v <= h[i+1].v) return h[i].v;
// 	double t = (h[i+1].p - h[i].p)/(h[i].v - r);
// 	double alcance = t*h[i].v;
// 	if(alcance > d - h[i].p) return h[i].v;
// 	return (d - h[i].p)/(alcance + (((d - h[i].p) - alcance)/r));

// }

void run() {
	int i, j, k, t, p, q = 0;
	double d, res;
	scanf("%lf %d", &d, &n);
	res = 1e9;

	for(i = 0; i < n; ++i) {
		scanf("%lf %lf", &h[i].p, &h[i].v);
		if(((d - h[i].p)/h[i].v) > (d - h[q].p)/h[q].v) q = i;
	}
	res = (d*h[q].v)/(d - h[q].p);
	printf("%lf\n", res);
}

int main(int argc, char * argv[]) {
	int i, j, t;
	scanf("%d", &t);
	for(i = 0; i < t; ++i) {
		printf("Case #%d: ", i+1);
		run();
	}
	return 0;
}