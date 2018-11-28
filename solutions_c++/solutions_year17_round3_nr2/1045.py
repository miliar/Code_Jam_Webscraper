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


vector<pii> v1, v2 ;

bool compare(pii x, pii y)
{
	return (x.fi < y.fi ) ;	
}

int main()
{
	#ifdef DHEER
  freopen("inp.txt","r",stdin) ;
  freopen("out.txt","w",stdout) ;
  #endif
  ios_base::sync_with_stdio(false);  cin.tie(0) ;
  
  int t ; inp(t) ;
  int cases = 1 ;
  while (t--)
  {
	  
	  cout<<"Case #"<<cases++<<": " ;
	  int ac, aj ;
	  inp2(ac,aj) ;
	  v1.clear() ; v2.clear() ;
	  int x, y ;
	  for (int i=0;i<ac;i++)
	  {
		  inp2(x,y) ; v1.pb(mp(x,y)) ;
	  }
	  
	  for (int i=0;i<aj;i++)
	  {
		  inp2(x,y) ; v2.pb(mp(x,y)) ;
	  }
	  
	  sort(all(v1),compare) ;
	  sort(all(v2),compare) ;
	  int ans ; 
	  if (ac + aj == 1)
	  {
		  ans = 2 ;
	  }else
	  {
		  if (ac == 0 || aj == 0)
		  {
			  if (ac == 2)
			  {
				  int diff = v1[1].se - v1[0].fi ;
				  int diff2 = v1[0].se + 1440 - v1[1].fi ;
				  if (diff <= 720 || diff2 <= 720) ans = 2 ;
				  else ans = 4 ;
			  }else
			  {
				  int diff = v2[1].se - v2[0].fi ;
				  int diff2 = v2[0].se + 1440 - v2[1].fi ;
				  if (diff <= 720 || diff2 <= 720) ans = 2 ;
				  else ans = 4 ;	
			  }
		  }else
		  {
			  ans = 2 ;
		  }
	  }
	  cout<<ans<<endl ;
  }

   return 0 ;
}
