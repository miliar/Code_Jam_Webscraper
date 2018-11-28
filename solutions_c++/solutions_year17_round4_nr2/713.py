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
  i64 N, C, M, i;
  cin >> N >> C >> M;

  vvi T(C, vi(N, 0));
  vi S(C, 0);
  REP(0, M, i) {
    i64 P, B;
    cin >> P >> B;
    --P;
    --B;
    T[B][P]++;
    S[B]++;
  }

  if(S[0] > S[1]) {
    swap(S[0], S[1]);
    swap(T[0], T[1]);
  }

  i64 ans1 = 0;
  i64 ans2 = max(S[1], T[0][0] + T[1][0]);
  REP(0, N, i) {
    if(T[0][i] + T[1][i] > ans2) {
      ans1 += (T[0][i] + T[1][i] - ans2);
    }
  }
  cout << ans2 << " " << ans1 << endl;
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

