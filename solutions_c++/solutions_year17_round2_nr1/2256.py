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

ll arr[1005][2] ;
ll d,n ; 

bool check(double x)
{
	
	for (int i=n-1;i>=0;i--)
	{
		if ((double) arr[i][1] >= x) continue ;
		double t1 = ((double) d) / x ;
		double t2 = ((double) d - (double) arr[i][0]) / ( (double) arr[i][1]) ;
		//cerr<<fixed<<setprecision(10)<<t1<<" "<<t2<<endl ;
		if (t1 < t2) return false ;
	}
	return true ;	
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
	  inpl2(d,n) ;
	  ll maxi = -1 ;
	  for (int i=0;i<n;i++)
	  {
		  inpl2(arr[i][0],arr[i][1]) ;
		  maxi = max(maxi,arr[i][1]) ;
	  }
	  
	  double l = 0.0 , r = 1000000000000000000.0 ;
	  double ans = 0.0 ;
	  for (int it = 1 ; it<=100;it++)
	  {
		  double mid = (l+r)/2.0 ;
		  if (check(mid))
		  {
			  l = mid ; ans = max(ans,mid) ;
		  }else
		  {
			  r = mid ;
		  }
	  }
	  cout<<"Case #"<<cases++<<": " ;
	  cout<<fixed<<setprecision(10)<<ans<<endl ;
  }
  
  
    	
   return 0 ;
}
