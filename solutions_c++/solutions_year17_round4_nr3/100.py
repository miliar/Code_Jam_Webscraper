#define NDEBUG
#include <bitset>
#include <cassert>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <set>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
using namespace std;

struct Point;
namespace dbg_impl_detail {
string str(const Point& p);
}
#define MINUSONE(v) memset((v), -1, sizeof (v))
namespace dbg_impl_detail {
  template<typename Container> std::string str_list(const Container& c);
  template<typename Container> std::string str_set(const Container& c);
  template<typename Container> std::string str_map(const Container& c);

  template<typename T> std::string str(const T& val) { return std::to_string(val); }
  template<> std::string str(const std::string& val) { return '"' + val + '"'; }
  template<typename T> std::string str(const std::vector<T>& v) { return str_list(v); }
  template<typename T> std::string str(const std::deque<T>& v) { return str_list(v); }
  template<typename T> std::string str(const std::list<T>& v) { return str_list(v); }
  template<typename T, typename C> std::string str(const std::set<T, C>& v) { return str_set(v); }
  template<typename T, typename C> std::string str(const std::multiset<T, C>& v) { return str_set(v); }
  template<typename T, typename H> std::string str(const std::unordered_set<T, H>& v) { return str_set(v); }
  template<typename T, typename H> std::string str(const std::unordered_multiset<T, H>& v) { return str_set(v); }
  template<typename K, typename V, typename C> std::string str(const std::map<K, V, C>& v) { return str_map(v); }
  template<typename K, typename V, typename C> std::string str(const std::multimap<K, V, C>& v) { return str_map(v); }
  template<typename K, typename V, typename H> std::string str(const std::unordered_map<K, V, H>& v) { return str_map(v); }
  template<typename K, typename V, typename H> std::string str(const std::unordered_multimap<K, V, H>& v) { return str_map(v); }
  template<size_t N> std::string str(const std::bitset<N>& v) { std::string ret; for (size_t i=0; i<N; ++i) { ret += char('0'+v.test(i)); } return ret; }
  template<typename T, typename U> std::string str(const std::pair<T, U>& val) {
    return '(' + str(val.first) + ", " + str(val.second) + ')';
  }
  template<typename T> std::string str(const std::complex<T>& val) {
    return '(' + str(std::real(val)) + ", " + str(std::imag(val)) + ')';
  }

  template<typename Container, typename Callback>
  std::string str_container(const Container& c, const char* brackets, Callback&& cb) {
    std::string ret(1, brackets[0]);
    for (auto it = c.begin(); it != c.end(); ++it) {
      if (it != c.begin()) ret += ", ";
      ret += cb(it);
    }
    return ret += brackets[1];
  }
  template<typename Container> std::string str_list(const Container& c) {
    return str_container(c, "[]", [](typename Container::const_iterator it) { return str(*it); } );
  }
  template<typename Container> std::string str_set(const Container& c) {
    return str_container(c, "{}", [](typename Container::const_iterator it) { return str(*it); } );
  }
  template<typename Container> std::string str_map(const Container& c) {
    return str_container(c, "{}", [](typename Container::const_iterator it) { return str(it->first) + ": " + str(it->second); } );
  }
}

#ifndef NDEBUG
#define DBG_1(x) #x << " = " << dbg_impl_detail::str(x)
#define DBG_2(x, ...) DBG_1(x) << ", " << DBG_1(__VA_ARGS__)
#define DBG_3(x, ...) DBG_1(x) << ", " << DBG_2(__VA_ARGS__)
#define DBG_4(x, ...) DBG_1(x) << ", " << DBG_3(__VA_ARGS__)
#define DBG_5(x, ...) DBG_1(x) << ", " << DBG_4(__VA_ARGS__)
#define DBG_6(x, ...) DBG_1(x) << ", " << DBG_5(__VA_ARGS__)
#define DBG_7(x, ...) DBG_1(x) << ", " << DBG_6(__VA_ARGS__)
#define DBG_8(x, ...) DBG_1(x) << ", " << DBG_7(__VA_ARGS__)
#define DBG_GET_MACRO(_1,_2,_3,_4,_5,_6,_7,_8,NAME,...) NAME
#define dbg(...) do { std::cerr << DBG_GET_MACRO(__VA_ARGS__,DBG_8,DBG_7,DBG_6,DBG_5,DBG_4,DBG_3,DBG_2,DBG_1)(__VA_ARGS__) << std::endl; } while (0)
#else
#define dbg(...) (void)0
#endif

const int MAX = 53;

int R, C;
char grid[MAX][MAX];

