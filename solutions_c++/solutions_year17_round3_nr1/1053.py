#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <iostream>
#include <climits>
#include <set>
#include <cmath>
#define ll long long

using namespace std;

struct aa {
    double area;
	int i;
    bool operator < (const aa &b) {
        return area > b.area;
    }
}a[1000];

bool cmp(int a, int b) {return a > b;}
int main() {
	//double pi = 3.141592654;
	double pi = M_PI;
	int T;
	cin >> T;
	for (int nm=1;nm<=T;nm++) {
		int n, k;
		cin >> n >> k;
		double r[1000], h[1000];
		for (int i=0;i<n;i++) {
			cin >> r[i] >> h[i];
			a[i].area = 2.0 * pi * r[i] * h[i];
			//a[i].area = 2.0 * r[i] * h[i];
			a[i].i = i;
		}
		sort(a, a+n);
		//for (int i=0;i<n;i++) printf("i = %d, area = %lf\n", a[i].i, a[i].area);
		double max_ans = 0;
		for (int i=0;i<n;i++) {
			double ans = pi * r[i] * r[i] + 2.0 * pi * r[i] * h[i];
			//double ans = r[i] * r[i] + 2.0 * r[i] * h[i];
			int ct = 1;
			for (int j=0;j<n && ct < k;j++) {
				if (a[j].i != i) {
					//printf("ji = %d, i = %d, ans = %lf, ct = %d\n", a[j].i, i, ans, ct);
					ans += a[j].area;
					ct++;
				}
			}
			max_ans = max(max_ans, ans);
		}
		printf("Case #%d: %.9lf\n", nm, max_ans);
	}
	return 0;
}
