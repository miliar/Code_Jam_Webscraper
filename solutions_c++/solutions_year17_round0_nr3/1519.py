#include<cstdio>
#include<cstring>
#include<vector>
#include<iostream>
#include<cmath>
#include<algorithm>
#include<queue>
#include<string>
#include<cstdlib>
#include<set>
#define mem(a,b) memset(a,b,sizeof(a))
#define LL __int64
#define MAX 1000010
using namespace std;

struct NODE{
	LL x, cnt;
	bool operator<(const struct NODE &a)const{
		return x > a.x;
	}
}nodes[5], temp[5];

LL n, k;

int main(){
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int ii = 1; ii <= t; ii++){
		scanf("%I64d%I64d", &n, &k);
		nodes[0].x = n;
		nodes[0].cnt = 1;
		int cou = 1;
		while(k){
			if (nodes[0].cnt >= k){
				printf("Case #%d: %I64d %I64d\n",ii,nodes[0].x / 2, (nodes[0].x - 1) / 2);
				break;
			}
			else{
				k -= nodes[0].cnt;
				if (nodes[0].x > 2){
					nodes[cou].x = (nodes[0].x - 1) / 2;
					nodes[cou].cnt = nodes[0].cnt;
					cou++;
				}
				if (nodes[0].x > 1){
					nodes[0].x = nodes[0].x / 2;
				}
			}
			sort(nodes, nodes + cou);
			int cc = 0;
			for (int i = 1; i < cou; i++){
				if (nodes[i].x == nodes[cc].x){
					nodes[cc].cnt += nodes[i].cnt;
				}
				else{
					cc++;
					nodes[cc] = nodes[i];
				}
			}
			cou = cc + 1;
		}
	}
	return 0;
}