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
  i64 K, N;
  cin >> N >> K;
  multiset<i64, greater<i64> > ivs;
  ivs.insert(N);
  i64 i;
  i64 ans1, ans2;
  REP(0, K, i) {
    auto iter = ivs.begin();
    i64 iv = *iter;
    ivs.erase(iter);
    if(iv == 0) {
      ans1 = ans2 = 0;
    }
    else if(iv % 2 == 1) {
      ans1 = ans2 = (iv - 1) / 2;
    }
    else {
      ans1 = iv / 2;
      ans2 = iv / 2 - 1;
    }
    ivs.insert(ans1);
    ivs.insert(ans2);
  }
  
  cout << ans1 << " " << ans2 << std::endl;
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

