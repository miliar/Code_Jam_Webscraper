
#include <bits/stdc++.h>
using namespace std;


typedef long long ll;
typedef vector <int> vi;
typedef pair< int ,int > pii;
typedef istringstream iss;
typedef ostringstream oss;
#define pb push_back
#define mps make_pair
#define f first
#define s second
#define sz size()
#define ln length()
#define rep(i,n) for(int i=0;i<n;i++)
#define fu(i,a,n) for(int i=a;i<=n;i++)
#define fd(i,n,a) for(int i=n;i>=a;i--)
#define all(a)  a.begin(),a.end() 
#define ESP (1e-9)

#define gi(n) scanf("%d",&n)
#define gl(n) cin >> n
#define pi(n) printf("%d",n)
#define pl(n) cout << n
#define ps printf(" ")
#define pn printf("\n")
#define dg(n,s); printf("%s %d",s,n)
#define imax numeric_limits<int>::max()
#define imin numeric_limits<int>::min()
#define lmax numeric_limits<ll>::max()
#define lmin numeric_limits<ll>::min()
typedef pair < int , int > pi ;
const ll inf = -1e15;  
const int md = 3e5 + 100 ;
const int mod = 1e9 + 7 ;
string s, s1;
int k; 
int t ;
map < int , int> dp; 
int solve (int i ) { 
	int res = -1 ;
    if ( i + 1 >= k )  {
			   	   for ( int j = i ; j > i - k ; j-- ){
			   	      if (s[j] == '+')	s[j] = '-';
			   	      else              s[j] = '+' ; 
				   }
				   for ( int j = i ; j >= i - k ; j-- ){
			   	      if (s[j] == '-' )  res = min ( res ,  1 + solve (j) ) ;  
				   }
				   for ( int j = i ; j > i - k ;j--){
				   	   if (s[j] == '+')	s[j] = '-';
			   	       else              s[j] = '+' ;  
				   }
				   
				  /* if ( j == -1 )  dp[i+1] = 1 ;
				   else  {
				   	   bool found = 1 ;
				   	   int tmp = k ;
				   	   if ( j + 1 - k < 0 )  found = 0 ; 
				   	   while ( tmp--) {
						 if ( dp[j] != '-' )   {
				   	       	       found = 0 ;
				   	       	       break; 
						  } 
						  j--;	
					   }
				   	   dp[i+1] =  dp[j+1] + 2 ; 
				   } 
			   }  */
		}
		return res ; 	   	
}	
int main () {
	
	 	freopen (  "B-small-attempt1.in" ,"r" ,stdin ) ;
    	freopen ( "out1.out" , "w", stdout );
	  cin >> t ;
	  for ( int test = 1 ; test <= t; test++){
	  	cout <<"Case #"<<test<<": ";
	  	cin >> s >> k ;
	  	s1 = s ; 
	  	int n1 = s.size () ; 
	  	dp.clear () ; 
	  	for ( int i = 0 ; i < n1 ; i++){
	  	    if ( s[i] == '-' ) {
	  	      dp[i] = solve (i) ;
		 }
		  else    dp[i+1] = dp[i] ; 
	   }
	   if (dp[n1] == -1 )  puts("IMPOSSIBLE") ;
	   else               cout << dp[n1] << "\n" ;
  }
	 return 0; 	
}
