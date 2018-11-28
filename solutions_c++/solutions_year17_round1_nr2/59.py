#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<queue>
#include<deque>
#include<string>
#include<string.h>
#include<vector>
#include<set>
#include<map>
#include<stdlib.h>
#include<cassert>
using namespace std;
const long long mod=1000000007;
const long long inf=mod*mod;
const long long d2=500000004;

vector<pair<int,int> > g[60];
int at[60];
int p[60];
int main(){
	int T;scanf("%d",&T);
	for(int t=1;t<=T;t++){
		int a,b;
		scanf("%d%d",&a,&b);
		for(int i=0;i<a;i++){
			scanf("%d",p+i);
			p[i]*=10;
		}
		for(int i=0;i<60;i++)g[i].clear();
		for(int i=0;i<a;i++)for(int j=0;j<b;j++){
			int q;
			scanf("%d",&q);
			q*=10;
			int R=q/(p[i]-p[i]/10);
			int L=(q+p[i]+p[i]/10-1)/(p[i]+p[i]/10);
			if(L>R)continue;
			g[i].push_back(make_pair(R,L));
		}
		for(int i=0;i<a;i++)std::sort(g[i].begin(),g[i].end());
		for(int i=0;i<60;i++)at[i]=0;
		int ret=0;
		while(1){
			int s=mod;
			int r=0;
			bool dame=false;
			for(int i=0;i<a;i++){
				if(at[i]==g[i].size()){
					dame=true;break;
				}
				s=min(s,g[i][at[i]].first);
				r=max(r,g[i][at[i]].second);
			}
			if(dame)break;
			if(s>=r){
				ret++;
				for(int i=0;i<a;i++)at[i]++;
			}else{
				for(int i=0;i<a;i++){
					while(at[i]<g[i].size()&&g[i][at[i]].first<r)at[i]++;
				}
			}
		}
		printf("Case #%d: %d\n",t,ret);
	}
}