#include <stdio.h>
#include <bits/stdc++.h>

using namespace std;
const int N = 1005;

int n, r, o, y, g, v, b, pre, started, k;
char s[N], ch[] = {'R', 'Y', 'B'}, res[N];
pair <int,int> p[N];

bool cmp(pair <int,int> a, pair <int,int> b){
	if(a.first == pre) return 0;
	if(b.first == pre) return 1;
	if(a.second != b.second) return a.second > b.second;
	if(a.first == started) return 1;
	if(b.first == started) return 0;
	return a.first < b.first;
}

void init(){
	int T;
	scanf("%d",&T);
	for(int t=1; t<=T; t++){
		scanf("%d%d%d%d%d%d%d",&n,&r,&o,&y,&g,&b,&v);
		p[0] = make_pair(0,r);
		p[1] = make_pair(1,y);
		p[2] = make_pair(2,b);
		started = pre = -1;
		k = 0;
		while(n--){
			sort(p,p+3,cmp);
			p[0].second--;
			res[k++] = ch[p[0].first];
			pre = p[0].first;
			if(started == -1) started = p[0].first;
		}
		res[k] = 0;
		if(p[0].second or p[1].second or p[2].second or res[0] == res[k - 1])
			printf("Case #%d: IMPOSSIBLE\n",t);
		else
			printf("Case #%d: %s\n",t,res);
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