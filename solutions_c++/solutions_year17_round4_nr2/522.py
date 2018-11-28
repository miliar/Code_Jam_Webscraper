//hi
#include<bits/stdc++.h>
using namespace std;
#define PB push_back
#define MP make_pair
#define F first
#define S second
typedef long long int LL;
vector<int> v[1002];
int n,c,m;
int cmp(vector<int> a,vector<int> b){
	if(a.size()>b.size()) return 1;
	return 0; 
}
int ans2;
int cnt[1002];
int lft[1002];
int check(int g){
	int i,j;
	cnt[0]=0;
	for(i=1;i<=n;i++) cnt[i]=g, lft[i]=0;
	for(i=1;i<=c;i++){
		for(j=0;j<(int)(v[i].size());j++){
			int d=v[i][j];
			//printf("%d %d\n",i,d);
			if(cnt[d]>0) cnt[d]--;
			else lft[d]++;
		}
	}
	//for(i=1;i<=n;i++) printf("left %d %d\n",i,lft[i]);
	for(i=1;i<=n;i++) cnt[i]+=cnt[i-1];
	for(i=1;i<=n;i++) lft[i]+=lft[i-1];
	for(i=1;i<=n;i++)
		if(lft[i]>cnt[i]) return 0;
	ans2=lft[n];
	return 1;
}
int main(void){
    int t,hh;
    scanf("%d",&t);
    for(hh=1;hh<=t;hh++){
		scanf("%d%d%d",&n,&c,&m);
		int i,j;
		for(i=1;i<=c;i++) v[i].clear();
		for(i=0;i<m;i++){
			int a,b;
			scanf("%d%d",&a,&b);
			v[b].PB(a);
		}
		//sort(v+1,v+1+c,cmp);
		int lb=0;
		for(i=1;i<=c;i++) lb=max(lb, (int)(v[i].size()));
		int ub=m;
		//printf("~  %d %d\n",lb,ub);
		while(lb<ub){
			int mid=(lb+ub)/2;
			if(check(mid)) ub=mid-1;
			else lb=mid+1;
		}
		while(check(lb)==0) lb++;
		printf("Case #%d: %d %d\n",hh,lb,ans2);
	}
    return 0;
}
