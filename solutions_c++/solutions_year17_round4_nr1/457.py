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
int a[4];
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    //::iterator iter;                  %I64d
    //for(int x=1;x<=n;x++)
    //for(int y=1;y<=n;y++)
    //scanf("%d",&a);
    //printf("%d\n",ans);
    int T;
    scanf("%d",&T);
    for(int gg=1;gg<=T;gg++)
	{
		int n,p;
		scanf("%d%d",&n,&p);
		mem(a,0);
		for(int x=1;x<=n;x++)
		{
			int t;
			scanf("%d",&t);
			a[t%p]++;
		}
		int ans=0;
		if(p==2)
		{
			ans=a[0]+(a[1]+1)/2;
		}
		else if(p==3)
		{
			int s=min(a[1],a[2]);
			ans=a[0]+s;
			a[1]-=s;
			a[2]-=s;
			ans+=(a[1]+2)/3+(a[2]+2)/3;
		}
		else
		{
			ans=a[0];
			int s=min(a[1],a[3]);
			ans+=s;
			a[1]-=s;
			a[3]-=s;
			int t=(max(a[1],a[3])+1)/2;
			t+=a[2];
			ans+=(t+1)/2;
		}
		printf("Case #%d: %d\n",gg,ans);
	}
    return 0;
}
