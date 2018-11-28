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
  ios_base::sync_with_stdio(false);  cin.tie(0) ;
  
  int t ; cin>>t ;
  int cases = 1 ;
  while (t--)
  {
	  
	  int n , m ; cin>>n>>m ;
	  char s[n][m] ;
	  for (int i=0;i<n;i++)
	  {
		  for (int j=0;j<m;j++)
		  {
			  cin>>s[i][j] ;
		  }
	  }
	  bool take[n][m] ; mset(take,true) ;
	  for (int i=0;i<n;i++)
	  {
		  for (int j=0;j<m;j++)
		  {
			  if (s[i][j] != '?' and take[i][j])
			  {
				  //left - up 
				  int x1 = i, y1 = j ;
				 // float slope ;
				 bool found = false ;
				  for (int i1 = 0 ;i1<=i;i1++)
				  {
					  for (int j1=0;j1<=j;j1++)
					  {
						//  if (i1 == i and j1 == j) continue ;
							if (s[i1][j1] == '?')
							{
								found = true ;
								x1 = i1 ; y1 = j1 ; break ;
							}
					  }
					  if (found) break ;
				  }
				  x1 = min(x1,i) ; y1 = min(y1,j) ;
				  for (int i1 = i ; i1 >= x1 ; i1 --)
				  {
					  for (int j1 = j ; j1 >= y1 ; j1 --)
					  {
						  if (s[i1][j1] == '?') s[i1][j1] = s[i][j] ;
						  take[i1][j1] = false ;
					  }
				  }
		//	cerr<<i<<" "<<j<<" "<<x1<<" "<<y1<<endl ;
				  //extend right
				  int y2 = m-1;
				//  bool found ;
				  for (int j1 = j + 1 ;j1 < m ; j1++)
				  {
					  found = false ;
					  for (int i1 = x1 ; i1 <= i ;i1++)
					  {
						  if (s[i1][j1] != '?')
						  {
							  y2 = j1 - 1 ; 
							  found = true ; break ;
						  }
					  }
					  if (found) break ;
					  for (int i1= x1; i1 <= i ; i1++)
					  {
						  s[i1][j1] = s[i][j] ;
						  take[i1][j1] = false;
					  }
				  }
		//  cerr<<i<<" "<<j<<" "<<y2<<endl ;
				  //x1,y1 ---> i,y2 
				  //extend row
				//  cout<<i<<" "<<j<<" "<<x1<<" "<<y1<<" "<<y2<<endl ;
				  for (int i1 = i + 1; i1 < n ;i1++)
				  {
					  found = false ;
					  for (int j1 = y1 ; j1 <= y2 ; j1++)
					  {
						  if (s[i1][j1] != '?')
						  {
							  found = true ; break ;
						  }
					  }
					  if (found) break ;
					  for (int j1 = y1 ; j1 <= y2 ; j1++)
					  {
						  s[i1][j1] = s[i][j] ;
						  take[i1][j1] = false ;
					  }
				  }
				  
			  }
		  }
	  }
	//  cerr<<endl ;
	  cout<<"Case #"<<cases++<<": \n" ;
	  for (int i=0;i<n;i++)
	  {
		  for (int j=0;j<m;j++)
		  {
			  cout<<s[i][j] ;
		  }
		  cout<<"\n" ;
	  }

  }

   return 0 ;
}
