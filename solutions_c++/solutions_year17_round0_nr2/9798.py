#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <climits>
#include <bitset>
#include <cmath>
#include <cstring>
#include <assert.h>
using namespace std;
#define all(M) (M).begin(), (M).end()
#define vi vector<int>
#define vl vector<ll>
#define sort(v) sort(all(v))
#define fo(i,m,n) for(auto i = m ; i < n ; i++)
#define rep(i,n) fo(i,0,n)
#define f first
#define s second
#define pb push_back
#define mp make_pair
#define pqueue priority_queue<pll,vector<pll>, greater<pll>>
#define sz(s) s.size()
#define trace(a) {for(auto i:a) cout << i << ' '; cout << '\n';}
//#define set(a) memset(a,0,sizeof(a))
#define si(n) scanf("%d",&n)
#define pi(n) printf("%d\n",n)
#define sl(n) scanf("%lld",&n)
#define pl(n) printf("%lld\n",n)
#define smi(n,m) scanf("%d%d",&n,&m)
#define pmi(n,m) printf("%d %d\n",n,m)
#define sml(n,m) scanf("%lld%lld",&n,&m)
#define pml(n,m) printf("%lld %lld\n",n,m)
typedef long long int ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

ll convert(ll n)
{
	vl a,b;
	while(n)
		a.pb(n%10), n/=10;
	n = sz(a);
	if(count(all(a), 0) + count(all(a), 1) == n)
		for(int i = n-2 ; i >= 0 && (a[i] == 1 || a[i] == 0) ; i--)
			a[i] = 0;
	for(int i = n-1 ; i >= 0 ; i--)
		if(a[i] > a[i-1] && i > 0)
		{
			b.pb(a[i]-1);
			while(i > 0)
				b.pb(9), i--;
			break;
		}
		else b.pb(a[i]);
	reverse(all(b));
	n = sz(b);
	ll num = 0;
	for(int i = n-1 ; i >= 0 ; i--)
		num = 10*num+b[i];
	return num;
}

int main()
{
	int t;
	si(t);
	fo(tt,1,t+1)
	{
		ll n;
		sl(n);
		cout << "Case #" << tt << ": " << convert(n) << '\n';
	}
	return 0;
}
