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

int t;

int main() {
  ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);

  cin>>t;
  rep(casos,1,t+1){
	  int n, r, o, y, g, b, v;
	  map<int,int> mp;
	  cin>>n>>r>>o>>y>>g>>b>>v;
	  mp[0] += r;
	  mp[1] += o;
	  mp[2] += y;
	  mp[3] += g;
	  mp[4] += b;
	  mp[5] += v;

	  int f;
	  if(r > 0){
		  f = 0;
	  }else{
		  if(o > 0){
			  f = 1;
		  }else{
			  if(y > 0){
				  f = 2;
			  }else{
				  if(g > 0){
					  f = 3;
				  }else{
					  if(b >0){
						  f = 4;
					  }else{
						  if(v >0){
							  f = 5;
						  }
					  }
				  }
			  }
		  }
	  }

	  mp[f]--;
	  //	  mp[f]++;
	  int beg = f;

	  bool flag = 0;
	  vi sol;
	  sol.push_back(f);

	  int x, z;
//	  int pr = -1, pb = -1, py = -1;
//	  if(f == 0) pr = 0;
//	  if(f == 2) py = 0;
//	  if(f == 4) pb = 0;
	  
	  rep(i,1,n){
		  if(f == 0 || f == 2 || f == 4){
			  
			  int a, b;
			  if(f == 0){
				  x = 3; y = 2; z = 4;
//				  a = py;
//				  b = pb;
			  }
			  if(f == 2){
				  x = 5; y = 0; z = 4;
//				  a = pr;
//				  b = pb;
			  }
			  if(f == 4){
				  x = 1; y = 0; z = 2;
//				  a = pr;
//				  b = py;
			  }

			  if(mp[x] == mp[y] && mp[y] == mp[z] && mp[z] == 0){
				  flag = 1;
				  break;
			  }
			  if(mp[x] > 0){
				  mp[x]--;
				  f = x;
//				  if(f == 0) pr = i;
//				  if(f == 2) py = i;
//				  if(f == 4) pb = i;
				  sol.push_back(f);
			  }else{
				  if(mp[y] > mp[z] /*|| a < b*/ || (mp[y] == mp[z] && y == beg)){
//					  debug(a);debug(b);
					  mp[y]--;
					  f = y;
//					  if(f == 0) pr = i;
//					  if(f == 2) py = i;
//					  if(f == 4) pb = i;
					  
					  sol.push_back(f);
				  }else{
					  mp[z]--;
					  f = z;
//					  if(f == 0) pr = i;
//					  if(f == 2) py = i;
//					  if(f == 4) pb = i;
					  sol.push_back(f);
				  }
			  }
		  }else{
			  if(f == 3) x = 0;
			  if(f == 1) x = 4;
			  if(f == 5) x = 2;
			  if(mp[x] == 0){
				  flag = 1; break;
			  }else{
				  mp[x]--;
				  f = x;
//				  if(f == 0) pr = i;
//				  if(f == 2) py = i;
//				  if(f == 4) pb = i;
				  sol.push_back(f);
			  }
		  }
	  }

	  if(f == 0){
		  if(!(beg == 2 || beg == 3 || beg == 4) ) flag = 1;
	  }
	  if(f == 2){
		  if(! (beg == 0 || beg == 4 || beg == 5) ) flag = 1; 
	  }
	  if(f == 4){
		  if(! (beg == 0 || beg == 1 || beg == 2) ) flag = 1;
	  }
	  if(f == 1){
		  if(beg != 4) flag = 1; 
	  }
	  if(f == 3){
		  if(beg != 0) flag = 1;
	  }
	  if(f == 5){
		  if(beg != 2) flag = 1;
	  }

//	  debugv(sol);
	  
	  cout<<"Case #"<<casos<<": ";
	  if(flag) cout<<"IMPOSSIBLE\n";
	  else{
		  rep(i,0,n){
			  if(sol[i] == 0) cout<<'R';
			  if(sol[i] == 1) cout<<'O';
			  if(sol[i] == 2) cout<<'Y';
			  if(sol[i] == 3) cout<<'G';
			  if(sol[i] == 4) cout<<'B';
			  if(sol[i] == 5) cout<<'V';
		  }
		  cout<<'\n';
	  }

  }
  
  return 0;
}
