#include<stdio.h>
#include<algorithm>
#include<math.h>
#include<string.h>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<time.h>
#include<assert.h>
#include<iostream>
using namespace std;
typedef long long LL;
typedef pair<int,int>pi;
int ned[55];
int n,m;
vector<pi>V[55];
int cur[55];
int main(){
	freopen("B-large.in.txt","r",stdin);
	freopen("B-large.out.txt","w",stdout);
	int cas=1;
	int _;scanf("%d",&_);
	while(_--){
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;i++)scanf("%d",ned+i),V[i].clear();
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				int x;scanf("%d",&x);
				int l=10*x/(11*ned[i]);
				int r=10*x/(9*ned[i]);
				if((10*x)%(11*ned[i]))l++;
				if(r>=l)V[i].push_back(pi(l,r));
				//printf("%d %d r=%d\n",i,l,r);
			}
			sort(V[i].begin(),V[i].end());
		}
		int ans=0;
		memset(cur,0,sizeof cur);
		while(1){
			int mx=-1;
			bool flag=1;
			for(int i=0;i<n;i++){
				if(cur[i]>=V[i].size()){flag=0;break;}
				mx=max(mx,V[i][cur[i]].first);
			}
			if(!flag)break;
			bool ok=1;
			for(int i=0;i<n;i++){
				if(V[i][cur[i]].second<mx){
					cur[i]++;
					ok=0;
					break;
				}
			}
			if(ok){
				ans++;
				for(int i=0;i<n;i++)cur[i]++;
			}
		}
		printf("Case #%d: ",cas++);
		printf("%d\n",ans);
	}
	return 0;
}
