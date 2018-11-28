/******************************************
*    AUTHOR:         BHUVNESH JAIN        *
*    INSTITUITION:   BITS PILANI, PILANI  *
******************************************/
#include <bits/stdc++.h>
using namespace std;
 
typedef long long LL; 
typedef long double LD;
typedef pair<int,int> pii;
typedef pair<LL, LL> pll;

int ans;

bool poss(vector<pii> a, vector<pii> b, vector<pii> c, vector<pii> d) {
	for(int i = 0; i < c.size(); ++i) {
		if (c[i].first < 0 || c[i].second > 1440) {
			return 0;
		}
	}
	for(int i = 0; i < d.size(); ++i) {
		if (d[i].first < 0 || d[i].second > 1440) {
			return 0;
		}
	}
	for(int i = 0; i < a.size(); ++i) {
		for(int j = 0; j < c.size(); ++j) {
			if (a[i].first >= c[j].second || a[i].second <= c[j].first) {
				//
			}
			else {
				return 0;
			}
		}
	}
	for(int i = 0; i < b.size(); ++i) {
		for(int j = 0; j < d.size(); ++j) {
			if (b[i].first >= d[j].second || b[i].second <= d[j].first) {
				//
			}
			else {
				return 0;
			}
		}
	}
	return 1;
}

void solve2(vector<pii> a, vector<pii> b) {
	vector<pii> c(1), d(1);
	c[0].first = 0;
	c[0].second = 720;
	d[0].first = 720;
	d[0].second = 1440;
	if (poss(a, b, c, d)) {
		ans = 2;
	}
}

void solve3(vector<pii> a, vector<pii> b) {
	vector<pii> c(2), d(1);
	for(int i = 1; i < 720; ++i) {
		c[0].first = 0;
		c[0].second = i;
		d[0].first = i;
		d[0].second = i+720;
		c[1].first = i+720;
		c[1].second = 1440;
		if (poss(a, b, c, d)) {
			ans = min(ans, 3);
			return ;
		}
	}
}

void solve4(vector<pii> a, vector<pii> b) {
	vector<pii> c(2), d(2);
	for(int i = 1; i < 720; ++i) {
		for(int j = i+1; j < i+720; ++j) {
			c[0].first = 0;
			c[0].second = i;
			d[0].first = i;
			d[0].second = j;
			c[1].first = j;
			c[1].second = j + (720-i);
			d[1].first = j + (720-i);
			d[1].second = 1440;
			if (d[1].first > 1440) {
				break;
			}
			if (poss(a, b, c, d)) {
				ans = min(ans, 3);
				return ;
			}
		}
	}
}

// void solve5(vector<pii> a, vector<pii> b) {
// 	vector<int> c(3), d(2);
// 	for(int i = 1; i < 720; ++i) {
// 		for(int j = i+1; j < i+720; ++j) {
// 			for(int k = j+1; k < j+720; ++k) {
// 				c[0].first = 0;
// 				c[0].second = i;
// 				d[0].first = i;
// 				d[0].second = j;
// 				c[1].first = j;
// 				c[1].second = k;
// 				d[1].first = k;
// 				d[1].second = 720 - (j-i);
// 				c[2].first = 720 - (j-i);
// 				c[2].second = 1440;
// 				if (poss(a, b, c, d)) {
// 					ans = min(ans, 3);
// 					return ;
// 				}
// 			}
// 		}
// 	}
// }

int main() {
	int t, n, k;
	scanf("%d", &t);
	for(int T = 1; T <= t; ++T) {
		printf("Case #%d: ", T);
		scanf("%d %d", &n, &k);
		vector<pii> a(n), b(k);
		for(int i = 0; i < n; ++i) {
			scanf("%d %d", &a[i].first, &a[i].second);
		}
		for(int i = 0; i < k; ++i) {
			scanf("%d %d", &b[i].first, &b[i].second);
		}
		sort(a.begin(), a.end());
		sort(b.begin(), b.end());
		ans = INT_MAX;
		solve2(a, b);
		solve2(b, a);
		if (ans == 2) {
			printf("2\n");
			continue;
		}
		solve3(a, b);
		solve3(b, a);
		if (ans == 3) {
			printf("2\n");
			continue;
		}
		printf("4\n");
		continue;
		solve4(a, b);
		solve4(b, a);
		if (ans == 4) {
			printf("4\n");
			continue;
		}
		assert(false);
	}
	return 0;
}