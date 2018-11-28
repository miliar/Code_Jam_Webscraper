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

pair<ll,ll> get (ll n ){
	if(n&1) return mp(n/2,n/2) ; 
	else return mp(n/2-1,n/2) ;
}


int main(){
	int t ; cin >> t ; 
	ll n , k , find ;
	ii p ; 
	ll pos , c1 , c2 ; 
	ll a ; 
	ll aux1, aux2 ; 
	for( int w = 0 ; w < t ; w++){
		cout << "Case #"<< w + 1 << ": " ;
		find = 0 ;
		cin >> n >> k  ;
		pos = k ; 
		ll a = n ; 
		c1 = 1 ; 
		c2 = 0 ;	
		for( ; ; ) { 
			if( pos == 0 ) cout << "0 0"<< endl ;
			if( a == 0 ) break ; 
			//cout << a << " " << c1 << " " << c2 << endl ; 
			if( pos <= c1 ){
				p = get(a) ; 
				cout << p.snd << " " << p.fst << endl ; 
				break ;
			} 
			else if( pos <=c1 + c2 ){
				p = get(a-1) ;
				cout << p.snd << " " << p.fst << endl ; 
				break ; 
			}
			pos -= c1 + c2 ;
			if( a &1 ) {
				a = a/2 ; 
				aux1 = 2*c1 + c2 ; 
				aux2 = ((a==1) ? 0 : 1) * c2 ; 		
			}		
			else{
				a = a/2 ; 
				aux1 = c1 ; 
				aux2 = (2*c2+c1)*((a==1) ? 0 : 1) ;

			}
			c1 = aux1 ; 
			c2 = aux2 ; 
		}
	}
	
return 0 ; 
}
