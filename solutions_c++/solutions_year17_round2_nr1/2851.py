#include <iostream>
#include <fstream>
#include <algorithm>
#include <stdio.h>
#include <string>
#include <math.h>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <bitset>

#define pb push_back
#define mp make_pair
#define mod 1000000007

using namespace std;

int n, t;
double d, x, y, mx;

int main() {
	freopen("A-large.in","r",stdin);
	freopen("data.out","w",stdout);
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cin >> d >> n;
		mx = 0;
		for (int j = 0; j < n; j++) {
			cin >> x >> y;
			mx = max(mx, (d - x) / y);
		}
		printf("Case #%d: %.6f\n", i, d / mx);
	}
}
