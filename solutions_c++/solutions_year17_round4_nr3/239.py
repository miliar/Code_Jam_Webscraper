#define NAME "problem"
// #undef _DEBUG_CMD_

#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <fstream>
#include <functional>
#include <iostream>
#include <iterator>
#include <list>
#include <limits>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <tuple>
#include <type_traits>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

//////////// begin-of-template

using LL = long long;
using LD = long double;
using pii = pair<int, int>;
using veci = vector<int>;
using vecii = vector<veci>;

const LD eps = 1e-9;
const LD pi = acos(-1.0);
const int inf = 1000 * 1000 * 1000;
const LL inf64 = LL(inf) * inf;

#define mp make_pair
#define mt make_tuple
#define pb push_back
#define X first
#define Y second

template<typename C, typename = typename C::iterator, typename = typename enable_if<!is_same<string, C>::value>::type> ostream& operator<<(ostream& o, const C& c);
template<typename X, typename Y> ostream& operator<<(ostream& o, const pair<X, Y>& p) { return o << "<" << p.first << ", " << p.second << ">"; }
template<class T, size_t... Is> void _print_tuple(ostream& o, const T& t, index_sequence<Is...>) { bool _[] {0, (bool)(o << (Is > 0 ? ", " : "") << get<Is>(t))...}; (void)_; }
template<typename... T> ostream& operator<<(ostream& o, const tuple<T...>& t) { o << "<"; _print_tuple(o, t, make_index_sequence<sizeof...(T)>()); return o << ">"; }
template<typename T> struct _brackets { template<typename C> static string _(typename C::key_type*) { return "{}"; } template<typename C> static string _(...) { return "[]"; } static string get() { return _<T>(0); } };
template<typename C, typename, typename> ostream& operator<<(ostream& o, const C& c) { bool f = 1; o << _brackets<C>::get()[0]; for (const auto& item : c) { if (!f) { o << ", "; } f = 0; o << item; } return o << _brackets<C>::get()[1]; }
template<typename... Ts> string to_str(Ts... t) { ostringstream os; bool _[] = {0, (bool)(os << t)...}; (void)_; return os.str(); }
template<typename T> T from_str(const string& s) { istringstream is(s); T t; is >> t; return t; }
string T(int test) { return to_str("Case #", test, ":"); }
#define cmp_field(field) [](const auto& lhs, const auto& rhs) { return lhs.field < rhs.field; }

#ifdef _DEBUG_CMD_
#define _dbg(x) do { cerr << #x << "=" << x << "; "; } while (0)
#define _name(name, _1, _2, _3, _4, N, ...) name ## N 
#define _dbg1(x) _dbg(x)
#define _dbg2(x, ...) _dbg(x); _dbg1(__VA_ARGS__)
#define _dbg3(x, ...) _dbg(x); _dbg2(__VA_ARGS__)
#define _dbg4(x, ...) _dbg(x); _dbg3(__VA_ARGS__)
#define dbg(...) do { _name(_dbg, __VA_ARGS__, 4, 3, 2, 1, 0)(__VA_ARGS__); cerr << endl; } while (0)
#else
#define dbg(...)
#endif
#define check_in() do { if (cin.fail()) { return; } } while (0)
/////////// end-of-template


const int dx[] = {-1, 0, 1, 0};
const int dy[] = {0, 1, 0, -1};

struct problem_t {
  int r, c;
  vector<string> a;

  vector<vector<vector<pair<pii, int>>>> who;

  bool in_field(const pii& p) {
    return p.X >= 0 && p.Y >= 0 && p.X < r && p.Y < c;
  }
  
  pii move_pt(const pii& p, int dir) {
    return {p.X + dx[dir], p.Y + dy[dir]};
  }

  int rotate(const pii& , int dir, char ch) {
    if (ch == '/') {
      return dir ^ 1;
    } else {
      return (3 + (((dir + 1) % 4) ^ 1)) % 4;
    }
  }

  vector<vector<vector<int>>> take;
  // - 0
  // | 1

  int get_t(char ch) {
    return ch == '-' ? 0 : 1;
  }
  char get_c(int t) {
    return t == 0 ? '-' : '|';
  }
  
