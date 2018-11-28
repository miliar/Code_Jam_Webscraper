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

void stp(const vvi &D0, vvi &D1, i64 i, i64 j) {
  if(D1[i][j] >= 0) {
    return;
  }

  i64 N, k;
  N = D0.size();

  set<pi> q;
  vi visited(N, 0);
  vvi D(N, vi(N, -1));
  q.insert(pi(0, i));
  while(!q.empty()) {
    pi p = *q.begin();
    q.erase(q.begin());
    
    i64 cur = p.second;
    if(D[i][cur] < 0) {
      D[i][cur] = p.first;
    }
    D[i][cur] = min(D[i][cur], p.first);
    visited[cur] = 1;

    REP(0, N, k) {
      if(visited[k] == 0 && D0[cur][k] > 0) {
	i64 newD = D[i][cur] + D0[cur][k];
	if(D[i][k] > 0) {
	  q.erase(q.find(pi(D[i][k], k)));
	  D[i][k] = min(D[i][k], newD);
	}
	else {
	  D[i][k] = newD;
	}
	q.insert(pi(D[i][k], k));
      }
    }
  }

  i64 l;
  REP(0, N, k) {
    REP(0, N, l) {
      if(D[k][l] > 0) {
	D1[k][l] = D[k][l];
      }
    }
  }
}

void Solver::solve() {
  i64 N, Q, i, j;
  cin >> N >> Q;

  vi E(N), S(N);
  REP(0, N, i) {
    cin >> E[i] >> S[i];
  }

  vvi D0(N, vi(N));
  REP(0, N, i) {
    REP(0, N, j) {
      cin >> D0[i][j];
    }
  }

  vvi D(N, vi(N, -1));
  REP(0, N, i) {
    REP(0, N, j) {
      if(i != j) {
	stp(D0, D, i, j);
      }
    }
  }

  i64 q;
  vector<pi> Qs(Q);
  REP(0, Q, q) {
    cin >> Qs[q].first >> Qs[q].second;
  }

  // solution for large dataset
  REP(0, Q, q) {
    i64 b = Qs[q].first - 1, e = Qs[q].second-1;
    vector<double> ts(N, -1);
    vi visited(N, 0);

    typedef pair<double, i64> pdi;
    set<pdi> qs;
    qs.insert(pdi(0, b));
    while(!qs.empty()) {
      pdi p = *qs.begin();
      qs.erase(qs.begin());

      if(visited[p.second] == 0) {
	visited[p.second] = 1;
	ts[p.second] = p.first;
	double t_cur = p.first;

	REP(0, N, j) {
	  if(j != p.second && visited[j] == 0 && D[p.second][j] > 0 && D[p.second][j] <= E[p.second]) {
	    double t_new = t_cur + double(D[p.second][j]) / double(S[p.second]);
	    if(ts[j] >= 0) {
	      // erase
	      qs.erase(qs.find(pdi(ts[j], j)));
	    }
	    else {
	      ts[j] = t_new;
	    }
	    ts[j] = min(ts[j], t_new);
	    qs.insert(pdi(ts[j], j));
	  }
	}
      }
    }
    if(q != 0) {
      cout << " ";
    }
    printf("%.10f", ts[e]);
  }
  cout << endl;
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

