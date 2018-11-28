//============================================================================
// Name        : gcj.cpp
// Author      : Boleyn Su
// Version     :
// Copyright   : All Rights Reserved
// Description : Hello World in C++, Ansi-style
//============================================================================

// BEGIN gcj.h
#ifdef CLOUD
#include <mpi.h>
#include <cassert>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace MPI;
using namespace std;

template <typename S>
void run(string in, string out) {
  ifstream cin(in);
  static char buf[1 << 25];
  Init();
  int nodes = COMM_WORLD.Get_size();
  int id = COMM_WORLD.Get_rank();

  int T;
  cin >> T;
  vector<string> ans(T);
  for (int t = 0; t < T; t++) {
    S::read(cin);
    if (t % nodes == id) {
      stringstream sout;
      sout << "Case #" << t + 1 << ":";
      S::solve(sout);
      ans[t] = sout.str();
    }
  }

  for (int t = 0; t < T; t++) {
    if (t % nodes == id) {
      if (id != 0) {
        int sz = ans[t].size();
        for (int i = 0; i < sz; i++) {
          buf[i] = ans[t][i];
        }
        assert(sz < sizeof(buf) / sizeof(*buf));
        COMM_WORLD.Send(&sz, 1, MPI_INT, 0, 0);
        COMM_WORLD.Send(buf, sz, MPI_CHAR, 0, 0);
      }
    } else {
      if (id == 0) {
        int sz;
        COMM_WORLD.Recv(&sz, 1, MPI_INT, t % nodes, 0);
        COMM_WORLD.Recv(buf, sz, MPI_CHAR, t % nodes, 0);
        ans[t] = string(buf, buf + sz);
      }
    }
  }
  if (id == 0) {
    ofstream cout(out);
    for (int t = 0; t < T; t++) {
      cout << ans[t];
    }
  }
  Finalize();
}

#else
#include <fstream>
#include <string>

using namespace std;

template <typename S>
void run(string in, string out) {
  ifstream cin(in);
  ofstream cout(out);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    S::read(cin);
    cout << "Case #" << t << ":";
    S::solve(cout);
  }
}
#endif
// END gcj.h

#include <algorithm>
#include <cassert>
#include <cstring>
#include <iomanip>
#include <limits>
#include <queue>
#include <set>
#include <utility>
#include <vector>

using namespace std;

//用于减少代码量的宏;
#define lp for (;;)
#define repf(i, a, b) for (int i = (a); i < (b); ++i)
#define ft(i, a, b) for (int i = (a); i <= (b); ++i)
#define fdt(i, a, b) for (int i = (a); i >= (b); --i)
#define rrepf(i, a, b) fdt(i, (a)-1, b)
#define rep(i, n) repf(i, 0, n)
#define rrep(i, n) rrepf(i, n, 0)
#define for_each(e, s) \
  for (__typeof__((s).begin()) e = (s).begin(); e != (s).end(); ++e)
#define for_nonempty_subsets(subset, set) \
  for (int subset = set; subset; subset = (subset - 1) & (set))
#define for_in_charset(i, charset) for (cstr i = (charset); *i; i++)
#define whl while
#define rtn return
#define fl(x, y) memset((x), char(y), sizeof(x))
#define clr(x) fl(x, char(0))
#define cpy(x, y) memcpy(x, y, sizeof(x))
#define sf scanf
#define pf printf
#define vec vector
#define pr pair
#define que queue
#define prq priority_queue
#define itr iterator
#define x first
#define y second
#define pb push_back
#define mp make_pair
#define ins insert
#define ers erase
#define lb lower_bound
#define ub upper_bound
#define rnk order_of_key
#define sel find_by_order
#define ctz __builtin_ctz
#define clz __builtin_clz
#define bc __builtin_popcount
#define sz(x) (int((x).size()))
#define all(x) (x).begin(), (x).end()
#define srt(x) sort(all(x))
#define uniq(x) srt(x), (x).erase(unique(all(x)), (x).end())
#define rev(x) reverse(all(x))
#define shf(x) random_shuffle(all(x))
#define nxtp(x) next_permutation(all(x))