  bool propagate(int x, int y) {
    assert(a[x][y] == '-' || a[x][y] == '|');

    vector<vector<vector<int>>> d(r, vector<vector<int>>(c, vector<int>(4)));

    queue<pair<pii, int>> q;

    const pii origin = {x, y};

    {
      int dir;
      if (a[x][y] == '|') {
        dir = 0;
      } else {
        dir = 1;
      }

      for (int i = 0; i <= 2; i += 2) {
        auto np = move_pt(origin, dir + i);
        q.emplace(np, dir + i);
      }
    }
    
    while (!q.empty()) {
      pii cur = q.front().X;
      int dir = q.front().Y;
      q.pop();


      if (!in_field(cur)) {
        continue;
      }
      if (d[cur.X][cur.Y][dir]) {
        continue;
      }

      char ch = a[cur.X][cur.Y];
      
      if (ch == '#') {
        continue;
      }
      
      d[cur.X][cur.Y][dir] = 1;


      if (ch == '|' || ch == '-') {
        return false;
      }

      if (ch == '/' || ch == '\\') {
        int ndir = rotate(cur, dir, ch);
        q.emplace(move_pt(cur, ndir), ndir);
        continue;
      }

      assert(ch == '.');
      q.emplace(move_pt(cur, dir), dir);
    }

    for (int i = 0; i < r; ++i) {
      for (int j = 0; j < c; ++j) {
        if (a[i][j] == '.' && (d[i][j][0] || d[i][j][1] || d[i][j][2] || d[i][j][3])) {
          who[i][j].emplace_back(make_pair(pii{x, y}, get_t(a[x][y])));
        }
      }
    }

    
    if (0) {
      dbg(x, y, a[x][y]);
    
      for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
          if (i == x && j == y) {
            cout << "o";
          } else if (a[i][j] == '.') {
            if (d[i][j][0] || d[i][j][2]) {
              cout << "|";
            } else if (d[i][j][1] || d[i][j][3]) {
              cout << "-";
            } else {
              cout << a[i][j];
            }
          } else {
            cout << a[i][j];
          }
        }
        cout << endl;
      }
    }
    return true;
  }

  bool go(int x, int y) {
    if (y == c) {
      return go(x + 1, 0);
    }
    if (x == r) {
      return true;
    }

    if (a[x][y] != '.') {
      return go(x, y + 1);
    }

    for (auto& e : who[x][y]) {
      if (take[e.X.X][e.X.Y][e.Y]) {
        return go(x, y + 1);
      }
    }

//    dbg(x, y, who[x][y]);
    for (auto& e : who[x][y]) {
      auto& tt = take[e.X.X][e.X.Y];
      if (tt[0] || tt[1]) {
        continue;
      }
      tt[e.Y] = 1;
//      dbg("take", e);
      if (go(x, y + 1)) {
        return true;
      }
      tt[e.Y] = 0;
    }
    return false;
  }

  
  void solve(int test) {
    cin >> r >> c;
    a.resize(r);
    for (auto& e : a) {
      cin >> e;
    }


    who = vector< vector<vector<pair<pii, int>>>>(r, vector<vector<pair<pii, int>>>(c));
    for (int i = 0; i < r; ++i) {
      for (int j = 0; j < c; ++j) {
        if (a[i][j] == '|' || a[i][j] == '-') {
          bool ok = false;
          char chok = 'x';
          for (char ch : {'-', '|'}) {
            a[i][j] = ch;
            if (propagate(i, j)) {
              chok = ch;
              ok = true;
            }
          }
          
          if (!ok) {
            dbg("bad laser");
            cout << T(test) << " IMPOSSIBLE" << endl;
            return;
          }
          a[i][j] = chok;
        }
      }
    }

    for (int i = 0; i < r; ++i) {
      for (int j = 0; j < c; ++j) {
        if (a[i][j] == '.' && who[i][j].empty()) {
          dbg("no who", i, j, a[i][j]);
          cout << T(test) << " IMPOSSIBLE" << endl;
          return;
        }
      }
    }

    take = vector< vector<vector<int>>>(r, vector<vector<int>>(c, vector<int>(2)));

    if (go(0, 0)) {
      cout << T(test) << " POSSIBLE" << endl;
      for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
          for (int t = 0; t < 2; ++t) {
            if (take[i][j][t]) {
              a[i][j] = get_c(t);
            }
          }
        }
      }

      for (int i = 0; i < r; ++i) {
        cout << a[i] << endl;
      }
      
    } else {
      cout << T(test) << " IMPOSSIBLE" << endl;
    }
  }
};


int main() {
  ios::sync_with_stdio(false); cin.tie(0);
#ifdef _DEBUG_CMD_
  cerr << "DEBUG ENABLED" << endl;
#endif
  
// freopen("input.txt", "r", stdin); // freopen("output.txt", "w", stdout);
// freopen(NAME ".in","r",stdin); freopen(NAME ".out","w",stdout);

  int t; cin >> t;

  for (int z = 0; z < t; ++z) {
    problem_t p;
    p.solve(z + 1);
  } 

  return 0;
}
