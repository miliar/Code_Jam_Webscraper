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

int q[10];

int main() {
	freopen("small.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	scanf("%d", &test);
	int count = 1;
	while(test--) {
		memset(q, 0, sizeof q);
		int n, p;
		scanf("%d %d", &n, &p);
		for(int i = 0; i<n; i++) {
			int x;
			scanf("%d", &x);
			q[x%p]++;
		}
		int ans = 0;
		if(p == 2) {
			ans = q[0] + q[1]/2;
			if(q[1]%2 != 0) ans++;
		} else if(p == 3) {
			int aux = min(q[1], q[2]);
			ans = q[0] + aux;
			q[1] -= aux;
			q[2] -= aux;
			ans += q[1]/3;
			ans += q[2]/3;
			if(q[1]%3 != 0) ans++;
			if(q[2]%3 != 0) ans++;
		} else {
			//TODO
		}
		printf("Case #%d: %d\n", count, ans);
		count++;
	}
	
	
	return 0;
}
