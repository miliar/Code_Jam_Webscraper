#include <bits/stdc++.h>
#define mp make_pair 
#define pb push_back 
#define fi first
#define se second
#define MOD 1000000007
#define DOMOD(d) if ((d) >= MOD) d %= MOD;
#define DONEGMOD(d) if ((d) < 0) d = ((d % MOD) + MOD) % MOD;
 
#define inp(a) scanf("%d", &a)
#define inp2(a,b) scanf("%d %d", &a, &b)
#define inp3(a,b,c) scanf("%d %d %d", &a, &b, &c)
#define inp4(a,b,c,d) scanf("%d %d %d %d", &a, &b, &c, &d)
 
#define inpl(a) scanf("%lld", &a)
#define inpl2(a,b) scanf("%lld %lld", &a, &b)
#define inpl3(a,b,c) scanf("%lld %lld %lld", &a, &b, &c)
#define inpl4(a,b,c,d) scanf("%lld %lld %lld %lld", &a, &b, &c, &d)
#define all(v) (v).begin(), (v).end()
#define rep(i,a,b) for (int i=a;i<b;i++)
#define mset(a,val) memset(a,val,sizeof(a))
#define printv(v) for (int i=0;i<(int) v.size(); i++) cout<<v[i]<<" " 
#define MAX 1000005
using namespace std ;
typedef long long int ll ;
typedef pair<int,int> pii ;
typedef pair<long long , long long > pll ;
typedef pair<int,pii> pipi ;
typedef pair<ll,pll> plpl ;
typedef pair<long long, int> pli ;
typedef pair<int,pair<int,string>> piis ;
typedef pair<ll,string> pls ;

ll find(ll n)
{
	vector<ll> v ;
	ll z = 0 ;
	ll temp = n ;
	bool ans2 = true ;
	while (n > 0)
	{
		v.pb(n%10) ; n/= 10 ; z++ ;
		if (n % 10 > 1) ans2 = false ;
	}
	
	reverse(all(v)) ;
	bool ans = true ;
	
	for (ll i=1;i<z;i++)
	{
		if (v[i] < v[i-1])
		{
			ans = false ; break ;
		}
	}
	if (ans) return temp ;
	ll ind = 0 ;
	for (ll i=1;i<z;i++)
	{
		if (v[i] >= v[i-1])
		{
			ind = i ;
		}else 
		{
			break ;
		}
	}
	
	
	if (ans2)
	{
		ll num = 0 ; 
		for (ll i=0;i<z-1;i++) num = num*10 + 9 ;
		return num ;
	}
	bool dd = false ;
	for (ll i=ind-1;i>=0;i--)
	{
		if (v[i] != v[ind])
		{
			ind = i+1 ; dd = true ; break ;
		}
	}
	if (!dd) ind = 0 ;
	
	string s ;
	ll num = 0 ;
	for (ll i=0;i<=ind;i++)
	{
		num = num*10LL + v[i] ;
	}
	num-- ;
	for (ll i = ind+1;i<z;i++) num = num*10 + 9 ;
	return num ;	
}


int main()
{
	#ifdef DHEER
  freopen("inp.txt","r",stdin) ;
  freopen("out.txt","w",stdout) ;
  #endif
  
  ll t ; cin>>t ;
  int cases = 1 ; 
  while (t--)
  {
	  ll n ; cin>>n ;
	  cout<<"Case #"<<cases++<<": "<<find(n)<<endl ;
  }
  
  
   return 0 ;
}
