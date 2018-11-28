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
    int x, y;
    bool operator < (const aa &b) {
        if (x != b.x) return x < b.x;
        return y < b.y;
    }
};

bool cmp(int a, int b) {return a > b;}
int bsearch(int *a, int n, int k);

int main() {
	int T;
	cin >> T;
	for (int nm=1;nm<=T;nm++) {
		int n, k;
		cin >> n >> k;
		double u, p[51];
		cin >> u;
		for (int i=0;i<n;i++) cin >> p[i];
		p[n] = 1;
		sort(p, p+n);
		for (int i=1;i<=n && u>0;i++) {
			if (p[i] > p[i-1]) {
				double a = min(u / (double)i, p[i] - p[i-1]);
				//printf("a = %lf, dif = %lf\n", a, p[i] - p[i-1]);
				for (int j=0;j<i;j++) p[j] += a;
				u -= a * (double) i;
			}
			/*
			printf("p ");
			for (int i=0;i<n;i++) printf("%lf ", p[i]);
			printf("\n");
			*/
		}
		double ans = 1;
		/*
		printf("p ");
		for (int i=0;i<n;i++) printf("%lf ", p[i]);
		printf("\n");
		*/
		for (int i=0;i<n;i++) ans *= p[i];
		printf("Case #%d: %lf\n", nm, ans);
	}
	return 0;
}

int bsearch(int *a, int n, int k) {
    int l = 0, h = n;
    while (l < h) {
        int m = (l + h) / 2;
        if (a[m] == k) return m;
        else if (a[m] > k) h = m;
        else l = m + 1;
    }
    return l;
}
