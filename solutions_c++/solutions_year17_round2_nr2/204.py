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

std::string fragment(char c) {
  switch(c) {
  case 'R':
    return "RG";
  case 'Y':
    return "YV";
  case 'B':
    return "BO";
  }
  return "";
}

void Solver::solve() {
  i64 N, R, O, Y, G, B, V;
  cin >> N >> R >> O >> Y >> G >> B >> V;

  // corner cases
  if(R == 0 && G == 0) {
    i64 i;
    if(V == 0 && Y == 0 && O == B) {
      REP(0, B, i) {
	cout << "OB";
      }
      cout << endl;
      return;
    }
    if(O == 0 && B == 0 && V == Y) {
      REP(0, V, i) {
	cout << "VY";
      }
      cout << endl;
      return;
    }
  }
  if(R == G && V == 0 && Y == 0 && O == 0 && B == 0) {
    i64 i;
    REP(0, R, i) {
      cout << "RG";
    }
    cout << endl;
    return;
  }


  // adaptation
  if((G > 0 && R <= G) || (V > 0 && Y <= V) || (O > 0 && B <= O)) {
    cout << "IMPOSSIBLE" << endl;
    return;
  }

  i64 R_new, Y_new, B_new;
  R_new = R - G;
  Y_new = Y - V;
  B_new = B - O;

  // now, solution for small can be re-used
  vector<pair<int, pair<int, char> > > vals(3);
  vals[0] = make_pair(R_new, make_pair(G, 'R'));
  vals[1] = make_pair(Y_new, make_pair(V, 'Y'));
  vals[2] = make_pair(B_new, make_pair(O, 'B'));

  sort(all(vals));

  if(vals[0].first + vals[1].first < vals[2].first) {
    cout << "IMPOSSIBLE" << endl;
    return;
  }
  else {
    i64 i, j;
    bool f0, f1, f2;
    f0 = f1 = f2 = true;
    REP(0, vals[2].first, i) {
      if(f2 ) {
	REP(0, vals[2].second.first, j) {
	  cout << fragment(vals[2].second.second);
	}
	f2 = false;
      }
      cout << vals[2].second.second;
      if(i < vals[1].first) {
	if(f1) {
	  REP(0, vals[1].second.first, j) {
	    cout << fragment(vals[1].second.second);
	  }
	  f1 = false;
	}
	cout << vals[1].second.second;
      }
      if(vals[2].first - vals[0].first <= i) {
	if(f0) {
	  REP(0, vals[0].second.first, j) {
	    cout << fragment(vals[0].second.second);
	  }
	  f0 = false;
	}
	cout << vals[0].second.second;
      }
    }
    cout << endl;
    return;
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

