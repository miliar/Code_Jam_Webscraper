#include <stdio.h>
#include <string>
#include <string.h>
#include <set>
#include <map>
#include <algorithm>
#include <cstdlib>
#include <queue>
#include <cmath>
#include <vector>
#include <iostream>

using namespace std;

#define MAXN 1010

int q[MAXN];
int v[MAXN];

int n, c, m;

int can(int x) {
	int sum = 0;
	int ret = 0;
	for(int i = 1; i<=n; i++) {
		int available = (i-1)*x-sum;
		if(v[i] > x) {
			int changes = v[i]-x;
			if(available < changes) return -1;
			ret += changes;
		}
		sum += v[i];
	}
	return ret;
}

int main() {
	freopen("large.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	scanf("%d", &test);
	int count = 1;
	while(test--) {
		memset(q, 0, sizeof q);
		memset(v, 0, sizeof v);
		int beg = 0, end = 2000;
		scanf("%d %d %d", &n, &c, &m);
		for(int i = 0; i<m; i++) {
			int p, b;
			scanf("%d %d", &p, &b);
			q[b]++;
			v[p]++;
		}
		for(int i = 1; i<=c; i++) {
			beg = max(beg, q[i]);
		}
		while(beg < end) {
			int mid = (beg+end)/2;
			if(can(mid) != -1) {
				end = mid;
			} else {
				beg = mid+1;
			}
		}
		
		printf("Case #%d: %d %d\n", count, beg, can(beg));
		count++;
	}
	
	
	return 0;
}
