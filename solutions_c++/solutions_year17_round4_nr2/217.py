#include <queue>
#include <limits>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <iostream>
using namespace std;

//MinCostMaxFlow mcmf;
struct node{
	int p,b;
}s[11111];
int cnt[1111];
bool cmp(node a,node b){
	return a.p<b.p;
}
int main(){

	freopen("B-large (1).in","r",stdin);
	freopen("B-large (1).out","w",stdout);
//	puts("dsad");
	int tt,ri=0;
	scanf("%d",&tt);
	while(tt--){
		memset(cnt,0,sizeof(cnt));
		int n,c,m;
		scanf("%d%d%d",&n,&c,&m);
		for(int i=0;i<m;++i){
			scanf("%d%d",&s[i].p,&s[i].b);
			cnt[s[i].b]++;
		}
		int ccnt=0;
		for(int i=1;i<=c;++i)
			ccnt=max(ccnt,cnt[i]);
		sort(s,s+m,cmp);
		for(int i=0;i<m;++i){
			int tmp=(i+1+s[i].p-1)/s[i].p;
			if(tmp>ccnt)
				ccnt=tmp;
		}
		int ans=0;
		int k=0;
		for(int i=0;i<m;++i){
			k++;
			if(i==m-1||s[i].p!=s[i+1].p)
			{
				if(k>=ccnt)
					ans+=k-ccnt;
				k=0;
			}
		}
		printf("Case #%d: %d %d\n",++ri,ccnt,ans);

	}
}
