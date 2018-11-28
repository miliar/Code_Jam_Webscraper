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

    freopen ("Cin.txt","r",stdin);
    freopen ("Cout.txt","w",stdout);
	int t;
	cin>>t;
	for(auto i = 1; i <= t; i++)
	{
		int n,k;
		cin>>n>>k;
		priority_queue<int> pq;
		pq.push(n);
		for(int j=0;j<k-1;j++)
		{
			
			int temp=pq.top();
			pq.pop();
			if(temp%2==0)
			{
				pq.push(temp/2);
				pq.push(temp/2 - 1);
			}
			else
			{
				pq.push(temp/2);
				pq.push(temp/2);
			}
		}
		int ret=pq.top();
		if(ret%2==0)
		{
			cout<<"Case #"<<i<<": "<<ret/2<<" "<<ret/2-1<<endl;
		}
		else
		{
			cout<<"Case #"<<i<<": "<<ret/2<<" "<<ret/2<<endl;
		}
	}
return 0;
}
