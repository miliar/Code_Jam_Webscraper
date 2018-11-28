#include<vector>
#include<list>
#include<map>
#include<set>
#include<deque>
#include<queue>
#include<stack>
#include<bitset>
#include<algorithm>
#include<functional>
#include<numeric>
#include<utility>
#include<iostream>
#include<sstream>
#include<iomanip>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<string>
#include<cstring>
#include<cstdio>
#include<ctime>
#include<climits>
#include<complex>
#include<cassert>
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define sz(x) (int)((x).size())
#define all(x) x.begin(),x.end()
#define clr(x) memset((x),0,sizeof(x))
#define cdp(x) memset((x),-1,sizeof(x))
#define rep(i,n) for (i=0;i<n;i++)
#define Rep(i,a,b) for (i=a;i<=b;i++)
#define ff(i,x) for (i=start[x];i!=-1;i=a[i].next)
#define foreach(e,x) for(__typeof(x.begin()) e=x.begin();e!=x.end();++e)
using namespace std;
const double eps=1e-8;
const double pi=acos(-1.0);
int dblcmp(double d){if (fabs(d)<eps)return 0;return d>eps?1:-1;}
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef vector<pii> vpi;
char s[1111];
int d;
int main()
{
	freopen("C:\\competition\\gcj\\A-large (3).in","r",stdin);
	freopen("C:\\competition\\gcj\\Aout.out","w",stdout);
	int i,j,k,cas,cc=0;
	scanf("%d",&cas);
	while (cas--)
	{
		scanf("%s%d",s,&d);
		int l=strlen(s),ans=0;
		for (i=0;i+d<=l;i++)
		{
			if (s[i]=='-')
			{
				ans++;
				for (j=i;j<i+d;j++)
				{
					if (s[j]=='-')s[j]='+';
					else s[j]='-';
				}
			}
		}
		for (i=0;i<l;i++)
		{
			if (s[i]=='-')ans=-1;
		}
		if (ans==-1)
		{
			printf("Case #%d: IMPOSSIBLE\n",++cc);
		}
		else 
		{
			printf("Case #%d: %d\n",++cc,ans);
		}
	}
	return 0;
}