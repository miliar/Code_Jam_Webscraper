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



int main()
{
	#ifdef DHEER
  freopen("inp.txt","r",stdin) ;
  freopen("out.txt","w",stdout) ;
  #endif
  ios_base::sync_with_stdio(false) ; cin.tie(0) ;
  
  int t ; cin>>t ;
  int arr[1005] ;
  int cases = 1 ;
  while (t--)
  {
	  string s ; cin>>s ;
	  int k ; cin>> k ;
	  int z = (int) s.size() ;
	  for (int i=1;i<=z;i++) arr[i] = (s[i-1] == '+') ? 1 : 0 ;
	  int count = 0 ;
	  for (int i=1;i<=z-k+1;i++)
	  {
		  if (!arr[i])
		  {
			  for (int j=i;j<=i+k-1;j++)
			  {
				  arr[j] ^= 1 ;
			  }
			  count++ ;	
		  }
	  }
	  bool ans = true ;
	  for (int i=1;i<=z;i++) 
	  {
		  if (!arr[i])
		  {
			  ans = false ; break ;
		  }
	  }
	  cout<<"Case #"<<cases++<<": " ;
	  if (ans) cout<<count<<endl ;
	  else cout<<"IMPOSSIBLE"<<endl ;
  }
  
   return 0 ;
}
