
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
int t ;
ll n ; 
int main () {
	freopen (  "B-small-attempt2.in" ,"r" ,stdin ) ;
	freopen ( "out1.out" , "w", stdout );
	  cin >> t ;
	  for ( int test = 1 ; test <= t; test++){
	  	cout <<"Case #"<<test<<": ";
	  	  cin >> n ;
	      ll tmp = n ;
	      int cnt = 0 ;
		  ll val = 1 ;  
		  string str1 , str2, str3 ; 
		  bool f2 =  0 , f1 = 0 ; 
		  while ( tmp ) {
		  	    str1 =  char ( tmp %10 + '0') + str1 ; 
		  	    if ( tmp % 10 > 1 )  f2 = 1 ; 
		  	    if ( tmp % 10 == 0 )  f1 = 1 ; 
		  	  tmp /= 10 ;
		  	  cnt++; 
		  	  str2 = str2 + "1" ; 
		  	  val = 1ll * val * 10 ; 
		  }
		  for ( int i = 0 ; i < str2.size () - 1 ; i++){
		  	  str3 = "9" + str3 ; 
		  }
		  if ( !f2 && f1 && str2.size()  > 1 ){
		  	    cout << str3 << endl; 
		  	    continue ;
		  }
		 ///  cout << str1 << endl;
		  val = val / 10 ;
		  for ( int i = 0 ; i < str2.size () ; i++){
		  	 bool found = true ;  
		     while(str2[i] - '0' < 9 && found ) {
		  	     for ( int j = i ; j  < str2.size () ; j++){
		  	        str2[j]++ ; 
			     }
			  //   cout << str2 << endl;
			     if ( str2 > str1 ){
			     	 found = false ; 
			     	 for ( int j = i ; j < str2.size() ;j++){
			     	 	 str2[j]--; 
				}
			  }
		    }
		   
		  
	  }
	  cout << str2 << endl;
  }
	  return 0;
}
