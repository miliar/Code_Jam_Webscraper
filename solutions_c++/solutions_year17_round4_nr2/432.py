//#include <bits/stdc++.h>
#include <stdio.h>
#include <iostream>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <limits.h>
#include <algorithm>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <bitset>
#include <string>
#include <time.h>
using namespace std;
long double esp=1e-11;
//#pragma comment(linker, "/STACK:1024000000,1024000000")
#define fi first
#define se second
#define all(a) (a).begin(),(a).end()
#define cle(a) while(!a.empty())a.pop()
#define mem(p,c) memset(p,c,sizeof(p))
#define mp(A, B) make_pair(A, B)
#define pb push_back
#define lson l , m , rt << 1
#define rson m + 1 , r , rt << 1 | 1
typedef long long int LL;
const long double PI = acos((long double)-1);
const LL INF=0x3f3f3f3f3f3f3f3fll;
const int MOD =1004535809ll;
const int maxn=1000100;
int a[4],f[1100],g[1100];
int n,c,m;
bool check(int k)
{
	int la=0,ans=0;
	for(int x=n;x>=1;x--)
		if(f[x]>k)
		{
			ans+=f[x]-k;
			la+=f[x]-k;
		}
		else
		{
			if(k-f[x]<la)
				la-=k-f[x];
			else
				la=0;
		}
	if(!la)return true;
	else return false;
}
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    //::iterator iter;                  %I64d
    //for(int x=1;x<=n;x++)
    //for(int y=1;y<=n;y++)
    //scanf("%d",&a);
    //printf("%d\n",ans);
    int T;
    scanf("%d",&T);
    for(int gg=1;gg<=T;gg++)
	{
		scanf("%d%d%d",&n,&c,&m);
		mem(f,0);
		mem(g,0);
		for(int x=1;x<=m;x++)
		{
			int p,b;
			scanf("%d%d",&p,&b);
			f[p]++;
			g[b]++;
		}
		int l=f[1],r=m;
		for(int x=1;x<=c;x++)l=max(l,g[x]);
		while(l<r)
		{
			int mid=(l+r)/2;
			if(check(mid))r=mid;
			else l=mid+1;
		}
		int ans=r;
		int time=0;
		for(int x=1;x<=n;x++)
			if(f[x]>ans)
				time+=f[x]-ans;
		printf("Case #%d: %d %d\n",gg,ans,time);
	}
    return 0;
}
