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
  i64 N, P;
  cin >> N >> P;
  vi G;
  i64 i;
  
  i64 ans = 0;
  i64 cp1, cp2, cm1;
  cp1 = cp2 = cm1 = 0;
  REP(0, N, i) {
    i64 g;
    cin >> g;

    if(g % P == 0) {
      ++ans;
    }
    else if(g % P == 1) {
      ++cp1;
    }
    else if((g + 1) % P == 0) {
      ++cm1;
    }
    else {
      ++cp2;
    }    
  }

  while(cp1 > 0 && cm1 > 0) {
    --cp1;
    --cm1;

    ++ans;
  }

  if(P == 4) {
    ans += (cp2 / 2);
    cp2 %= 2;
  }

  i64 rest = max(cp1, cm1);

  if(cp2 != 0) {
    ++ans;
    rest -= 2;
    rest = max(rest, 0LL);
  }
  
  ans += rest / P;
  if(rest % P != 0) {
    ++ans;
  }

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

