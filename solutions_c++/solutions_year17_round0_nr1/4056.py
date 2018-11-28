#include <cstdio>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>

using namespace std;
typedef long long i64;

typedef i64 int_t;

typedef pair<i64, i64> pi;

typedef vector<int_t> vi;
typedef vector<vi> vvi;
#define pb push_back
#define iter(T) T::iterator
#define sz(a) int((a).size())
#define all(c) (c).begin(), (c).end()
#define tr(c, i) for(auto i = (c).begin(); i != (c).end(); ++i)
#define present(c, x) ((c).find(x) != (c).end())
#define cpresent(c, x) (find(all(c), x) != (c).end())
#define REP(s, e, n)  for(n = (s); n < (e); ++n)

class Solver {
public:
  Solver() {}
  ~Solver() {}

  void solve();
};

void Solver::solve() {
  string S;
  i64 K, i, j;
  cin >> S >> K;

  i64 ans = 0;
  bool flag = true;
  REP(0, sz(S)-K+1, i) {
    if(S[i] == '-') {
      REP(0, K, j) {
	if(S[i+j] == '-') {
	  S[i+j] = '+';
	}
	else {
	  S[i+j] = '-';
	}
      }
      ++ans;
    }
  }
  REP(0, sz(S), i) {
    if(S[i] == '-') {
      flag = false;
    }
  }
  if(flag) {
    cout << ans << endl;
  }
  else {
    cout << "IMPOSSIBLE" << endl;
  }

}

int main(int argc, char *argv[]){
  i64 T;
  cin >> T;
  getchar();
  i64 t;

  REP(0, T, t) {
    Solver s;
    cout << "Case #" << t + 1 << ": ";
    s.solve();
  }

  return 0;
}

