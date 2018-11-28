#include <bits/stdc++.h>

using namespace std;

#define PB push_back
#define MP make_pair
#define LL long long
#define int LL
#define st first
#define nd second
#define VI vector<int>
#define LD long double
#define PII pair<int,int>
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())

template <class C> void mini(C& a4, C b4) { a4 = min(a4, b4); }
template <class C> void maxi(C& a4, C b4) { a4 = max(a4, b4); }

template <class TH> void _dbg(const char *sdbg, TH h) { cerr << sdbg << "=" << h << "\n"; }
template <class TH, class ... TA> void _dbg(const char *sdbg, TH h, TA... a) {
  while (*sdbg != ',') cerr << *sdbg++; cerr << "=" << h << ","; _dbg(sdbg+1, a...);
}

template <class T> ostream &operator<<(ostream &os, vector<T> V) {
  os << "["; for (auto vv : V) os << vv << ","; return os << "]";
}

template <class L, class R> ostream &operator<<(ostream &os, pair<L,R> P) {
  return os << "(" << P.st << "," << P.nd << ")";
}


#ifdef LOCAL
#define debug(...) _dbg(#__VA_ARGS__, __VA_ARGS__)
#else
#define debug(...) (__VA_ARGS__)
#define cerr if(0)cout
#endif


struct Matching {
  vector<VI> adj;
  int N;
  vector<int> matching, dematching;
  vector<bool> lockedVert, vis;

  Matching(int sz) : adj(sz), N(sz), matching(N, -1), dematching(N, -1), lockedVert(N), vis(N) {}

  void addEdge(int l, int r) {
    adj[l].push_back(r);
  }

  void insistEdge(int l, int r) {
    matching[l] = r;
    dematching[r] = l;
    lockedVert[l] = true;
  }

  bool dfs(int v) {
    if (vis[v]) { return false; }
    vis[v] = true;

    for (int s : adj[v]) {
      if (dematching[s] == -1 || dfs(dematching[s])) {
        matching[v] = s;
        dematching[s] = v;
        return true;
      }
    }
    return false;
  }

  int match() {
    bool change;
    int result = N - count(ALL(matching), -1);

    do {
      change = false;
      copy(ALL(lockedVert), vis.begin());

      for (int i = 0; i < N; i++) {
        if (!vis[i] && matching[i] == -1 && dfs(i)) {
          result++;
          change = true;
        }
      }

    } while (change);
    
    return result;
  }
};


struct Testcase {
  int N, M, S;
  set<string> descriptions;
  vector<string> resDescriptions;

  void run(int id) {
    cin >> N >> M;
    S = N - 1;
    Matching straight(N), diag(2 * N - 1);

    for (int r = 0; r < N; r++) {
      for (int c = 0; c < N; c++) {
        straight.addEdge(r, c);
        diag.addEdge(r + c, r - c + S);
      }
    }

    for (int i = 0; i < M; i++) {
      char type; int r, c;
      cin >> type >> r >> c;
      r--; c--;
      descriptions.insert(type + string(" ") + to_string(r+1) + " " + to_string(c+1));

      if (type != '+') { straight.insistEdge(r, c); }
      if (type != 'x') { diag.insistEdge(r + c, r - c + S); }
    }

    int score = straight.match() + diag.match();

    for (int r = 0; r < N; r++) {
      for (int c = 0; c < N; c++) {
        bool isX = false, isP = false;

        if (straight.matching[r] == c) { isX = true; }
        if (diag.matching[r + c] == r - c + S) { isP = true; }

        if (!isP && !isX) { continue; }

        char ch;
        if (isP && isX) {
          ch = 'o';
        } else if (isP) {
          ch = '+';
        } else {
          ch = 'x';
        }

        resDescriptions.PB(ch + string(" ") + to_string(r+1) + " " + to_string(c+1));
      }
    }

    sort(ALL(resDescriptions));
    vector<string> outDescriptions;
    set_difference(ALL(resDescriptions), ALL(descriptions), back_inserter(outDescriptions));

    cout << "Case #" << id << ": " << score << " " << SZ(outDescriptions) << "\n";
    for (string s : outDescriptions) { cout << s << "\n"; }
  }
};


int32_t main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout << fixed << setprecision(11);
  cerr << fixed << setprecision(6);

  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    Testcase tc;
    tc.run(i + 1);
  }
}
