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

bool compare(pair<char,int> x, pair<char,int> y)
{
	return (x.se<y.se) ;	
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
	  int n ; inp(n) ;
	  int x ;
	  vector<pair<char,int>> d;
	  for (int i=0;i<6;i++)
	  {
		 inp(x) ;
		 if (x == 0) continue ;
		 if (i==0) d.pb(mp('R',x)) ;
		 else if (i==2) d.pb(mp('Y',x)) ;
		 else if (i==4) d.pb(mp('B',x)) ;	
	  }
	  vector<char> v ;
	  sort(all(d),compare) ;
	  int c = 0 ;
	  bool found = false ;
	  for (auto it : d)
	  {
		  if (c==0)
		  {
			  for (int i=1;i<=it.se;i++) v.pb(it.fi) ;
		  }else
		  {
			  vector<char> v2 ;
			  int count = it.se ;
			  for (int i=0;i<(int) v.size();i++)
			  {
				  if (count > 0)
				  {
					  v2.pb(it.fi) ; v2.pb(v[i]) ; count-- ;
				  }else
				  {
					  v2.pb(v[i]) ;
				  }
			  }
			  v.clear() ;
			  while (count > 0)
			  {
				  v.pb(it.fi) ; count-- ;
			  }
			  
		  }
	  for (auto it : v) cerr<<it ; cerr<<endl ;
		  c++ ;
	  }
	  
	  for (int i=0;i<(int) v.size() - 1; i++)
	  {
		  if (v[i] == v[i+1]) 
		  {
			  found = true ; break ;
		  }
	  }
	  
	  if (v[0] == v[v.size()-1] and v.size() > 1) found = true ;
	   //cerr<<v[0]<<endl; 
	  cout<<"Case #"<<cases++<<": " ;
	  if (found) cout<<"IMPOSSIBLE" ;
	  else 
	  {
		  for (auto it : v) 
		  {
			 // if (it == '\n') continue ;
			  cout<<it ;
		  }
	  }
	  cout<<"\n" ;
  }
  
  
    	
   return 0 ;
}
