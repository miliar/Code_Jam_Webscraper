/* ***********************************************
 	Author        : luckcul
 	Mail          : tyfdream@gmail.com
 	Created Time  : 2017-04-08 20:31:53
 	Problem       : problem
************************************************ */
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <map>
#include <set>
using namespace std;
#define INF 1000000000
//typedef __int64 LL;
struct node{
	int v, t;
	friend bool operator<(node x, node y) {
		return x.v < y.v;
	}
};

int t, k, n;

int main() {
#ifndef ONLINE_JUDGE
	// freopen("in.txt", "r", stdin);
	freopen("C-small-2-attempt0.in", "r", stdin);
	freopen("C-small-2-attempt0.out", "w", stdout);
#endif // ONLINE_JUDGE
	scanf("%d", &t);
	for(int ti = 0; ti < t; ti ++) {
		scanf("%d%d", &n, &k);

		priority_queue<node> Q;
		// Q.clear();
		node s;
		s.v = n; s.t = 1;
		Q.push(s);
		for(int i = 0; i < k-1; i++) {
			node now = Q.top();
			// printf("%d %d \n", now.v, now.t);
			if(now.v % 2) {
				node a;
				a.v = now.v/2;
				a.t = 2;
				Q.push(a);
				// printf("1in: %d %d \n", a.v, a.t);
			}
			else {
				node a, b;
				a.v = now.v/2;
				a.t = 1;
				b.v = now.v/2 - 1;
				b.t = 1;
				Q.push(a);
				Q.push(b);
				// printf("2in : %d %d, %d %d\n", a.v, a.t, b.v, b.t);
			}
			// cout<<"size: "<<Q.size()<<endl;
			// node temp = Q.top();
			// printf("temp: %d %d\n", temp.v, temp.t);
			Q.pop();
			// cout<<"size: "<<Q.size()<<endl;
			if(now.t > 1){
				now.t --;
				Q.push(now);
			}
			// cout<<"size: "<<Q.size()<<endl;
		}

		node ans = Q.top();
		// printf("out: %d %d\n", ans.v, ans.t);
		printf("Case #%d: ", ti+1);
		if(ans.v % 2) printf("%d %d\n", ans.v/2, ans.v/2);
		else printf("%d %d\n", max(0, ans.v/2), max(0, ans.v/2-1));
	}

	return 0;
}
