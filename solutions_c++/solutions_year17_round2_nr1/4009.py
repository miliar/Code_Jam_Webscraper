#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <queue>
using namespace std;

typedef struct NODE{
	int pos, speed;
}node;

bool cmp(node a, node b){
	if(a.speed != b.speed)
		return a.speed > b.speed;
	return a.pos < b.pos;
}

int main(){
	int cas;
	while(scanf("%d", &cas)!=EOF){
		for(int t=1;t<=cas;t++){
			int d, n;
			scanf("%d %d", &d, &n);
			node h[n];
			for(int i=0;i<n;i++)
				scanf("%d %d", &h[i].pos, &h[i].speed);
			sort(h, h+n, cmp);
			queue<node> q;
			for(int i=0;i<n;i++)
				q.push(h[i]);
			while(q.size() != 1){
				node node1 = q.front();
				q.pop();
				node node2 = q.front();
				q.pop();
				if(min((double)(d-node1.pos)/node1.speed, (double)(d-node2.pos)/node2.speed) >= (double)(node2.pos-node1.pos)/(node1.speed-node2.speed))
					q.push(node2);
				else
					q.push(node1);
			}
			node last = q.front();
			double ans = (double)d*last.speed/(d-last.pos);
			printf("Case #%d: %.6lf\n", t, ans);
		}
	}
	return 0;
}