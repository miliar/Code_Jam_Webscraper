#include<algorithm>
#include <iostream>
#include <stdlib.h>
#include <string.h>
#include  <stdio.h>
#include   <math.h>
#include   <time.h>
#include   <vector>
#include   <bitset>
#include    <queue>
#include      <set>
#include      <map>
using namespace std;

const int N=1005;

int n,c,m,ok[N][N],Num[N];
vector<int> G[N];

void solve()
{
	memset(ok,0,sizeof ok);
	memset(Num,0,sizeof Num);
	for(int i=0;i<N;i++)
		G[i].clear();
	cin>>n>>c>>m;
	for(int i=1,p,b;i<=m;i++)
		scanf("%d%d",&p,&b),G[p].push_back(b);
	int Ans=0;
	for(int i=1;i<=n;i++)
	{
		for(int j=0;j<G[i].size();j++)
		{
			int k=1;
			while(ok[k][G[i][j]]||Num[k]==i)
				k++;
			Num[k]++;ok[k][G[i][j]]=1;Ans=max(Ans,k);
		}
	}
	int Ans2=0;
	for(int i=1;i<=n;i++)
		Ans2+=max(0,int(G[i].size())-Ans);
	cout<<Ans<<" "<<Ans2<<endl;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
#endif
	int t;cin>>t;
	for(int i=1;i<=t;i++)
		printf("Case #%d: ",i),solve();
	return 0;
}

