#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;
typedef long long ll;
//typedef pair<double, int> P;
struct ind_t {
	double ind;
	double top;
	int i;
};
struct top_t {
	double top;
	int i;
};

const int MAX_N = 1000;
int n;
int k;
double r[MAX_N];
double h[MAX_N];
double ind[MAX_N];
double top[MAX_N];
ind_t ind_s[MAX_N];
top_t top_s[MAX_N];
//pair<double, int> ind[MAX_N];
//pair<double, int> top[MAX_N];
//double ind[MAX_N];
//double top[MAX_N];

double solve() {
	bool used[MAX_N] = {};

	scanf("%d%d", &n, &k);

	for (int i=0; i<n; i++) {
		scanf("%lf", &r[i]);
		scanf("%lf", &h[i]);
		ind[i] = 2 * r[i] * h[i];
		top[i] = r[i] * r[i];
		ind_s[i] = {ind[i], top[i], i};
		top_s[i] = {top[i], i};
		//ind[i] = make_pair(2 * r[i] * h[i], i);
		//top[i] = make_pair(r[i] * r[i], i);
	}
	sort(ind_s, ind_s+n, [](ind_t p1, ind_t p2){return p1.ind>p2.ind || p1.ind==p2.ind && p1.top > p2.top;});
	sort(top_s, top_s+n, [](top_t p1, top_t p2){return p1.top>p2.top;});

	double sum = 0;
	double max_top = 0;
	for (int i=0; i<k-1; i++) {
		sum += ind_s[i].ind;
		used[ind_s[i].i] = true;
		max_top = max(max_top, top[ind_s[i].i]);
	}
	used[ind_s[k-1].i] = true;
	max_top = max(max_top, top[ind_s[k-1].i]);
	double sum2 = ind_s[k-1].ind + max_top;
	for (int i=0; i<n; i++) {
		if (used[top_s[i].i]) {
			break;
		}
		sum2 = max(sum2, ind[top_s[i].i] + top_s[i].top);
	}
	return (sum + sum2) * M_PI;
}

int main() {
	int t;
	scanf("%d\n", &t);

	for (int i=1; i<=t; i++) {
		printf("Case #%d: %.9f\n", i, solve());
	}
}
