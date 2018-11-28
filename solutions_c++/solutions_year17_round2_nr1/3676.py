#include <stdio.h>
#include <iostream>
#include <algorithm>
#define INF 987654321
using namespace std;
int t;
double d,n;
struct st {
	double k, s;
};
st str[1002];
double MAX = -INF;
void init() {
	MAX = -INF;
}
int main() {
	scanf("%d", &t);
	for (int test = 0; test < t; test++) {
		init();
		scanf("%lf %lf", &d, &n);
		for (int i = 0; i < n; i++) {
			scanf("%lf %lf", &str[i].k, &str[i].s);
		}
		for (int i = 0; i < n; i++) {
			double tmp = d - str[i].k;
			double div = 1 / str[i].s;
			double result = tmp * div;
			if (MAX < result) {
				MAX = result;
			}
		}
		double ans = d / MAX;
		cout << "Case #" << test + 1 << ": ";
		printf("%.6lf\n", ans);
	}
	return 0;
}