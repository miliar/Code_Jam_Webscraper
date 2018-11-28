using namespace std;
#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <limits.h>
#include <vector>
#include <map>
#include <bitset>
#include <string>
#include <iterator>
#include <set>
#include <utility>
#include <queue>
#include <numeric>
#include <functional>
#include <ctype.h>
#include <stack>
#include <algorithm>
#include <cstdlib>
#define S(x) scanf("%d",&x)
#define S2(x,y) scanf("%d%d",&x,&y)
#define wl(n) while(n--)
#define ll long long
#define bitcnt(x) __builtin_popcount(x)
#define P(x) printf("%d\n",x)
#define PB push_back
#define MP make_pair
#define fl(i,n) for(i=0;i<n;i++)
#define fil(i,a,n) for(i=a;i<n;i++)
#define rev(i,a,n) for(i=n-1;i>=a;i--)
#define mem(a,i) memset(a,i,sizeof(a))
#define F first
#define S1 second
typedef pair<int,int> P;
vector<int> v1;
pair<int,int> p1;
#define MOD 1000000007
#define debug(x)  printf("####%d####\n",x);
#define nl printf("\n");
#define str string
int a[1234567];
string s;
int dp[1001];
ll pow1(ll x,ll y)
{
    if(y==0)
    return 1;
    ll temp= pow1(x,y/2)%MOD;
    if(y%2==0)
    return (temp*temp)%MOD;
    else
    return (((temp*temp)%MOD)*x)%MOD;
}
int main()
{
    //std::ios_base::sync_with_stdio(false);
    freopen("/home/meintoo/Downloads/A-small-attempt0.in","r",stdin);
    freopen("/home/meintoo/Downloads/o.txt","w",stdout);
    int t;
    int n,i,j,k,m,l;
    int l1=1;
    S(t);
    wl(t)
    {
    	cin>>s>>k;
    	int n=s.length();
    	int ans=0,f=0;
    	fl(i,n)
    	{
    		if(s[i]=='-')
    		{
    			if(i+k>n)
    				f=1;
    			else
    			{
    				fil(j,i,i+k)
    				{
    					if(s[j]=='-')
    						s[j]='+';
    					else
    						s[j]='-';
    				}
    				ans++;
    			}
    		}
    	}

    	if(f==1)
    		printf("Case #%d: IMPOSSIBLE\n",l1++ );
    	else
    		printf("Case #%d: %d\n",l1++,ans );
    }
    return 0;
}
