#include <stdio.h>
#include <stack>
#include <map>
#include <string.h>
#include <string>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <math.h>
#include <vector>
#include <set>
#include <queue>
using namespace std;
#define ll long long
#define mp make_pair
#define pb push_back
//#define ld long double
const double sn = 1e-9;
ll d, n;
pair<ll, ll> ks[1005];
bool check(long double v) {
	for (int i = 0; i < n; i++) {
		if (ks[i].second >= v)
			continue;
		long double dis = (ks[i].first*v)/(v-ks[i].second);
		if (dis < d)
			return false;
	}
	return true;
}
int main() {
	freopen("A-large.in","r",stdin);
	freopen("alarge.out","w",stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		scanf("%I64d%I64d", &d, &n);
		for (int i = 0; i < n; i++) {
			scanf("%I64d%I64d", &ks[i].first, &ks[i].second);
		}
		long double l = 1, r = 1e14;
		for (int i = 0; i < 200; i++) {
			long double mid = (l + r) / 2;
			if (check(mid))
				l = mid;
			else
				r = mid;
		}
		printf("Case #%d: %lf\n",i+1,l);
	}
	return 0; 
}