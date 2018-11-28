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

bool compare(pll x, pll y)
{
	return (x.fi*x.se > y.fi*y.se) ;
}

bool compare2(ll x, ll y)
{
	return (x > y) ;	
}

int n , k ; 
vector<pll> v ;



int main()
{
	#ifdef DHEER
  freopen("inp.txt","r",stdin) ;
  freopen("out.txt","w",stdout) ;
  #endif
  ios_base::sync_with_stdio(false);  cin.tie(0) ;
  
  int t ; inp(t) ;
  const double pi = acos(-1) ;
  int cases = 1 ;
  while (t--)
  {
	  inp2(n,k) ;
	  
	  ll r, h ;
	  vector<ll> v2 ;
	  v.clear() ;
	  for (int i=0;i<n;i++)
	  {
		  inpl2(r,h) ;
		  v.pb(mp(r,h)) ;
		  v2.pb(r) ;
	  }
	  
	  sort(all(v),compare) ;
	  sort(all(v2),compare2) ;
	  ll tot = 0 ;
	  for (auto it : v2)
	  {
		  int c = 0 ;
		  bool f = false ;
		  ll temp = it*it ;
		  for (int i=0;i<n;i++)
		  {
			  r = v[i].fi ; h = v[i].se ;
			  if (c==k-1 and f == false)
			  {
				  if (r==it)
				  {
					  f = true ; c++ ;
					  temp += 2*r*h ; break ;
				  }else
				  {
					  continue ;
				  }
			  }
			  if (r < it)
			  {
				  temp += 2*r*h ; c++;
			  }else if (r==it)
			  {
				  f = true ;
				  temp += 2*r*h ;
				  c++ ;
			  }
			  if (c==k) break ;
		  }
		  if (c==k and f)
		  {
			  tot = max(tot,temp) ;
		  }
	  }
	  
	  double ans = ((double) tot)*pi ;
	  
	  
	  cout<<"Case #"<<cases++<<": " ;
	  cout<<fixed<<setprecision(10)<<ans<<endl ;
  }

   return 0 ;
}
