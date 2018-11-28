#include <bits/stdc++.h>
using namespace std;
#define fi first
#define se second
#define mp make_pair
#define gc getchar
#define pb push_back
#define eb emplace_back
typedef pair<int,int> pii;
typedef long double LD;
typedef long long LL;
int tc,n,c,m,matchl[1005],matchr[1005];
vector <int> tempat[5],node[1005];
bitset <1005> visited;
int matching(int now){
	if(visited[now])
		return 0;
	visited[now]=true;
	for(auto v:node[now])
	{
		if(matchr[v]==-1||matching(matchr[v])==1)
		{
			matchr[v]=now;
			matchl[now]=v;
			return 1;
		}
	}
	return 0;
}
int main()
{
	freopen("BSmall.in","r",stdin);
	freopen("BSmall.out","w",stdout);
	scanf("%d",&tc);
	for(int test=1;test<=tc;test++)
	{
		for(int i=0;i<2;i++)
			tempat[i].clear();
		memset(matchl,-1,sizeof(matchl));
		memset(matchr,-1,sizeof(matchr));
		scanf("%d%d%d",&n,&c,&m);
		for(int i=1;i<=m;i++)
		{
			int pemilik,nomor;
			scanf("%d%d",&nomor,&pemilik);
			tempat[pemilik-1].pb(nomor);
		}
		for(int i=0;i<2;i++)
			sort(tempat[i].begin(),tempat[i].end());
		//cout<<"tersort"<<endl;
		if(tempat[0].size()>tempat[1].size())
			swap(tempat[0],tempat[1]);
		for(int i=0;i<(int) tempat[0].size();i++)
		{
			//cout<<"ini awal "<<node[i].size()<<endl;
			for(int j=0;j<(int) tempat[1].size();j++)
			{
				//cout<<i<<" "<<j<<endl;
				if(tempat[0][i]!=tempat[1][j])
					node[i].pb(j);
			}
		}
		int y=tempat[1].size(),z=0;
		for(int i=0;i<tempat[0].size();i++)
		{
			visited.reset();
			if(matching(i))
			{
				//I'm Okay
			}
			else
			{
				if(tempat[0][i]==1)
					y++;
				else
					z++;
			}
		}
		printf("Case #%d: %d %d\n",test,y,z);
		for(int i=0;i<tempat[0].size();i++)
			node[i].clear();
	}
}
