#include <bits/stdc++.h>
using namespace std;
template <class T> int size(const T &x) { return x.size(); }
#define rep(i,a,b) for (__typeof(a) i=(a); i<(b); ++i)
#define iter(it,c) for (__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
const int INF = 2147483647;

#define MAXN 5000
int dist[MAXN+1], q[MAXN+1];
#define dist(v) dist[v == -1 ? MAXN : v]
struct bipartite_graph {
  int N, M, *L, *R; vi *adj;
  bipartite_graph(int _N, int _M) : N(_N), M(_M),
    L(new int[N]), R(new int[M]), adj(new vi[N]) {}
  ~bipartite_graph() { delete[] adj; delete[] L; delete[] R; }
  bool bfs() {
    int l = 0, r = 0;
    rep(v,0,N) if(L[v] == -1) dist(v) = 0, q[r++] = v;
      else dist(v) = INF;
    dist(-1) = INF;
    while(l < r) {
      int v = q[l++];
      if(dist(v) < dist(-1)) {
        iter(u, adj[v]) if(dist(R[*u]) == INF)
          dist(R[*u]) = dist(v) + 1, q[r++] = R[*u]; } }
    return dist(-1) != INF; }
  bool dfs(int v) {
    if(v != -1) {
      iter(u, adj[v])
        if(dist(R[*u]) == dist(v) + 1)
          if(dfs(R[*u])) {
            R[*u] = v, L[v] = *u;
            return true; }
      dist(v) = INF;
      return false; }
    return true; }
  void add_edge(int i, int j) { adj[i].push_back(j); }
  int maximum_matching() {
    int matching = 0;
    memset(L, -1, sizeof(int) * N);
    memset(R, -1, sizeof(int) * M);
    while(bfs()) rep(i,0,N)
      matching += L[i] == -1 && dfs(i);
    return matching; } };

bool A[110][110],
     B[110][110],
     C[110][110],
     D[110][110];

int main() {
    int ts;
    cin >> ts;
    rep(t,0,ts) {
        int n, m;
        cin >> n >> m;
        memset(A,0,sizeof(A));
        memset(B,0,sizeof(B));
        memset(C,0,sizeof(C));
        memset(D,0,sizeof(D));
        rep(i,0,m) {
            char tp;
            int x,y;
            cin >> tp >> x >> y;
            x--, y--;
            if (tp == '+' || tp == 'o') {
                A[x][y] = true;
            }
            if (tp == 'x' || tp == 'o') {
                B[x][y] = true;
            }
        }

        int add = 0;
        {
            bipartite_graph G(2*n-1, 2*n-1);
            vector<bool> usedl(2*n-1),
                         usedr(2*n-1);
            rep(i,0,n) {
                rep(j,0,n) {
                    if (A[i][j]) {
                        usedl[i-j+n-1] = true;
                        usedr[i+j] = true;

                       // cout << i << "," << j << " " << i-j + n-1 << " " << i+j << endl;
                    }
                }
            }
            rep(i,0,n) {
                rep(j,0,n) {
                    if (usedl[i-j+n-1]) continue;
                    if (usedr[i+j]) continue;
                    G.add_edge(i-j+n-1,i+j);
                    // cout << i << " " << j << " " <<  i-j+n-1 << " " << i+j << endl;
                }
            }
            // cout << "a " << G.maximum_matching() << endl;
            add += G.maximum_matching();
            rep(i,0,n) {
                rep(j,0,n) {
                    if (A[i][j] || G.L[i-j+n-1] == i+j) {
                        C[i][j] = true;
                    }
                }
            }
        }
        {
            bipartite_graph G(n,n);
            vector<bool> usedl(n),
                         usedr(n);
            rep(i,0,n) {
                rep(j,0,n) {
                    if (B[i][j]) {
                        usedl[i] = true;
                        usedr[j] = true;
                    }
                }
            }
            rep(i,0,n) {
                if (usedl[i]) continue;
                rep(j,0,n) {
                    if (usedr[j]) continue;
                    G.add_edge(i,j);
                    // cout << i << " " << j << endl;
                }
            }
            // cout << "b " << G.maximum_matching() << endl;
            add += G.maximum_matching();
            rep(i,0,n) {
                rep(j,0,n) {
                    if (B[i][j] || G.L[i] == j) {
                        D[i][j] = true;
                    }
                }
            }
        }

        vector<pair<ii,char> > res;
        int cnt = 0;
        rep(i,0,n) {
            rep(j,0,n) {
                if (C[i][j] && D[i][j]) {
                    cnt += 2;
                    if (!A[i][j] || !B[i][j]) {
                        res.push_back(make_pair(ii(i,j), 'o'));
                    }
                } else if (C[i][j]) {
                    cnt += 1;
                    if (!A[i][j]) {
                        res.push_back(make_pair(ii(i,j), '+'));
                    }
                } else if (D[i][j]) {
                    cnt += 1;
                    if (!B[i][j]) {
                        res.push_back(make_pair(ii(i,j), 'x'));
                    }
                } else {
                }
            }
        }

        cout << "Case #" << (t+1) << ": ";
        cout << cnt << " " << size(res) << endl;
        iter(it,res) {
            cout << it->second << " " << it->first.first + 1 << " " << it->first.second + 1 << endl;
        }
    }
    return 0;
}

