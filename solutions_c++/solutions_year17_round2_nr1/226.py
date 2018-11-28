#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

#define MAXN 1200

int tn;
int n;
double loc[MAXN], sp[MAXN];
double D;

bool is_valid(long double s0) {

	vector<pair<long double, long double> > a, na;

	for(int i = 0; i < n; i++)
		a.push_back(make_pair(loc[i], sp[i]));
	a.push_back(make_pair(0, s0));
	a.push_back(make_pair(D, 0));
	sort(a.begin(), a.end());

	while (a.size() > 1) {
		// find the next horse that catches up with a previous one
		//printf("a.size() = %d\n", a.size());
		long double min_time = 1e100;
		int min_i = -1;
		for(int i = 0; i < a.size()-1; i++) 
			if (a[i].second > a[i+1].second) {
				long double t = (a[i+1].first - a[i].first) / (a[i].second - a[i+1].second);
				if (t < min_time) {
					min_time = t;
					min_i = i;
				}
			}

		//printf("min_i = %d, min_time = %lf\n", min_i, min_time);

		if (min_i == 0) { // Annie's horse activates
			long double next_K = a[0].first + a[0].second * min_time;
			if (fabs(next_K - D) < 1e-12) return true; else return false;
		}
		na.clear();
		for(int i = 0; i < a.size(); i++)
			if (i != min_i) {
				long double next_K = a[i].first + a[i].second * min_time;
				long double next_S = a[i].second;
				na.push_back(make_pair(next_K, next_S));
			}
		a = na;
	}

	return true;

}

int main() {

	scanf("%d", &tn);
	for(int ctn = 0; ctn < tn; ctn ++) {

		scanf("%lf %d", &D, &n);
		double max_speed = 0;
		for(int i = 0; i < n; i++) {
			scanf("%lf %lf\n", &loc[i], &sp[i]);
			double t_speed = D / ((D - loc[i]) / sp[i]);
			if (t_speed > max_speed) max_speed = t_speed;
		}

		long double lft = 0, rght = max_speed;
		//printf("max_speed = %lf\n", max_speed);
		while (fabs(lft - rght) > 1e-7 && (fabs(rght) < 1e-7 || fabs(lft-rght) / fabs(rght) > 1e-7)) {
			long double mid = 0.5 * (lft + rght);
			//printf("lft = %lf, rght = %lf, mid = %lf\n", lft, rght, mid);
			//printf("%e, %e, %e\n", fabs(lft-rght), fabs(rght), fabs(lft-rght) / fabs(rght));
			if (is_valid(mid)) lft = mid; else rght = mid;
			//printf("Done\n");
		}
		//double lft = (double)(is_valid(90));

		printf("Case #%d: %0.7lf\n", ctn+1, (double)lft);

	}

	return 0;

}