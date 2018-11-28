#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>
 
#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<set>
#include<queue>
#include<stack>
#include<algorithm>
using namespace std;
 
#define fori(a,b) for(i = a; i <= b; i++)
#define forj(a,b) for(j = a; j <= b; j++)
#define fork(a,b) for(k = a; k <= b; k++)
#define scani(a) scanf("%d",&a);
#define scanlli(a) scanf("%lld", &a);
#define scanc(c) scanf("%c",&c);
#define scans(s) scanf("%s", s);
#define mp(a,b) make_pair(a, b)
#define ll(a) (long long int)(a)
#define vi vector<int>
#define vc vector<char>
#define vs vector<string>
#define println printf("\n");
#define sz(v) v.size()
#define len(s) s.length()
#define max(a,b) ((a > b) ? a : b)
#define min(a,b) ((a < b) ? a : b)

int main() {
	int t, n, k, x, y;
	scani(t)
	for (int tc = 1; tc <= t; tc++) {
		scani(n)
		scani(k)
		priority_queue<int> pq;
		pq.push(n);
		for (int i = 1; i <= k; i++) {
			int mx = pq.top(); 
			pq.pop();
			if (mx % 2 == 1) {
				x = (mx - 1) / 2;
				y = (mx - 1) / 2;
			} else {
				x = mx / 2;
				y = mx / 2 - 1;
			}
			if (x > 0) {
				pq.push(x);
			}
			if (y > 0) {
				pq.push(y);
			}
		}
		printf("Case #%d: %d %d\n", tc, x, y);
	}
}