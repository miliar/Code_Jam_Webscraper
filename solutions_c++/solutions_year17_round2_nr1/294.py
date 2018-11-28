#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <stdio.h>
#include <string>
#include <map>
#include <set>
using namespace std;

void solve(int test) {
	double D;
	int N;
	cin >> D >> N;
	vector<pair<double, double> > poss(N);
	for (int i = 0; i < N; ++i) {
		cin >> poss[i].first >> poss[i].second;
	}
	double minspeed = 1e18;
	for (int i = 0; i < N; ++i) {
		minspeed = min(minspeed, D * poss[i].second / (D - poss[i].first));
	}
	printf("Case #%d: %.10lf\n", test, minspeed);
}

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i) {
		solve(i + 1);
	}
	return 0;
}