#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdio>
using namespace std;
typedef long long LL;

int L[1005], R[1005];
bool vis[1005];
int main(void)
{
	int T, ti = 0;
	scanf("%d",&T);
	while(++ti<=T)
	{
		LL N, K;
		scanf("%lld%lld",&N,&K);
		//for(int N = 1;N<=100;N++)
		//{
		//	printf("\n\nN: %d\n",N);
			memset(vis,0,sizeof(vis));
			for(int i=1;i<=N;i++)
				L[i]=i-1,R[i]=N-i;
			for(int k=1;k<=K;k++)
			{
				int t;
				for(int i=1;i<=N;i++)
					if(!vis[i]) {t = i; break;}
				for(int i=t+1;i<=N;i++)
				{
					if(vis[i]) continue;
					if(min(L[t],R[t])<min(L[i],R[i]))
						t=i;
					else if(min(L[t],R[t])==min(L[i],R[i])
						&&max(L[t],R[t])<max(L[i],R[i]))
						t=i;
				}
				vis[t]=1;
				for(int i=t-1;i>0;i--)
					if(vis[i]) break;
					else R[i]=t-1-i;
				for(int i=t+1;i<=N;i++)
					if(vis[i]) break;
					else L[i]=i-t-1;
				if(k==K) printf("Case #%d: %d %d\n",ti,max(L[t],R[t]),min(L[t],R[t]));
			//	printf("%d: %d %d\n",k,max(L[t],R[t]),min(L[t],R[t]));
			}
		//}
		//printf("Case #%d: ",ti);
	}
	return 0;
}
