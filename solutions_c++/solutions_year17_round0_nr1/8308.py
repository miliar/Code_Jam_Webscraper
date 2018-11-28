#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <list>
#include <cmath>
#include <iomanip>
#include <time.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define sz(a) (int)(a.size())
#define all(c) (c).begin(),(c).end()
#define F first
#define S second
#define si(n) scanf("%d",&n)
#define sll(n) scanf("%lld",&n)
#define REP(i,a,b) for(int i=a;i<b;i++)
#define MOD 1000000007
#define endl '\n'
#define fast_io ios_base::sync_with_stdio(false);cin.tie(NULL)
typedef long long int ll;
ll powmod(ll a,ll b)
{
    if(b==0)return 1;
    ll x=powmod(a,b/2);
    ll y=(x*x)%MOD;
    if(b%2)
    return (a*y)%MOD;
    return y%MOD;
}


int main() {

    freopen ("Ain.txt","r",stdin);
    freopen ("Aout.txt","w",stdout);
    int t;
	cin>>t;
	for(auto tc = 1; tc <= t; tc++)
	{
		string s;
		int k;
		cin>>s>>k;
		int l=s.size();
		int ans=0;
		for(int i=0;i<=(l-k);i++)
		{
			if(s[i]=='-')
			{
				for(int j=i;j<(i+k);j++)
				{
					if(s[j]=='-')
						s[j]='+';
					else
						s[j]='-';
				}
				ans++;

			}
		}
		int fl=0;
		for(int i=0;i<l;i++)
		{
			if(s[i]=='-')
			{
				fl=1;
				break;
			}
		}
		if(fl==0)
		{
			cout<<"Case #"<<tc<<": "<<ans<<endl;
		}
		else
		{
			cout<<"Case #"<<tc<<": IMPOSSIBLE"<<endl;
		}




	}
	return 0;
}