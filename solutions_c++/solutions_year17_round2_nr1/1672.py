#include <stdio.h>
#include <bits/stdc++.h>

using namespace std;
const int N = 1005;

int n, D;
pair <int,int> p[N];

bool cmp(pair <int,int> a, pair <int,int> b){
	if(a.first != b.first) return a.first > b.first;
	return a.second > b.second;
}

void init(){
	int T;
	scanf("%d",&T);
	for(int t=1; t<=T; t++){
		scanf("%d%d",&D,&n);
		for(int i = 0; i < n; i++){
			scanf("%d%d",&p[i].first,&p[i].second);
		}
		sort(p,p+n,cmp);
		double ti = 0;
		for(int i = 0; i < n; i++){
			double t1 = (D - p[i].first) / (double)p[i].second;
			ti = max(ti,t1);
		}
		double res = D / ti;
		printf("Case #%d: %.10lf\n",t,res);
	}
}

int main(){
	#ifndef ONLINE_JUDGE
		freopen("input.txt","r",stdin);
		freopen("output.txt","w",stdout);
	#endif
	init();
	return 0;
}