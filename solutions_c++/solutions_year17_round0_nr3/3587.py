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

int main(){
  cin.tie(0);
  ios_base::sync_with_stdio(false);

  int T; cin >> T;
  FOR(t_,1,T+1){
	LL N, K;
	cin >> N >> K;

	map<LL,LL> m;
	set<LL> s;
	m[N] = 1;
	s.insert(N);
	LL ans_l = -100;
	while(K > 0){
	  LL l = *(--end(s));
	  s.erase(l);
	  LL l2 = (l-1) / 2;
	  if(l2 > 0){
		m[l2] += m[l];
		s.insert(l2);
	  }
	  if(l-l2-1 > 0){
		m[l-l2-1] += m[l];
		s.insert(l-l2-1);
	  }
	  K -= m[l];
	  ans_l = l;
	}
	LL l2 = (ans_l - 1) / 2;
	PLL ans(ans_l-l2-1, l2);
	cout << "Case #" << t_ << ": " << ans.FF << " " << ans.SS << endl;
  }

  return 0;
}
