#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<string>
#include<iomanip>
#include<vector>
#include<set>
#include<map>
#include<queue>

using namespace std;
typedef long long LL;
typedef unsigned long long ULL;

#define rep(i,k,n) for(int i=(k);i<=(n);i++)
#define rep0(i,n) for(int i=0;i<(n);i++)
#define red(i,k,n) for(int i=(k);i>=(n);i--)
#define sqr(x) ((x)*(x))
#define clr(x,y) memset((x),(y),sizeof(x))
#define pb push_back
#define mod 1000000007

char s[30][30];
bool vis[30];

int main()
{
	freopen("C:\\tmpcode\\gcj\\2017\\r1a\\a\\A-large.in", "r", stdin);
	freopen("C:\\tmpcode\\gcj\\2017\\r1a\\a\\mylargeoutput.txt", "w", stdout);
	int T;scanf("%d",&T);
	rep(ii,1,T)
	{
		int n,m;
		scanf("%d%d",&n,&m);
		rep(i,1,n)scanf("%s",s[i]+1);
		printf("Case #%d:\n",ii);
		// clr(vis,0);
		// rep(i,1,n)rep(j,1,m)if(s[i][j]!='?' && !vis[s[i][j]-'A'])
		// {
			// int le=m,ri=1,up=n,dn=1;
			// rep(k,1,n)rep(l,1,m)if(s[k][l]==s[i][j])
			// {
				// le=min(le,l);
				// ri=max(ri,l);
				// up=min(up,k);
				// dn=max(dn,k);
			// }
			// rep(k,up,dn)rep(l,le,ri)s[k][l]=s[i][j];
			// vis[s[i][j]-'A']=1;
		// }
		clr(vis,0);
		rep(i,1,n)rep(j,1,m)if(s[i][j]!='?' && !vis[s[i][j]-'A'])
		{
			int le=j,ri=j,up=i,dn=i;
			vis[s[i][j]-'A']=1;
			while(up>1)
			{
				bool ok=1;
				rep(k,le,ri)if(s[up-1][k]!='?')ok=0;
				if(!ok)break;
				up--;
				rep(k,le,ri)s[up][k]=s[i][j];
			}
			while(dn<n)
			{
				bool ok=1;
				rep(k,le,ri)if(s[dn+1][k]!='?')ok=0;
				if(!ok)break;
				dn++;
				rep(k,le,ri)s[dn][k]=s[i][j];
			}
		}
		clr(vis,0);
		rep(i,1,n)rep(j,1,m)if(s[i][j]!='?' && !vis[s[i][j]-'A'])
		{
			int le=j,ri=j,up=i,dn=i;
			while(up>1 && s[up-1][j]==s[i][j])up--;
			while(dn<n && s[dn+1][j]==s[i][j])dn++;
			vis[s[i][j]-'A']=1;
			while(le>1)
			{
				bool ok=1;
				rep(k,up,dn)if(s[k][le-1]!='?')ok=0;
				if(!ok)break;
				le--;
				rep(k,up,dn)s[k][le]=s[i][j];
			}
			while(ri<m)
			{
				bool ok=1;
				rep(k,up,dn)if(s[k][ri+1]!='?')ok=0;
				if(!ok)break;
				ri++;
				rep(k,up,dn)s[k][ri]=s[i][j];
			}
		}
		rep(i,1,n)puts(s[i]+1);
	}
	
	
	return 0;
}
