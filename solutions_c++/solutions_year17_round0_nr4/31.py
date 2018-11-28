#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define DEBUG
#ifdef DEBUG
#define TRACE(x) cerr << #x << " = " << x << endl;
#define _ << " _ " <<
#else
#define TRACE(x) ((void)0)
#endif

const int INFCAP = 1000000005;
const int MAXN = 430;
typedef struct {
  int to;
  int cap;
} edge;

vector<int> ai[MAXN];
vector<edge> el;
int lev[MAXN];
int SRC;
int DST;
vector<int> lai[MAXN];
unsigned ng[MAXN];
int path[MAXN];
int pathsz;

void addedge(int u, int v, int c) {
  const int idx = el.size();
  const edge e1 = {v, c}, e2 = {u, 0};
  ai[u].push_back(idx);
  el.push_back(e1);
  ai[v].push_back(idx + 1);
  el.push_back(e2);
}

bool buildlevel() {
  for (int i = 0; i < MAXN; i++)
    lai[i].clear();
  fill(lev, lev + MAXN, 0);
  queue<int> q;
  q.push(SRC);
  lev[SRC] = 1;
  while (!q.empty()) {
    const int v = q.front();
    q.pop();
    if (v == DST)
      return true;
    for (auto idx : ai[v]) {
      const edge&e = el[idx];
      if (e.cap > 0) {
        if (lev[e.to] == 0) {
          lev[e.to] = lev[v] + 1;
          lai[v].push_back(idx);
          q.push(e.to);
        } else if (lev[e.to] == lev[v] + 1) {
          lai[v].push_back(idx);
        }
      }
    }
  }
  return false;
}

int dfs(int v) {
  if (v == DST)
    return INFCAP;
  for (; ng[v] < lai[v].size(); ng[v]++) {
    const edge& e = el[lai[v][ng[v]]];
    if (e.cap > 0) {
      int fl = dfs(e.to);
      if (fl > 0) {
        path[pathsz++] = lai[v][ng[v]];
        return min(fl, e.cap);
      }
    }
  }
  return 0;
}

ll maxflow(int src, int dst) {
  SRC = src, DST = dst;
  ll ret = 0;
  while (buildlevel()) {
    fill(ng, ng + MAXN, 0);
    int fl;
    while ((fl = dfs(SRC)) > 0) {
      ret += fl;
      for (int i = 0; i < pathsz; i++) {
        el[path[i]].cap -= fl;
        el[path[i] ^ 1].cap += fl;
      }
      pathsz = 0;
    }
  }
  return ret;
}

bool rhit[105];
bool chit[105];
bool dhit[450];
#define dm(i, j) (((i) - (j)) + 110)
#define dp(i, j) (((i) + (j)) + 220)
#define mp(i, j) (((i) << 16) | (j))
const int mask = 0x0000ffff;

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

  int T;
  cin >> T;
  for (int tt = 1; tt <= T; tt++) {
    int n, m;
    cin >> n >> m;
    int score = 0;
    fill(rhit, rhit + 105, false);
    fill(chit, chit + 105, false);
    fill(dhit, dhit + 450, false);
    el.clear();
    for (int i = 0; i < MAXN; i++)
      ai[i].clear();
    map<int, int> ans;
    map<int, int> orig;
    for (int i = 0; i < m; i++) {
      char ch;
      int r, c;
      cin >> ch >> r >> c;
      int isx = ch != '+';
      int ist = ch != 'x';
      if (isx) {
        rhit[r] = chit[c] = true;
        ans[mp(r, c)] |= 1;
        orig[mp(r, c)] |= 1;
        score++;
      }
      if (ist) {
        dhit[dm(r, c)] = dhit[dp(r, c)] = true;
        ans[mp(r, c)] |= 2;
        orig[mp(r, c)] |= 2;
        score++;
      }
    }

    int cptr = 1;
    for (int i = 1; i <= n; i++) {
      if (!rhit[i]) {
        while (chit[cptr])
          cptr++;
        rhit[i] = chit[cptr] = true;
        ans[mp(i, cptr)] |= 1;
        score++;
      }
    }

    for (int i = 110 - (n - 1); i <= 110 + n - 1; i++)
      addedge(0, i, 1);
    for (int j = 222; j <= 220 + 2 * n; j++)
      addedge(j, 1, 1);
    for (int i = 110 - (n - 1); i <= 110 + n - 1; i++)
      if (!dhit[i]) {
        const int imj = i - 110;
        for (int j = 222 + (i & 1); j <= 220 + 2 * n; j += 2) {
          const int ipj = j - 220;
          const int r = (imj + ipj) / 2;
          const int c = ipj - r;
          if (!dhit[j] && 1 <= r && r <= n && 1 <= c && c <= n)
            addedge(i, j, 1);
        }
      }
    maxflow(0, 1);
    for (int i = 0; i < (int)el.size(); i += 2) {
      const int from = el[i ^ 1].to;
      const int to = el[i].to;
      const int cap = el[i].cap;
      if (from != 0 && to != 1 && cap == 0) {
        const int imj = from - 110;
        const int ipj = to - 220;
        const int r = (imj + ipj) / 2;
        const int c = ipj - r;
        ans[mp(r, c)] |= 2;
        score++;
      }
    }

    vector<pair<int, int>> ans2;
    cout << "Case #" << tt << ": " << score << ' ';
    for (auto it : ans)
      if (it.second != orig[it.first])
        ans2.push_back(it);
    cout << ans2.size() << '\n';
    for (auto it : ans2) {
      const char ch = it.second == 3 ? 'o' : it.second == 2 ? '+' : 'x';
      cout << ch << ' ' << (it.first >> 16) << ' ' << (it.first & mask) << '\n';
    }
  }


  return 0;
}
