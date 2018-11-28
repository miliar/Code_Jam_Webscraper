#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<ctime>
#include<cmath>
#include<iostream>
#include<queue>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<string>
using namespace std;
typedef long long ll;
typedef double db;
typedef pair<db,db> per;
const int MOD = 1000000007;
const int INF = 1000000007;
const int N = 1005;
vector<int>t[N];
int a[N];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,ca=1;
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: ",ca++);
		int n,c,m;
		memset(a,0,sizeof(a));
		scanf("%d%d%d",&n,&c,&m);
		for(int i=0;i<m;i++)
		{
			int x,y;
			scanf("%d%d",&x,&y);
			t[x].push_back(y);
		}
		for(int i=1;i<=n;i++)
		{
			sort(t[i].begin(),t[i].end());
		}
		int r1=0,r2=0,tot=0;
		for(int i=1;i<=n;i++)
		{
			int sz=t[i].size(),cnt=0,sum=0;
			for(int j=0;j<sz;j++)
			{
				cnt++;
				if(j==sz-1||t[i][j]!=t[i][j+1])
				{
					int id=t[i][j];
					a[id]+=cnt;
					r1=max(r1,a[id]);
					cnt=0;
				}
				sum++;
			}
			tot+=sum;
			r1=max(r1,tot/i+(tot%i!=0));
		}
		for(int i=1;i<=n;i++)
		{
			int sz=t[i].size();
			if(sz>r1)r2+=sz-r1;
		}
		printf("%d %d\n",r1,r2);
		for(int i=1;i<=n;i++)t[i].clear();
	}
	return 0;
}

