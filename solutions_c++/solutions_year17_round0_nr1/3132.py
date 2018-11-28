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

char s[1000+10];
int tc, c, t, k, l;

int main() {
  ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);

  scanf("%d",&tc);

  rep(r,1,tc+1){
	  scanf("%s %d",&s,&k);
	  t = 0;
	  c = 0;
	  l = strlen(s);
	  rep(i,0,l) if(s[i] == '-') t++;
//	  debug(l-k+1);
	  rep(i,0,l-k+1){
		  if(s[i] == '-'){
			  c++;
			  rep(j,i,i+k){
				  if(s[j] == '-'){
					  s[j] = '+';
					  t--;
				  }else{
					  s[j] = '-';
					  t++;
				  }
			  }
			  if(t == 0) break;
		  }
	  }
	  if(t == 0) printf("Case #%d: %d\n",r,c);
	  else printf("Case #%d: IMPOSSIBLE\n",r);
  }
  
  return 0;
}
