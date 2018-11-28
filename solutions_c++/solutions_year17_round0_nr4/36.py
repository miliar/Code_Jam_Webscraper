// Author: Chi-Kit (George) LAM
#include <bits/stdc++.h>
using namespace std;
#define DEBUG_ENABLED 1
namespace jam{
  typedef long long LL;
  struct Jam {
    Jam(unsigned int seed) {
      srand(seed);
      cout.precision(9);
    }
  };
#if DEBUG_ENABLED
  #define DEBUG(...) \
    (cout << "DEBUG:" << __LINE__ << ": (" << #__VA_ARGS__ \
          << ") = " << make_tuple(__VA_ARGS__) << endl)
  template <size_t I, class... Types> struct TuplePrinter {
    void print(ostream& out, const tuple<Types...>& x) const {
      TuplePrinter<I-1, Types...>().print(out, x);
      out << ", " << get<I-1>(x);
    }
  };
  template <class... Types> struct TuplePrinter<1, Types...> {
    void print(ostream& out, const tuple<Types...>& x) const {
      out << get<0>(x);
    }
  };
  template <class... Types>
  ostream& operator<<(ostream& out, const tuple<Types...>& x) {
    out << "(";
    TuplePrinter<sizeof...(Types), Types...>().print(out, x);
    return out << ")";
  }
  template <class T1, class T2>
  ostream& operator<<(ostream& out, pair<T1, T2> x) {
    return out << tuple<T1, T2>(x);
  }
  template <class T, class Alloc>
  ostream& operator<<(ostream& out, const deque<T, Alloc>& x) {
    out << "{";
    bool flag = true;
    for (auto& v : x) {
      if (flag) {
        flag = false;
      } else {
        out << ", ";
      }
      out << v;
    }
    return out << "}";
  }
  template <class T, class Compare, class Alloc>
  ostream& operator<<(ostream& out, const set<T, Compare, Alloc>& x) {
    out << "{";
    bool flag = true;
    for (auto& v : x) {
      if (flag) {
        flag = false;
      } else {
        out << ", ";
      }
      out << v;
    }
    return out << "}";

  }
  template <class Key, class T, class Compare, class Alloc>
  ostream& operator<<(ostream& out, const map<Key, T, Compare, Alloc>& x) {
    out << "{";
    bool flag = true;
    for (auto& kv : x) {
      if (flag) {
        flag = false;
      } else {
        out << ", ";
      }
      out << kv->first << ": " << kv->second;
    }
    return out << "}";
  }
#else
  #define DEBUG(...)
#endif
  template <typename flow_type=int> struct FlowNetwork {
    int n;
    vector< vector<int> > adj;
    vector< map<int,flow_type> > c;
    vector< map<int,flow_type> > f;
    vector<int> pred;
    FlowNetwork(int n) : n(n), adj(n), c(n), f(n) {};
    void add(int u, int v, flow_type x) {
      if (c[u][v] == 0 && c[v][u] == 0) {
        adj[u].push_back(v);
        adj[v].push_back(u);
      }
      c[u][v] += x;
    }
    bool bfs(int s, int t) {
      pred = vector<int>(n, -1);
      queue<int> Q;
      Q.push(s);
      pred[s] = s;
      while (!Q.empty()) {
        int u = Q.front(); Q.pop();
        for (int v : adj[u]) {
          if (f[u][v] < c[u][v] && pred[v] == -1) {
            pred[v] = u;
            if (v == t) return true;
            Q.push(v);
          }
        }
      }
      return false;
    }
    flow_type edmonds_karp(int s, int t) {
      flow_type total = 0;
      while (bfs(s,t)) {
        flow_type delta = c[pred[t]][t] - f[pred[t]][t];
        for (int v = t; v != s; v = pred[v]) {
          int u = pred[v];
          delta = min(delta, c[u][v] - f[u][v]);
        }
        for (int v = t; v != s; v = pred[v]) {
          int u = pred[v];
          f[u][v] += delta; f[v][u] -= delta;
        }
        total += delta;
      }
      return total;
    }
  };
} // namespace jam
using namespace jam;
Jam JAM(/*seed*/ 0);

void solve(int T) {
  int N, M, ans = 0;
  cin >> N >> M;
  vector<char> A(N*N, '.'), B;
  vector<bool> P(N*6, false);
  for (int i=0; i!=M; ++i) {
    char c;
    int x, y;
    cin >> c >> x >> y;
    --x; --y;
    A[x*N+y] = c;
    if (c == 'o' || c == 'x') {
      P[x] = true;
      P[3*N + y] = true;
      ++ans;
    }
    if (c == 'o' || c == '+') {
      P[N + x + y] = true;
      P[5*N + x - y - 1] = true;
      ++ans;
    }
  }
  FlowNetwork<> G(7 * N);
  for(int i = 0; i!=3*N-1; ++i) {
    if (!P[i]) {
      G.add(3*N-1, i, 1);
    }
    if (!P[3*N+i]) {
      G.add(3*N+i, 6*N-1, 1);
    }
  }
  for (int x=0; x!=N; ++x) {
    for (int y=0; y!=N; ++y) {
      G.add(x, 3*N + y, 1);
      G.add(N + x + y, 5*N + x - y - 1, 1);
    }
  }
  ans += G.edmonds_karp(3*N-1, 6*N-1);
  int count = 0;
  B = A;
  for (int x=0; x!=N; ++x) {
    for (int y=0; y!=N; ++y) {
      if (G.f[x][3*N + y]) {
        B[x*N+y] = (B[x*N+y] == '+' ? 'o' : 'x');
      }
      if (G.f[N + x + y][5*N + x - y - 1]) {
        B[x*N+y] = (B[x*N+y] == 'x' ? 'o' : '+');
      }
      if (B[x*N+y] != A[x*N+y]) {
        ++count;
      }
    }
  }
  cout << "Case #" << T << ": " << ans << " " << count << endl;
  for (int x=0; x!=N; ++x) {
    for (int y=0; y!=N; ++y) {
      if (B[x*N+y] != A[x*N+y]) {
        cout << B[x*N+y] << " " << (x+1) << " " << (y+1) << endl;
      }
    }
  }
}
int main(){
  int T;
  cin >> T;
  for (int i=0; i<T; ++i) {
    solve(i+1);
  }
  return 0;
}
