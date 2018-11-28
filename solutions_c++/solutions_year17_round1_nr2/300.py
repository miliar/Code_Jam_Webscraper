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




struct problem_t {

  static bool check(int x, int pos) {
    return pos * 90 <= 100 * x && 100 * x <= 110 * pos;
  }
  
  static pii range(int x, int need) {
    // 90 * i * need <= 100 * x <= 110 * i * need
    // 90 * i * need <= 100 * x  =>  i <= 100 * x / (90 * need)
    // 110 * i * need >= 100 * x  =>  i >= 100 * x / (110 * need) 

    int l = (100 * x + 110 * need - 1) / (110 * need);
    int r = 100 * x / (90 * need);

    
    if (l > r) {
      return mp(l, r);
    }


    return mp(l, r);
  }

  pii intersect(const pii& a, const pii& b) {
    return mp(max(a.X, b.X), min(a.Y, b.Y));
  }

  bool is_empty(const pii& a) {
    return a.X > a.Y;
  }

  void solve(int test) {
    int n, p;
    cin >> n >> p;
    vector<int> need(n);
    for (auto& e : need) {
      cin >> e;
    }

    vector< vector<int> > a(n, vector<int>(p));
    for (auto& ingv : a) {
      for (auto& e : ingv) {
        cin >> e;
      }
      sort(ingv.begin(), ingv.end());
    }

    vector< vector<pii> > r(n);
    for (int i = 0; i < n; ++i) {
      for (auto& e : a[i]) {
        r[i].push_back(range(e, need[i]));
      }
    }

    vector<int> wave(n);

    int res = 0;
    
    while (true) {
      if (wave[0] == p) {
        break;
      }
      
      for (int i = 1; i < n; ++i) {
        while (wave[i] < p && r[i][wave[i]].Y < r[0][wave[0]].X) {
          ++wave[i];
        }
      }

      if (find(wave.begin(), wave.end(), p) != wave.end()) {
        break;
      }
      
      pii seg = r[0][wave[0]];
      for (int i = 1; i < n; ++i) {
        seg = intersect(seg, r[i][wave[i]]);
      }

      if (!is_empty(seg)) {
        ++res;

        for (int i = 0; i < n; ++i) {
          ++wave[i];
        }
      } else {
        int idx = 0;
        for (int i = 1; i < n; ++i) {
          if (r[i][wave[i]] < r[idx][wave[idx]]) {
            idx = i;
          }
        }

        wave[idx]++;
      }
    }
    

    cout << T(test) << " " << res << endl;
  }
};

void test() {
  exit(0);
}

int main() {
  ios::sync_with_stdio(false); cin.tie(0);
#ifdef _DEBUG_CMD_
  cerr << "DEBUG ENABLED" << endl;
#endif

//  test();
  
// freopen("input.txt", "r", stdin); // freopen("output.txt", "w", stdout);
// freopen(NAME ".in","r",stdin); freopen(NAME ".out","w",stdout);

  int t; cin >> t;

  for (int z = 0; z < t; ++z) {
    problem_t p;
    p.solve(z + 1);
  } 

  return 0;
}
