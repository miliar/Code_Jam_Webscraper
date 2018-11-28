#include <bits/stdc++.h>
using namespace std;

using VI = vector<int>;
using VVI = vector<VI>;
using PII = pair<int, int>;
using LL = long long;
using VL = vector<LL>;
using VVL = vector<VL>;
using PLL = pair<LL, LL>;
using VS = vector<string>;

#define ALL(a)  begin((a)),end((a))
#define RALL(a) (a).rbegin(), (a).rend()
#define PB push_back
#define EB emplace_back
#define MP make_pair
#define SZ(a) int((a).size())
#define SORT(c) sort(ALL((c)))
#define RSORT(c) sort(RALL((c)))
#define UNIQ(c) (c).erase(unique(ALL((c))), end((c)))

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)

#define FF first
#define SS second
template<class S, class T>
istream& operator>>(istream& is, pair<S,T>& p){
  return is >> p.FF >> p.SS;
}
template<class S, class T>
ostream& operator<<(ostream& os, const pair<S,T>& p){
  return os << p.FF << " " << p.SS;
}
template<class T>
void maxi(T& x, T y){
  if(x < y) x = y;
}
template<class T>
void mini(T& x, T y){
  if(x > y) x = y;
}


const double EPS = 1e-10;
const double PI  = acos(-1.0);
const LL MOD = 1e9+7;

// 0 1 2 3 4 5
// R,O,Y,G,B,V;
const int R = 0;
const int O = 1;
const int Y = 2;
const int G = 3;
const int B = 4;
const int V = 5;
bool check(VI tmp, const string& s){
  int n = SZ(s);
  string col = "ROYGBV";
  VI bit{1,3,2,6,4,5};
  VI ix(n);
  for(int i=0;i<n;++i){
	ix[i] = col.find(s[i]);
	tmp[ix[i]]--;
  }
  REP(i,6) if(tmp[i] != 0) return false;

  if(bit[ix[0]] & bit[ix.back()]) return false;
  REP(i,n-1)
	if(bit[ix[i]] & bit[ix[i+1]])
	  return false;
  return true;
}

int main(){
  cin.tie(0);
  ios_base::sync_with_stdio(false);

  int T; cin >> T;
  FOR(t,1,T+1){
	int N;
	string col = "ROYGBV";
	VI xs(6);
	cin>>N;
	REP(i,6) cin >> xs[i];
	VI orig = xs;

	{
	  int cnt = 0;
	  REP(i,6) if(xs[i]) ++cnt;
	  if(cnt == 2){
		string ans;
		if(xs[O] != 0 && xs[B] != 0 && xs[O] == xs[B]){
		  REP(i,xs[O]) ans += "OB";
		}
		if(xs[R] != 0 && xs[G] != 0 && xs[R] == xs[G]){
		  REP(i,xs[R]) ans += "RG";
		}
		if(xs[Y] != 0 && xs[V] != 0 && xs[Y] == xs[V]){
		  REP(i,xs[Y]) ans += "YV";
		}

		if(!ans.empty()){
		  cout << "Case #" << t << ": " << ans << endl;
		  continue;
		}
	  }
	}

	bool ok = true;
	ok = ok && (xs[O] == 0 || xs[O] + 1 <= xs[B]);
	ok = ok && (xs[G] == 0 || xs[G] + 1 <= xs[R]);
	ok = ok && (xs[V] == 0 || xs[V] + 1 <= xs[Y]);
	xs[R] -= xs[G];
	xs[Y] -= xs[V];
	xs[B] -= xs[O];
	int n = xs[R] + xs[Y] + xs[B];
	int mx = max(xs[R], max(xs[Y], xs[B]));
	ok = ok && ((n==xs[R]&&xs[R]==1)
				|| (n==xs[Y]&&xs[Y]==1)
				|| (n==xs[B]&&xs[B]==1)
				|| (mx <= n - mx));

	if(!ok || n <= 1){
	  cout << "Case #" << t << ": IMPOSSIBLE" << endl;
	}
	else{
	  string buf(n, '*');
	  int ix = -1;
	  REP(i,3) if(xs[i*2] == mx) ix = i;
	  
	  REP(i,3) if(i != ix && xs[i*2] > 0){
		buf[0] = col[i*2];
		xs[i*2]--;
		ix = i;
		break;
	  }
	  for(int i=1;i<n;++i){
		int mix = -1;
		REP(j,3){
		  if((mix == -1 || xs[mix*2] < xs[j*2]) && j != ix)
			mix = j;
		}
		buf[i] = col[mix*2];
		xs[mix*2]--;
		ix = mix;
	  }

	  string ans;
	  for(int i=0;i<n;++i){
		ans += buf[i];
		switch(buf[i]){
		case 'R':
		  REP(ii,xs[G])
			ans += "GR";
		  xs[G] = 0;
		  break;
		case 'Y':
		  REP(ii,xs[V])
			ans += "VY";
		  xs[V] = 0;
		  break;
		case 'B':
		  REP(ii,xs[O])
			ans += "OB";
		  xs[O] = 0;
		  break;
		}
	  }

	  if(!check(orig, ans)){
		REP(i,6) cout << orig[i] << " "; cout << endl;
		cout << ans << endl;
		return 1;
	  }

	  cout << "Case #" << t << ": " << ans << endl;
	}
  }

  return 0;
}
