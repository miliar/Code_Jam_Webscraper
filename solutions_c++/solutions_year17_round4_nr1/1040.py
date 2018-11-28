#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define nfor(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define fore(i, l, r) for (int i = int(l); i < int(r); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define all(a) (a).begin(), (a).end()
#define sz(a) int((a).size())
#define pb(a) push_back(a)
#define mp(x, y) make_pair((x), (y))
#define x first
#define y second

using namespace std;

typedef long long li;
typedef long double ld;
typedef pair<int, int> pti;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

template<typename A, typename B> inline ostream& operator<< (ostream& out, const pair<A, B>& p) { return out << "(" << p.x << ", " << p.y << ")"; }
template<typename T> inline ostream& operator<< (ostream& out, const vector<T>& a) { out << "["; forn(i, sz(a)) { if (i) out << ','; out << ' ' << a[i]; } return out << " ]"; }
template<typename T> inline ostream& operator<< (ostream& out, const set<T>& a) { return out << vector<T>(all(a)); }
template<typename X, typename Y> inline ostream& operator<< (ostream& out, const map<X, Y>& a) { return out << vector<pair<X, Y>>(all(a)); }
template<typename T> inline ostream& operator<< (ostream& out, const pair<T*, int>& a) { return out << vector<T>(a.x, a.x + a.y); }

inline ld gett() { return ld(clock()) / CLOCKS_PER_SEC; }

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9, PI = 3.1415926535897932384626433832795;

#ifdef SU1
//#define GEN
#ifndef GEN
//#define LOG
#endif
#endif

const int N = 101, P = 4;

int n, p;
int a[N];

bool read() {
  if (!(cin >> n >> p)) return false;
  forn(i, n) assert(scanf("%d", &a[i]) == 1);
  return true;
}

inline void upd(int& a, int b) { if (a < b) a = b; }

int cnt[P];
int z[2][P][N][N][N];

void solve(int test) {
  printf("Case #%d: ", test + 1);

  memset(cnt, 0, sizeof(cnt));
  forn(i, n) {
    cnt[a[i] % p]++;
  }

  memset(z, -1, sizeof(z));
  z[0][0][0][0][0] = 0;
  forn(i, n) {
    int cr = i & 1, nt = cr ^ 1;
    memset(z[nt], -1, sizeof(z[nt]));
    forn(rm, p)
      forn(c0, i + 1)
      forn(c1, i - c0 + 1)
      forn(c2, i - c0 - c1 + 1) {
        int c3 = i - c0 - c1 - c2;
        assert(c3 >= 0);
        int dv = z[cr][rm][c0][c1][c2];
        if (dv == -1) continue;
#ifdef LOG
        clog << "i: " << i << " rm: " << rm << " c0: " << c0 << " c1: " << c1 <<
            " c2: " << c2 << " c3: " << c3 << " dv: " << dv << endl;
#endif
        int ct = rm == 0;
        dv += ct;

        if (c0 < cnt[0]) {
          int nrm = (rm + 0) % p;
          int& nv = z[nt][nrm][c0 + 1][c1][c2];
          upd(nv, dv);
        }
        if (c1 < cnt[1]) {
          int nrm = (rm + 1) % p;
          int& nv = z[nt][nrm][c0][c1 + 1][c2];
          upd(nv, dv);
        }
        if (c2 < cnt[2]) {
          int nrm = (rm + 2) % p;
          int& nv = z[nt][nrm][c0][c1][c2 + 1];
          upd(nv, dv);
        }
        if (c3 < cnt[3]) {
          int nrm = (rm + 3) % p;
          int& nv = z[nt][nrm][c0][c1][c2];
          upd(nv, dv);
        }
      }
  }

  int cr = n & 1;
  int ans = -1;
  forn(rm, p) ans = max(ans, z[cr][rm][cnt[0]][cnt[1]][cnt[2]]);
  assert(ans >= 0);
  cout << ans << endl;
}

int main() {
#ifdef SU1
  assert(freopen("input.txt", "rt", stdin));
  assert(freopen("output.txt", "wt", stdout));
#endif

  cout << setprecision(10) << fixed;
  cerr << setprecision(5) << fixed;

  int tc;
  cin >> tc;
  forn(tt, tc) {
    assert(read());
    ld stime = gett();
    solve(tt);
#ifdef SU1
    clog << "Test: " << tt + 1 << endl;
    cerr << "Time: " << gett() - stime << endl;
#endif
    //break;
  }

  return 0;
}
