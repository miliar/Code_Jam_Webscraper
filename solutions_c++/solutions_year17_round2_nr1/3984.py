#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>
using namespace std;
typedef long long ll;

struct horses {
	ll pos;
	ll sp;
} ar[10010];

bool operator < (horses a, horses b) {
	if (a.pos != b.pos)
		return a.pos < b.pos;
	return a.sp < b.sp;
}

int main() {
	freopen("/Users/viverma/Downloads/input.txt", "r", stdin);
	freopen("/Users/viverma/Downloads/output.txt", "w", stdout);
	ll t, d, n, i, changeInd;
	double finSp;
	cin>>t;
	for (ll test = 1; test <= t; test++) {
		changeInd = 0;
		cin>>d>>n;
		for (i = 0; i < n; i++) {
			cin>>ar[i].pos>>ar[i].sp;
		}
		sort (ar, ar+n);
		finSp = (double)ar[0].sp;
		for (i = 1; i < n; i++) {
			double frstTime = (double)(d - ar[i-1].pos) / (double)(ar[i-1].sp);
			double scndTime = (double)(d - ar[i].pos) / (double)(ar[i].sp);
			if (ar[i].sp < ar[i - 1].sp && frstTime < scndTime) {
				changeInd = i;
				finSp = ar[i].sp;
			}
		}
		double totalTime = (double)(d - ar[changeInd].pos) / (double)(finSp);
		double maxSpeed = (double) d / totalTime;
		printf("Case #%lld: %.6lf\n", test, maxSpeed);
	}

	return 0;
}