template <typename type>
inline bool cmax(type& a, const type& b) {
  rtn a < b ? a = b, true : false;
}
template <typename type>
inline bool cmin(type& a, const type& b) {
  rtn b < a ? a = b, true : false;
}

const int MAX_DIST = 0x7f7f7f7f;
const int MAXV = 1 << 20;
const int MAXE = 2 << 20;
typedef int flow_type;
const int MAX_FLOW = 0x7f7f7f7f;
typedef struct struct_edge* edge;
struct struct_edge {
  int v;
  flow_type c;
  edge n, b;
} pool[MAXE];
edge top;
int S, T;
edge adj[MAXV];
void build_graph(int s, int t) {
  top = pool, clr(adj);
  S = s, T = t;  //源,汇
                 // add_edge(u,v,c);
}
void add_edge(int u, int v, flow_type c, flow_type bc = 0) {
  top->v = v, top->c = c, top->n = adj[u], adj[u] = top++;
  top->v = u, top->c = bc, top->n = adj[v], adj[v] = top++;
  adj[u]->b = adj[v], adj[v]->b = adj[u];
  if (u == v)
    adj[u]->n->b = adj[u],
    adj[v]->b = adj[v]->n;  //防止add_edge(u,u,c,bc)时出现RE
}
int d[MAXV];
int q[MAXV];
int qh, qt;
bool relabel() {
  fl(d, MAX_DIST), d[q[qh = qt = 0] = T] = 0;
  whl(qh <= qt) {
    int u = q[qh++];
    for (edge i = adj[u]; i; i = i->n)
      if (i->b->c && cmin(d[i->v], d[u] + 1))
        if ((q[++qt] = i->v) == S) rtn true;
  }
  rtn false;
}
edge cur[MAXV];
flow_type augment(int u, flow_type e) {
  if (u == T) rtn e;
  flow_type f = 0;
  for (edge& i = cur[u]; i; i = i->n) {
    if (i->c && d[u] == d[i->v] + 1)
      if (flow_type df = augment(i->v, min(e, i->c)))
        i->c -= df, i->b->c += df, e -= df, f += df;
    if (!e) break;
  }
  rtn f;
}
flow_type dinic() {
  flow_type f = 0;
  while (relabel()) cpy(cur, adj), f += augment(S, MAX_FLOW);
  rtn f;
}

int n, c, m;
pair<int, int> lst[1 << 20];
edge e[1 << 20];

struct Solver {
  static void read(istream& cin) {
    cin >> n >> c >> m;
    for (int i = 0; i < m; ++i) {
      cin >> lst[i].first >> lst[i].second;
      lst[i].second--;
    }
  }
  static void solve(ostream& cout) {
    build_graph(m, m + 1);
    for (int i = 0; i < m; i++) {
      e[i] = top;
      if (lst[i].second) {
        add_edge(i, T, 1);
      } else {
        add_edge(S, i, 1);
      }
    }
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < m; j++) {
        if (lst[i].second < lst[j].second) {
          if (lst[i].first != lst[j].first) {
            add_edge(i, j, 1);
          }
        }
      }
    }
    int x = dinic();
    int cnt[2] = {0, 0};
    int is1 = false;
    for (int i = 0; i < m; i++) {
      if (e[i]->c) {
        cnt[lst[i].second]++;
        is1 = is1 || lst[i].first == 1;
      }
    }
//    cout << m << " " << x << " " << cnt[0] << " " << cnt[1] << " " << is1
//         << endl;
    cout << " " << m - x - (is1 ? 0 : min(cnt[0], cnt[1])) << " "
         << (is1 ? 0 : min(cnt[0], cnt[1])) << endl;
  }
};

int main() {
  run<Solver>("in.txt", "out.txt");
  return 0;
}
