#include <bits/stdc++.h>

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for(int i = (int)(a); i <= (int)(b); ++i)

#define pb push_back
#define eb emplace_back

#define fi first
#define se second

#define all(v) (v).begin(), (v).end()

using namespace std;

typedef long double ld;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef vector<pii> vpi;
typedef vector<vpi> vvpi;
typedef set<pii> spi;
typedef pair<ld, ld> pld;
typedef vector<ld> vld;
typedef vector<pld> vpld;

const int inf = 1e9+100500;
const ld eps = 1e-9;
const ld pi = acosl(-1.0);

template<typename T> bool uin(T& a, T b) { if (b < a) { a = b; return true; } return false; }
template<typename T> bool uax(T& a, T b) { if (a < b) { a = b; return true; } return false; }

int di[4] = {-1, 0, 1, 0};
int dj[4] = {0, -1, 0, 1};

bool ok (const vs& a, int i, int j) {
  return i >= 0 && i < a.size() && j >= 0 && j < a[0].size();
}

void place(const vs& a, vvi& cm, int i, int j, int val) {
  forn(t, 4) {
    forn(k, a.size() + a[0].size() + 1) {
      int ni = i + di[t] * k, nj = j + dj[t] * k;
      if (!ok(a, ni, nj)) break;
      if (a[ni][nj] == '#') break;
      cm[ni][nj] |= val;
    }
  }
}

int bfs(const vs& a, const vvi& cm, vvi& used, int i, int j, int M, int m) {
  forn(i, used.size()) fill(all(used[i]), inf);
  queue<pii> Q;
  used[i][j] = 0;
  Q.push(pii(i, j));
  int r = 0;
  while (!Q.empty()) {
    i = Q.front().fi;
    j = Q.front().se;
    Q.pop();
    if (a[i][j] == '#') continue;
    int hm = cm[i][j] & m;
    r |= hm;
    if (hm == 0 && used[i][j] < M) {
      forn(t, 4) {
        int ni = i + di[t], nj = j + dj[t];
        if (!ok(a, ni, nj)) continue;
        if (uin(used[ni][nj], used[i][j] + 1)) {
          Q.push(pii(ni, nj));
        }
      }
    }
  }
  return r;
}

void solve() {
  int R, C, M;
  cin >> C >> R >> M;
  vs a(R);
  forn(i, R) cin >> a[i];
  vpi S;
  forn(i, R) forn(j, C) if (a[i][j] == 'S') S.eb(i, j);
  vpi T;
  forn(i, R) forn(j, C) if (a[i][j] == 'T') T.eb(i, j);
  vector<vvb> MST(1 << T.size());
  vvi cm(R, vi(C, 0));
  forn(t, T.size()) {
    place(a, cm, T[t].fi, T[t].se, 1 << t);
  }
  vvi used(R, vi(C, 0));
  forn(m, (1<<T.size())) {
    vvb b(S.size(), vb(T.size(), false));
    forn(i, S.size()) {
      int mm = bfs(a, cm, used, S[i].fi, S[i].se, M, m);
      forn(j, T.size()) b[i][j] = (mm >> j) & 1;
    }
    MST[m] = b;
  }
  vvi d((1<<T.size()), vi((1<<S.size()), 0));
  vvpi pd((1<<T.size()), vpi((1<<S.size()), pii(-1, -1)));
  forn(st, 1 << T.size()) {
    auto b = MST[st];
    forn(sm, 1 << S.size()) {
      forn(s, S.size()) if ((sm >> s) & 1) {
        forn(t, T.size()) if (b[s][t] && ((st >> t) & 1)) {
          if (uax(d[st][sm], 1 + d[st ^ (1 << t)][sm ^ (1 << s)])) {
            pd[st][sm] = pii(s, t);
          }
        }
      }
    }
  }

  int st = (1 << T.size()) - 1;
  int sm = (1 << S.size()) - 1;
  int res = d[st][sm];
  vpi out;
  while (d[st][sm] > 0) {
    pii r = pd[st][sm];
    out.pb(r);
    st ^= 1 << r.se;
    sm ^= 1 << r.fi;
  }
  cout << res << '\n';
  for(auto& e: out) {
    cout << e.fi+1 << ' ' << e.se+1 << '\n';
  }
}

int main() {
#ifdef HOME
  // freopen("input.txt", "r", stdin);
#endif
  cout << fixed;
  cout.precision(15);
  int T;
  cin >> T;
  forn(t, T) {
    cout << "Case #" << t + 1 << ": ";
    solve();
  }
  return 0;
}
