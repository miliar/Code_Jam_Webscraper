#include <bits/stdc++.h>
#include <sstream>
using namespace std;
#define fastio ios_base::sync_with_stdio(0);cin.tie(0);
#define clr(a,v) memset(a, v, sizeof(a))
#define trace(x) cerr << #x << ": " << x << '\n'
#define trace2(x,y) cerr << #x << ": " << x << " | " << #y << ": " << y << '\n';
#define trace3(x,y,z) cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << '\n';
#define all(v) (v).begin(),(v).end()
#define pb push_back
#define sz(v) ((int)v.size())
#define REP(i,x,y) for(long long (i)=(x);(i)<(y);(i)++)
#define RREP(i,x,y) for(long long (i)=(x);(i)>=(y);(i)--)
#define REPIT(it,A) for(typeof(A.begin()) it = (A.begin()); it!=A.end();it++)
#define mp make_pair
#define mt(x,y,z) mp((x),mp((y),(z)))
#define fst first
#define snd second
#define ones(x) __builtin_popcountll(x)
#define gcd __gcd
#define MOD 1000000007
#define oo 1e8
#define itm1 fst
#define EPS 1e-3
#define itm2 snd.fst
#define itm3 snd.snd
typedef unsigned long long ll;
typedef pair<ll,ll> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<ll> vll;
typedef pair<ll,ii> tri;
typedef vector<tri> vt;

int check ( string s ) { 
	int ans = -1 ; 
	for ( int i = 1 ; i < sz(s) ; ++i){
		if( s[i-1] -'0' > s[i] -'0' ) {
			ans = i ;
			break ; 
		} 
	}
return ans ; 
}

int main(){
	int t ; cin >> t ; 
	string s ; 
	int p , lp , ans ; 
	char tmp ; 
	for( int w = 0 ; w < t ; w++){
		ans = 0 ;  
		cin >> s ; 
		p = check(s) ;
		if( p == -1 ) {
			cout<< "Case #" << w+1 <<": " << s << endl  ;	
		}
		else {	
			tmp = s[p-1] ; 
			lp = - 1 ; 
			for( int i = p-1 ; i >=0 ; --i){
				if(s[i] != tmp) {
					lp = i + 1; 
					break ; 
				}
			}
			cout<< "Case #" << w+1 << ": " ; 
			if( lp == - 1 ){
				if(s[0] > '1') cout << s[0]-'1' ;
				for( int i = 1 ; i < sz(s) ; ++i) cout << "9" ;
				cout << endl ; 
			}
			
			else{
				for( int i = 0 ; i < lp ; ++i){
					cout << s[i] ; 
				}
				if(lp != 0 || s[lp] != 1) cout << s[lp]-'1';
				for ( int i = lp+1 ; i < sz(s) ; ++i) cout <<"9"; 
				cout << endl ;
			} 
		}
	}
return 0 ; 
}
