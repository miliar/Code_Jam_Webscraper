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
  int t ; inp(t) ; int cases = 1 ;
  while (t--)
  {
	  int n, k ; inp2(n,k) ;
	  priority_queue<int> q ;
	  
	  q.push(n) ;
	  int f ;
	  int count = 0 ;
	  int l, r ;
	  
	  while (!q.empty())
	  {
		  f = q.top() ; q.pop() ;
		  l = (f-1) / 2 ; r = f/2 ;
		  q.push(l) ; q.push(r) ;
		  count++ ;
		  if (count == k || (l==0 and r==0)) 
		  {
			  cout<<"Case #"<<cases++<<": "<<r<<" "<<l<<endl ; break ;
		  }
	  }
	  
  }
  
   return 0 ;
}
