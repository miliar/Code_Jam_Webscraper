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
  enum OP {
    ATTACK = 1,
    BUFF = 2,
    CURE = 3,
    DEBUFF = 4,
  };
  
  int simulate(int hd, int ad, int hk, int ak, int b, int d, int cnt_d, int cnt_b) {
    int health = hd;

    OP prev_op = OP::CURE;
    auto prev_st = make_tuple(-1, -1, -1, -1);
    
    int step = 0;
    while (true) {
      ++step;
      auto st = make_tuple(health, ad, hk, ak);
      if (prev_st == st) {
        return -1;
      }
      prev_st = st;

      if (ad >= hk) {
        hk -= ad;
        prev_op = OP::ATTACK;
        return step;
      }
      
      // dbg(health, ad, hk, ak);
      if (health <= ak - d * (cnt_d > 0)) {
        health = hd;
        prev_op = OP::CURE;
      } else {
        if (cnt_d > 0 && ak > 0) {
          prev_op = OP::DEBUFF;
          --cnt_d;
          ak -= d;
          if (ak < 0) {
            ak = 0;
          }
        } else if (cnt_b > 0 && ad < hk) {
          prev_op = OP::BUFF;
          --cnt_b;
          ad += b;
        } else {
          prev_op = OP::ATTACK;
          hk -= ad;
          if (hk <= 0) {
            return step;
          }
        }
      }

      // dbg(step, prev_op);

      assert(hk > 0);
      health -= ak;
      if (health <= 0) {
        return -1;
      }
    }

    return step;
  }

  void solve(int test) {
    int hd, ad, hk, ak, b, d;

    cin >> hd >> ad >> hk >> ak >> b >> d;

    // dbg(simulate(hd, ad, hk, ak, b, d, 0, 0));
    // exit(0);

    int res = -1;
    for (int cnt_d = 0; cnt_d <= 200; ++cnt_d) {
      for (int cnt_b = 0; cnt_b <= 200; ++cnt_b) {
        auto cur = simulate(hd, ad, hk, ak, b, d, cnt_d, cnt_b);
        if (cur != -1) {
          if (res == -1 || res > cur) {
            res = cur;
          }
        }
      }
    }

    if (res == -1) {
      cout << T(test) << " IMPOSSIBLE" << endl;
    } else {
      cout << T(test) << " " << res << endl;
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
