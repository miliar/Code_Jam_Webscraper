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

i64 answer(i64 S, i64 N) {
  i64 digit = S % 10;
  if(S < 10) {
    if(digit <= N) {
      return digit;
    }
    else if(digit == 0) {
      return 0;
    }
    else {
      return -1;
    }
  }
  else {
    i64 ans1 = -1, ans2 = -1;
    i64 t1, t2;
    if(N == 0) {
      return -1;
    }
    if(digit <= N) {
      t1 = answer((S - digit) / 10, digit);
      if(t1 >= 0) {
	ans1 = t1 * 10 + digit;
      }
    }
    t2 = answer((S - digit) / 10 - 1, N);
    if(t2 >= 0) {
      ans2 = t2 * 10 + N;
    }
    return max(ans1, ans2);
  }
}

void Solver::solve() {
  i64 S;
  cin >> S;

  i64 ans = answer(S, 9);
  cout << ans << endl;
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

