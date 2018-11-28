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
const int N = 100 + 10;
int n, p;
int rem[4];
int main() {
#ifndef ONLINE_JUDGE
//	freopen("myfile.in", "r", stdin);
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	for (int cas = 1; cas <= t; ++cas) {
		memset(rem, 0, sizeof rem);
		printf("Case #%d: ", cas);
		scanf("%d%d", &n, &p);
		for (int x,i = 0; i < n; ++i) {
			scanf("%d", &x);
			++rem[x%p];
		}
		int ans = rem[0];
		if (p == 2) 
			ans += (rem[1] + 1) / 2;
		else if (p == 3) {
			int mn = min(rem[1], rem[2]);
			ans += mn;
			rem[1] -= mn;
			rem[2] -= mn;
			ans += (rem[1]+2) / 3;
			ans += (rem[2] + 2) / 3;
		}
		else if (p == 4) {
			ans += rem[2] / 2;
			rem[2] -= rem[2] / 2 * 2;
			int mn = min(rem[1], rem[3]);
			ans += mn;
			rem[1] -= mn;
			rem[3] -= mn;
			if (rem[2]) {
				if (rem[1])
					ans += (rem[1] + 1) / 4 + 1;
				else if (rem[3])
					ans += (rem[3] + 1 / 4) + 1;
				else
					++ans;
			}
			else {
				ans += (rem[1]+3) / 4;
				ans += (rem[3] + 3) / 4;

			}
		}
		printf("%d\n", ans);


	}


	return 0;
}
