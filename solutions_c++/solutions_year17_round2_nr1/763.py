#include <algorithm>
#include <assert.h>
#include <iostream>
#include <string.h>
#include <memory.h>
#include <stdio.h>
#include <complex>
#include <cstdlib>
#include <sstream>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <vector>
#include <string>
#include <bitset>
#include <cstdio>
#include <queue>
#include <stack>
#include <cmath>
#include <set>
#include <map>
#include<deque>
typedef long long ll;
using namespace std;
const int N = 1000 + 10;
int n, d;
int main() {
#ifndef ONLINE_JUDGE
//	freopen("myfile.in", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	for (int cas = 1; cas <= t; ++cas) {
		printf("Case #%d: ", cas);
		scanf("%d%d", &d, &n);
		double mx = 0;
		
		for (int x, y, i = 0; i < n; ++i) {
			scanf("%d%d", &x, &y);
			mx = max(mx, (d-x) / (double)y);
		}
		double ans=d/mx;
		printf("%.6lf\n", ans);


	}

	return 0;
}

