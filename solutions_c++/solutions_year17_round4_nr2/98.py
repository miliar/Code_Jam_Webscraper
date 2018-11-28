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
const double EPS=1e-10;
const double PI=acos(-1.0);
int ABS(int a){return max(a,-a);}
long long ABS(long long a){return max(a,-a);}
vector<int> g[1100];
int cnt[1100];
int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		int N,M,C;
		scanf("%d%d%d",&N,&C,&M);
		for(int i=0;i<1100;i++)g[i].clear();
		for(int i=0;i<1100;i++)cnt[i]=0;
		for(int i=0;i<M;i++){
			int p,q;
			scanf("%d%d",&p,&q);q--;
			g[q].push_back(p);
			cnt[p]++;
		}
		for(int i=0;i<C;i++)std::sort(g[i].begin(),g[i].end());
		int ret=0;
		for(int i=0;i<C;i++){
			ret=max(ret,(int)(g[i].size()));
		}
		int tot=0;
		for(int i=1;i<=N;i++){
			tot+=cnt[i];
			ret=max(ret,(tot+i-1)/i);
		}
		int req=0;
		for(int i=1;i<=N;i++)req+=max(0,cnt[i]-ret);
		printf("Case #%d: %d %d\n",t,ret,req);
	}
}