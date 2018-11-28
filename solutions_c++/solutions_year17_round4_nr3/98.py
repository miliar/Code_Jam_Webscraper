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

struct { vi adj; int val, num, lo; bool done; } V[2*10000+100];
struct TwoSat {
  int n, at = 0; vi S;
  TwoSat(int _n) : n(_n) {
    rep(i,0,2*n+1)
      V[i].adj.clear(),
      V[i].val = V[i].num = -1, V[i].done = false; }
  bool put(int x, int v) {
    return (V[n+x].val &= v) != (V[n-x].val &= 1-v); }
  void add_or(int x, int y) {
    V[n-x].adj.push_back(n+y), V[n-y].adj.push_back(n+x); }
  int dfs(int u) {
    int br = 2, res;
    S.push_back(u), V[u].num = V[u].lo = at++;
    iter(v,V[u].adj) {
      if (V[*v].num == -1) {
        if (!(res = dfs(*v))) return 0;
        br |= res, V[u].lo = min(V[u].lo, V[*v].lo);
      } else if (!V[*v].done)
        V[u].lo = min(V[u].lo, V[*v].num);
      br |= !V[*v].val; }
    res = br - 3;
    if (V[u].num == V[u].lo) rep(i,res+1,2) {
      for (int j = size(S)-1; ; j--) {
        int v = S[j];
        if (i) {
          if (!put(v-n, res)) return 0;
          V[v].done = true, S.pop_back();
        } else res &= V[v].val;
        if (v == u) break; }
      res &= 1; }
    return br | !res; }
  bool sat() {
    rep(i,0,2*n+1)
      if (i != n && V[i].num == -1 && !dfs(i)) return false;
    return true; }
  bool get(int x) {
      assert(V[n+x].val == 0 || V[n+x].val == 1);
      return V[n+x].val != 0;
  }
};
// vim: cc=60 ts=2 sts=2 sw=2:

vi need[50][50];
char arr[50][50];

// N, W, S, E
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, -1, 0, 1};

int turn(char c, int dir) {
    if (c == '.') return dir;
    if (c == '/') {
        if (dir == 0) return 3;
        if (dir == 3) return 0;
        if (dir == 1) return 2;
        if (dir == 2) return 1;
    }
    if (c == '\\') {
        if (dir == 0) return 1;
        if (dir == 1) return 0;
        if (dir == 2) return 3;
        if (dir == 3) return 2;
    }
    assert(false);
}

int main() {
    int ts;
    cin >> ts;
    rep(t,0,ts) {
        int n, m;
        cin >> n >> m;
        rep(i,0,n) {
            rep(j,0,m) {
                cin >> arr[i][j];
                need[i][j].clear();
            }
        }
        vi bad;
        int who = 1;
        rep(i,0,n) {
            rep(j,0,m) {
                vii met;
                queue<pair<ii,ii> > Q;
                if (arr[i][j] == '|') {
                    Q.push(make_pair(ii(i,j), ii(0, who)));
                    Q.push(make_pair(ii(i,j), ii(2, who)));
                    Q.push(make_pair(ii(i,j), ii(1, -who)));
                    Q.push(make_pair(ii(i,j), ii(3, -who)));
                    who++;
                }
                if (arr[i][j] == '-') {
                    Q.push(make_pair(ii(i,j), ii(1, who)));
                    Q.push(make_pair(ii(i,j), ii(3, who)));
                    Q.push(make_pair(ii(i,j), ii(0, -who)));
                    Q.push(make_pair(ii(i,j), ii(2, -who)));
                    who++;
                }
                while (!Q.empty()) {
                    pair<ii,ii> cur = Q.front();
                    Q.pop();
                    ii nxt(cur.first.first + dx[cur.second.first],
                           cur.first.second + dy[cur.second.first]);
                    if (nxt.first < 0 || nxt.first >= n || nxt.second < 0 || nxt.second >= m)
                        continue;
                    if (arr[nxt.first][nxt.second] == '#')
                        continue;
                    if (arr[nxt.first][nxt.second] == '|') {
                        bad.push_back(cur.second.second);
                        continue;
                    }
                    if (arr[nxt.first][nxt.second] == '-') {
                        bad.push_back(cur.second.second);
                        continue;
                    }
                    int ndir = turn(arr[nxt.first][nxt.second], cur.second.first);
                    need[nxt.first][nxt.second].push_back(cur.second.second);
                    Q.push(make_pair(nxt, ii(ndir, cur.second.second)));
                }
            }
        }
        cout << "Case #" << (t+1) << ": ";
        // TODO: what if who = 1?
        TwoSat ts(who-1);
        iter(it,bad) {
            ts.add_or(-*it, -*it);
        }
        bool ok = true;
        rep(i,0,n) {
            rep(j,0,m) {
                if (arr[i][j] == '.') {
                    // cout << i << "," << j << ": ";
                    // iter(it,need[i][j]) {
                    //     cout << *it << " ";
                    // }
                    // cout << endl;
                    if (size(need[i][j]) == 0) {
                        ok = false;
                        goto done;
                    }
                    if (size(need[i][j]) == 1) {
                        ts.add_or(need[i][j][0], need[i][j][0]); // TODO: ok?
                    }
                    if (size(need[i][j]) == 2) {
                        ts.add_or(need[i][j][0], need[i][j][1]);
                    }
                    assert(size(need[i][j]) <= 2);
                }
            }
        }

        ok = ok && ts.sat();
        if (ok) {
            cout << "POSSIBLE" << endl;
            int who = 1;
            rep(i,0,n) {
                rep(j,0,m) {
                    if (arr[i][j] == '|') {
                        if (ts.get(who)) {
                            cout << "|";
                        } else {
                            cout << "-";
                        }
                        who++;
                    } else if (arr[i][j] == '-') {
                        if (ts.get(who)) {
                            cout << "-";
                        } else {
                            cout << "|";
                        }
                        who++;
                    } else {
                        cout << arr[i][j];
                    }
                }
                cout << endl;
            }
        }
done:
        if (!ok) {
            cout << "IMPOSSIBLE" << endl;
        }
    }



    return 0;
}

