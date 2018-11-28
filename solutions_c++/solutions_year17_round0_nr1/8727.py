#include <iostream>
#include <cstring>
#include <vector>
#include <cstring>
#include <queue>
#include <utility>
using namespace std;
int T;
int k;
int ca=1;
int dp[1030]={-1};
char inp[1000];
queue<pair<int,int> > q;
// void bfs(int mk,int dep,int k,int l)
// {
// 	int mi=0x3f3f3f;
// 	for(int i=0;i+k>strlen(inp);i++)
// 	{
// 		int mask=((1<<(l-i))-1)^((1<<(l-i-k))-1);
// 		if(mk^mask==0)
// 		{
// 			mi=min(dep,mi);
// 			return;
// 		}
// 		if(dp[mk^mask]!=-1)
// 		{
// 			mi=min(mi,dp[mk^mask]);
// 			return;
// 		}
// 		if(dp[mk^mask]==-2)
// 		{
// 			return;
// 		}
// 		bfs(mk^mask,dep+1,k,l);
// 	}
// }
int main()
{
	scanf("%d",&T);
	
	dp[0]=0;
	int ans=0;
	int f;
	while(T--)
	{
		scanf("%s %d",inp,&k);
		memset(dp,-1,sizeof(dp));
		// cout<<strlen(inp)<<endl;
		int mk=0;
		int l=strlen(inp);
		queue<pair<int,int> > q;
		int inqueue[1030]={-1};
		memset(inqueue,0,sizeof(inqueue));

		for(int i=0;i<l;i++)
		{
			if(inp[i]=='+')
			{
				mk=mk<<1;
			}
			else
				mk=(mk<<1)|1;
		}
		int la=mk;
		if(mk==0)
		{
			printf("Case #%d: %d\n",ca++,0);
			continue;
		}
		else
		{
			pair<int,int> p = make_pair(mk,1);
			q.push(p);
			inqueue[mk]=1;
			f = -1;
			while(!q.empty()&&f==-1)
			{
				pair<int,int> t = q.front();
				q.pop();
				mk=t.first;
				inqueue[mk]=1;
				// if(t.second>10)
				// {
				// 	f=0;
				// 	break;
				// }
				// cout<<"mk is "<<mk<<endl;
				for(int i=0;i<l;i++)
				{
					if(i+k>strlen(inp))
						continue;
					int mask=((1<<(l-i))-1)^((1<<(l-i-k))-1);
					// cout<<"mask is "<<mask<<endl;
					if((mk^mask)==0)
					{
						f=1;
						printf("Case #%d: %d\n",ca++,t.second);
						break;
					}
					if(inqueue[mk^mask])
					{
						// f=0;
						// // printf("Case 2#%d: %d\n",ca++,dp[mk^mask]);
						// break;
						continue;
					}
					p=make_pair(mk^mask,t.second+1);
					q.push(p);
				}
			}
		}
		if(f!=1)
		{
			printf("Case #%d: IMPOSSIBLE\n",ca++);
		}
	}
	return 0;
}