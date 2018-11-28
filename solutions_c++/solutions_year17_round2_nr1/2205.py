#include <bits/stdc++.h>
#include <assert.h>
#define MP make_pair
#define PB push_back
#define forn(i, a, b) for(int i =(a); i <=(b); ++i)
#define forr(i, a, b) for(int i = (a); i >= (b); --i)
#define VAR(v, i) __typeof(i) v=(i)
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
#define FOREACH(i, v) for (__typeof(v.begin()) i = v.begin(); i != v.end(); i++)
#define BACEACH(i, v) for (__typeof(v.rbegin()) i = v.rbegin(); i != v.rend(); i++)
#define debug(x) {cerr <<#x <<" = " <<x <<"\n"; }
#define debugv(x) {{cerr <<#x <<" = "; FOREACH(itt, (x)) cerr <<*itt <<", "; cerr <<"\n"; }}
#define debuga(x,n) {{cerr <<#x <<" = "; rep(i,0,n) cerr<<x[i]<<", "; cerr <<"\n";}}
#define make(type, x) type x; cin>>x;
#define make2(type, x, y) type x, y; cin>>x>>y;
#define make3(type, x, y, z) type x, y, z; cin>>x>>y>>z;
#define SSTR( x ) dynamic_cast< std::ostringstream & > (( std::ostringstream() << std::dec << x )).str()
#define F first
#define S second
#define EPS 1e-9
#define rep(i,a,b) for(int i=(a);i<(b);i++)

using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

template<class C> void mini(C&a4, C b4){a4=min(a4, b4); }
template<class C> void maxi(C&a4, C b4){a4=max(a4, b4); }
template<class T1, class T2>
ostream& operator<< (ostream &out, pair<T1, T2> pair) { return out << "(" << pair.first << ", " << pair.second << ")";}

const int maxn = 1000+10;
int k[maxn], s[maxn];
int n, t;
long double D;

bool f(long double x){

	long double target = D/x;
//	debug(target);
	
	rep(i,0,n){
		long double v= target * s[i] + k[i];
		if(v < D) return false;
	}
	return true;
}

int main() {
  ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);

  cin>>t;
  rep(r,1,t+1){
	  cin>>D>>n;
	  rep(i,0,n){
		  cin>>k[i]>>s[i];
	  }

	  long double hi = 100000000000000000, lo = 0, mid = 0, ans;
	  rep(i,0,10000){
		  mid = (hi+lo)/2.0;
		  if(f(mid)){
			  lo = mid;
			  ans = mid;
		  }else{
			  hi = mid;
		  }
	  }

	  cout<<"Case #"<<r<<": ";
	  cout<<fixed<<setprecision(6)<<ans<<'\n';
  }
  
  return 0;
}
