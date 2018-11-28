#include<vector>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

int n;

double D;

int main() {
	int T;
	scanf("%d", &T);
	while (T--) {
		scanf("%lf%d", &D, &n);
		vector<pair<double, double> > horse;
		for (int i = 0; i < n; ++i) {
			double x, v;
			scanf("%lf%lf", &x, &v);
			horse.push_back(make_pair(x, v));
		}
		sort(horse.begin(), horse.end());
		double t = 0;
		for (int i = (int)horse.size() - 1; i >= 0; --i) {
			t = max((D - horse[i].first) / horse[i].second, t);
		}
		double v = D / t;
		static int id = 0;
		printf("Case #%d: %.6f\n", ++id, v);
	}
	return 0;
}
