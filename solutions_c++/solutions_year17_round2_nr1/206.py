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
  i64 D, N, i;
  cin >> D >> N;
  vi K(N), S(N);
  REP(0, N, i) {
    cin >> K[i] >> S[i];
  }

  i64 max_idx = 0;
  REP(0, N, i) {
    //if( (D - K[max_idx]) / S[max_idx] > (D - K[i]) / S[i] ) {
    if( (D - K[max_idx]) * S[i] < (D - K[i]) * S[max_idx] ) {
      max_idx = i;
    }
  }

  double max_t = double(D - K[max_idx]) / double(S[max_idx]);
  double ans = D / max_t;

  printf("%.10f\n", ans);
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