const int dy[4] = {-1, 0, 1, 0};
const int dx[4] = {0, 1, 0, -1};
struct Point {
  int y, x;
  Point() { }
  Point(int y, int x) : y(y), x(x) { }
  static Point invalid() { return Point(-1, -1); }
  bool operator==(const Point& o) const { return x == o.x && y == o.y; }
  bool operator!=(const Point& o) const { return !(*this == o); }
};
namespace dbg_impl_detail {
string str(const Point& p) {
  char buf[50];
  sprintf(buf, "(y=%d, x=%d)", p.y, p.x);
  return buf;
}
}
Point move(Point p, int dir) {
  return Point(p.y + dy[dir], p.x + dx[dir]);
}
bool valid(Point p) {
  return p.y >= 0 && p.y < R && p.x >= 0 && p.x < C;
}

pair<Point, int> sim(const Point init, const int init_dir) {
  Point p = init;
  int dir = init_dir;
  while (1) {
    p = move(p, dir);
    if (!valid(p) || grid[p.y][p.x] == '#') {
      return make_pair(Point::invalid(), -1);
    }
    if (grid[p.y][p.x] == 's') {
      return make_pair(p, dir % 2);
    }
    if (p == init && dir == init_dir) {
      return make_pair(Point::invalid(), -1);
    }
    if (grid[p.y][p.x] == '/') {
      dir ^= 1;
    }
    if (grid[p.y][p.x] == '\\') {
      dir ^= 3;
    }
  }
}

static int shooter_state[MAX][MAX];
void try_set(Point p, int dir) {
  assert(dir < 2);
  auto& ref = shooter_state[p.y][p.x];
  if (ref != -1 && ref != dir) {
    throw 1;
  }
  ref = dir;
}

vector<pair<Point, int> > imps[MAX][MAX][2];
void dfs(Point var, int val, vector<Point>& rollback) {
  if (shooter_state[var.y][var.x] != -1) {
    if (shooter_state[var.y][var.x] != val) {
      throw 1;
    }
    return;
  }

  shooter_state[var.y][var.x] = val;
  rollback.push_back(var);
  for (const auto& i : imps[var.y][var.x][val]) {
    dfs(i.first, i.second, rollback);
  }
}

void solve() {
  cin >> R >> C;
  for (int y = 0; y < R; ++y) {
    cin >> grid[y];
    for (int x = 0; x < C; ++x) {
      if (grid[y][x] == '|' || grid[y][x] == '-') {
        grid[y][x] = 's';
      }
      imps[y][x][0].clear();
      imps[y][x][1].clear();
    }
  }

  MINUSONE(shooter_state);
  for (int y = 0; y < R; ++y) {
    for (int x = 0; x < C; ++x) {
      if (grid[y][x] == 's') {
        for (int dir = 0; dir < 4; ++dir) {
          pair<Point, int> s = sim(Point(y, x), dir);
          if (s.second != -1) {
            dbg(Point(y, x), !(dir % 2));
            try_set(Point(y, x), !(dir % 2));
          }
        }
      }
    }
  }

  for (int y = 0; y < R; ++y) {
    for (int x = 0; x < C; ++x) {
      if (grid[y][x] != '.') {
        continue;
      }
      vector<pair<Point, int> > options;
      for (int dir = 0; dir < 4; ++dir) {
        pair<Point, int> rv = sim(Point(y, x), dir);
        if (rv.second != -1) {
          Point s = rv.first;
          int st = shooter_state[s.y][s.x];
          if (st == -1 || st == rv.second) {
            options.push_back(rv);
          }
        }
      }
      assert(options.size() <= 2);
      switch (options.size()) {
      case 0: throw 1;
      case 1: {
        try_set(options.back().first, options.back().second);
        break;
      }
      case 2: {
        const auto& o1 = options[0];
        const auto& o2 = options[1];
        imps[o1.first.y][o1.first.x][!o1.second].push_back(o2);
        imps[o2.first.y][o2.first.x][!o2.second].push_back(o1);
      }
      }
    }
  }

  vector<Point> rollback;
  for (int y = 0; y < R; ++y) {
    for (int x = 0; x < C; ++x) {
      if (grid[y][x] == 's') {
        rollback.clear();
        const Point var(y, x);
        int& ref = shooter_state[var.y][var.x];
        if (ref != -1) {
          int pre = ref;
          ref = -1;
          dfs(var, pre, rollback);
        } else {
          try {
            rollback.clear();
            dfs(var, 0, rollback);
          } catch (...) {
            while (!rollback.empty()) {
              shooter_state[rollback.back().y][rollback.back().x] = -1;
              rollback.pop_back();
            }
            dfs(var, 1, rollback);
          }
        }
        grid[y][x] = "|-"[ref];
      }
    }
  }

  cout << "POSSIBLE\n";
  for (int y = 0; y < R; ++y) {
    cout << grid[y] << '\n';
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  int T;
  cin >> T;
  for (int tt=1; tt<=T; ++tt) { // caret here
    cout << "Case #" << tt << ": ";
    try {
      solve();
    } catch (...) {
      cout << "IMPOSSIBLE\n";
    }
    cout << flush;
  }
}
