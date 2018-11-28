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
#define eps 1e-8
const int maxn=100;
int n,m,a[maxn],b[maxn][maxn],f[maxn];


int main()
{
	freopen("C:\\tmpcode\\gcj\\2017\\r1a\\b\\B-large.in", "r", stdin);
	freopen("C:\\tmpcode\\gcj\\2017\\r1a\\b\\mylargeoutput.txt", "w", stdout);
	int T;scanf("%d",&T);
	rep(ii,1,T)
	{
		scanf("%d%d",&n,&m);
		rep(i,1,n)scanf("%d",&a[i]);
		rep(i,1,n)
		{
			rep(j,1,m)scanf("%d",&b[i][j]);
			sort(b[i]+1,b[i]+m+1);
			f[i]=1;
		}
		LL cur=1;
		bool ok=1;
		int ans=0;
		while(ok)
		{
			bool flag=1;
			rep(i,1,n)
			{
				while(f[i]<=m && cur*a[i]*0.9 > b[i][f[i]]+eps)
				{
					f[i]++;
				}
				if(f[i]>m)
				{
					ok=0;
					flag=0;
					break;
				}
				if(cur*a[i]*1.1+eps < b[i][f[i]])
				{
					cur++;
					flag=0;
					break;
				}
			}
			if(flag)
			{
				ans++;
				rep(j,1,n)f[j]++;
			}
		}
		
		
		
		printf("Case #%d: %d\n",ii,ans);
	}
	
	
	return 0;
}
