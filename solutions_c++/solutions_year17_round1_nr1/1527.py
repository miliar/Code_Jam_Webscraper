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


int main()
{
	freopen ("Cin.txt","r",stdin);
    freopen ("Cout.txt","w",stdout);
	int t;
	cin>>t;
	for(int i = 0; i<t; i++)
	{
		int r, c;
		cin>>r>>c;
		char a[30][30];
		for(int j = 0; j<r; j++)
			for(int k = 0; k<c; k++)
				cin>>a[j][k];
		for(int j = 0; j<r; j++)
		{
			for(int k = 0; k<c; k++)
			{
				if(a[j][k]!='?')
				{
					for(int p = k + 1; p<c; p++)
						if(a[j][p] == '?')
							a[j][p] = a[j][k];
						else
							break;
					for(int p = k - 1; p>=0; p--)
						if(a[j][p] == '?')
							a[j][p] = a[j][k];
						else
							break;
				}
			}
		}
		for(int j = 0; j<(r - 1); j++)
		{
			for(int k = 0; k<c; k++)
				if(a[j][k] != '?' && a[j + 1][k] == '?')
					a[j + 1][k] = a[j][k];
		}
		for(int j = r - 1; j>0; j--)
		{
			for(int k = 0; k<c; k++)
				if(a[j][k] != '?' && a[j - 1][k] == '?')
					a[j - 1][k] = a[j][k];
		}
		cout<<"Case #"<<i + 1<<":"<<endl;
		for(int j = 0; j<r; j++)
		{
			for(int k = 0; k<c; k++)
				cout<<a[j][k];
			cout<<endl;
		}
	}
}