#pragma clang diagnostic warning "-Weverything"
// {{{ Includes
#ifndef ONLINE_JUDGE
#pragma clang diagnostic warning "-Wall"
#pragma clang diagnostic warning "-Wextra"
#pragma clang diagnostic warning "-Wconversion"
#pragma clang diagnostic ignored "-Wvla"
#pragma clang diagnostic ignored "-Wvla-extension"
#pragma clang diagnostic ignored "-Wshadow"
#pragma clang diagnostic ignored "-Wc++98-compat-pedantic"
#pragma clang diagnostic ignored "-Wunused-macros"
#pragma clang diagnostic ignored "-Wmissing-prototypes"
#pragma clang diagnostic ignored "-Wsign-conversion"
#pragma clang diagnostic ignored "-Wsign-compare"
#pragma clang diagnostic ignored "-Wold-style-cast"
#pragma clang diagnostic ignored "-Wmissing-variable-declarations"
#pragma clang diagnostic ignored "-Wglobal-constructors"
#pragma clang diagnostic ignored "-Wunused-const-variable"
#pragma clang diagnostic ignored "-Wpadded"
#pragma clang diagnostic ignored "-Wfloat-equal" // it's fine
#pragma clang diagnostic ignored "-Wdouble-promotion" // also
#endif

#include <unordered_map>
#include <random>
#include <climits>
#include <array>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <queue>
#include <cstring>
#include <limits>
#include <chrono>
#include <unistd.h>
using namespace std;
// }}}
// {{{ Utilities
#ifdef ONLINE_JUDGE
static bool debug = false;
#else
static bool debug = true;
#endif
#define db(x) #x << "=" << (x) << " "
#define dprintf debug && printf

#define All(x) x.begin(), x.end()
#define Loop(i, n) for (int i = 0; i < int(n); ++i)
template <typename T, typename Q, typename S>
bool Bounded(const T &x, const Q &a, const S &b) { return a <= x && x <= b; }

typedef long double Real;
const Real pi = 4*atan(Real(1.0));
const Real Inf = numeric_limits<Real>::infinity();
// https://github.com/JuliaLang/julia/blob/master/base/floatfuncs.jl
Real isapprox(Real x, Real y, Real rtol = sqrt(numeric_limits<Real>::epsilon()), Real atol = Real(0.0), bool nans = false) {
  return x == y ||
    (nans && isnan(x) && isnan(y)) ||
    (isfinite(x) && isfinite(y) && abs(x - y) <= atol + rtol*max(abs(x), abs(y)));
}
typedef long long int ll;
typedef vector<Real> Vd;
typedef vector<int> Vi;
typedef vector<ll> Vll;
typedef vector<bool> Vb;
typedef pair<int,int> Pii;
typedef pair<ll,ll> Pll;

template <typename T> int sz(const T &x) { return (int)x.size(); }
template <typename T, typename Q> bool mem(const T &s, const Q &x) { return s.find(x) != s.end(); }
template <typename T> void push(vector<T>& c, const T& e) { c.push_back(e); }
template <typename T> void push(queue<T>& c, const T& e) { c.push(e); }
template <typename T> void push(set<T>& c, const T& e) { c.insert(e); }
template <typename T, typename... Args> auto emplace(vector<T>& c, Args&&... args) -> decltype(c.emplace_back(args...)) { c.emplace_back(args...); }
template <typename T, typename... Args> auto emplace(queue<T>& c, Args&&... args) -> decltype(c.emplace(args...)) { c.emplace(args...); }
template <typename T, typename... Args> auto emplace(set<T>& c, Args&&... args) -> decltype(c.emplace(args...)) { c.emplace(args...); }
template <typename T> void umin(T &x, const T &y) { x = min(x, y); }
template <typename T> void umax(T &x, const T &y) { x = max(x, y); }
template <typename T> int sign(const T &x) {
  return x == 0 ? 0 : x > 0 ? 1 : -1;
}
template <typename T> T square(const T &x) { return x * x; }
// }}}
// {{{ IO
template <typename S, typename T>
istream& operator>>(istream& in, pair<S, T>& p) { return in >> p.first >> p.second; }
template <typename T, typename I = typename T::iterator>
void read(T &cnt) { for (auto& x : cnt) cin >> x; }
template <typename S, typename T>
ostream& operator<<(ostream& out, const pair<S, T>& p) {
  return out << "{" << p.first << ", " << p.second << "}";
}
template <typename T> struct show_container {
  const T &container;
  show_container(const T &container_) : container(container_) {}
};
template <typename T>
ostream &operator<<(ostream &o, const show_container<T> &thing) {
  bool first = true;
  o << "{";
  for (const auto &x : thing.container) {
    if (!first)
      o << ", ";
    first = false;
    o << x;
  }
  o << "}";
  return o;
}
template <typename T> show_container<T> show(const T &container) {
  return show_container<T>(container);
}

#define dprintf debug && printf
struct dout_ { } dout;
template <typename T> dout_ &operator<<(dout_ &out, const T &thing) { if (debug) cout << thing; return out; }
dout_ &operator<<(dout_ &out, ostream &(*thing)(ostream &)) { if (debug) cout << thing; return out; }

struct outboth {
  ostream &a;
  ostream &b;
  outboth(ostream &a_, ostream &b_) : a(a_), b(b_) {}
};
template <typename T> outboth &operator<<(outboth &both, const T &thing) {
  both.a << thing;
  both.b << thing;
  return both;
}
outboth &operator<<(outboth &both, ostream &(*thing)(ostream &)) {
  both.a << thing;
  both.b << thing;
  return both;
}
// }}}
// {{{ Timing

struct ScopeTiming_impl {
  string filename, function;
  int lineno;
  string label;
  int *counter;
  chrono::time_point<std::chrono::high_resolution_clock> startTime, endTime;
  ScopeTiming_impl(string filename_ = "<no file>",
    string function_ = "<>",
    int lineno_ = -1, string label = "", int* counter_ = nullptr)
    : filename(filename_), function(function_),
      lineno(lineno_), label(label), counter(counter_)
  {
    startTime = std::chrono::high_resolution_clock::now();
  }
  ~ScopeTiming_impl() {
    if (!debug) return;
    endTime = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = endTime - startTime;
    cout << filename << ":" << lineno << ":" << function;
    if (!label.empty()) cout << ":" << label;
    if (counter) cout << "[" << ++*counter << "]";
    cout << ": Time taken: ";
    auto oldprec = cout.precision(3);
    auto oldflags = cout.setf(std::ios::fixed);
    cout << (1e3 * elapsed.count()) << "ms." << endl;
    cout.flags(oldflags);
    cout.precision(oldprec);
  }
};
#ifndef ONLINE_JUDGE
#define TIMING_1(label, c1, c2) static int counter##c1 = 0; ScopeTiming_impl timing##c2(__FILE__, __FUNCTION__, __LINE__, label, &counter##c1)
#define TIMING_(label, c1, c2) TIMING_1(label, c1, c2)
#define TIMING(label) TIMING_(label, __COUNTER__, __COUNTER__)
#define TIMING0() TIMING("")
#else
#define TIMING(label)
#define TIMING0()
#endif

// }}}
// {{{ Solver

int isvalid(const Vi& v, ll r) {
  Loop(i,sz(v)) {
    ll total = v[i];
    // dout << db(r) << show(v[i]) << db(total) << endl;
    bool possible = false;
    for (ll a = 1; a*r <= 4*total && !possible; ++a) {
      possible = total*10 >= a*r*9 && total*10 <= a*r*11;
      // if (i == 5) dout << db(a) << db(r) << db(total) << show(v) << endl;
    }
    if (!possible)
      return i;
  }
  return sz(v);
}

int isvalid(const Vi& v0, ll r0, const Vi& v1, ll r1) {
  // assert(sz(v0) == sz(v1));
  // const int n = sz(v0);
  // dout << "isvalid: " << sz(v0) << endl;
  // dout << show(v0) << show(v1) << endl;
  Loop(i,min(sz(v0), sz(v1))) {
    ll t0 = v0[i], t1 = v1[i];
    int a0 = (int)round(Real(t0) / Real(r0));
    int a1 = (int)round(Real(t1) / Real(r1));
    bool possible = false;
    for (int a = (a0+a1)/2; a <= (a0+a1+1)/2; ++a) {
      if ((t0*10 >= a*r0*9 && t0*10 <= a*r0*11) && (t1*10 >= a*r1*9 && t1*10 <= a*r1*11)) {
        possible = true;
      }
    }
    if (!possible) {
      return i;
    }
  }
  return min(sz(v0), sz(v1));
}

void solve(int casenum, outboth rout) {
  printf("==================================================% 3d\n", casenum);
  TIMING0();

  int N, P; cin >> N >> P;
  Vi R(N); read(R);
  vector<Vi> Q(N, Vi(P)); Loop(i,N) read(Q[i]);
  Loop(i,N) sort(All(Q[i]));
  dout << db(N) << db(P) << show(R) << endl;
  Loop(i,N) dout << "    " << show(Q[i]) << endl;
  int best = 0;

  // if (N == 1) {
  //   for (int s = 1; s < (1<<P); ++s) {
  //     Vi v; Loop(i,P) if (s&(1<<i)) v.push_back(Q[0][i]);
  //     umax(best, isvalid(v, R[0]));
  //   }
  // } else if (N == 2) {
  //   for (int s0 = 1; s0 < (1<<P); ++s0) {
  //     Vi v0; Loop(i,P) if (s0&(1<<i)) v0.push_back(Q[0][i]);
  //     for (int s1 = 1; s1 < (1<<P); ++s1) {
  //       Vi v1; Loop(i,P) if (s1&(1<<i)) v1.push_back(Q[1][i]);
  //       umax(best, isvalid(v0, R[0], v1, R[1]));
  //     }
  //   }
  // }

  bool finished = false;
  for (int a = 1; a <= (int)(1e9);) {
    Vi which(N, -1);
    Loop(i,N) {
      // sort(All(Q[i]));
      while (!Q[i].empty() && 10ll*Q[i][0] < 9ll*a*R[i]) {
        Q[i].erase(Q[i].begin());
      }
      for (int j = 0; j < sz(Q[i]); ++j) {
        if (10ll*Q[i][j] >= 9ll*a*R[i] && 10ll*Q[i][j] <= 11ll*a*R[i]) {
          which[i] = j;
          break;
        }
      }
      // dout << db(i) << show(Q[i]) << db(which[i]) << endl;
    }
    if (0 == std::count_if(All(which), [&](int x) { return x == -1; })) {
      Loop(i,N) {
        Q[i].erase(Q[i].begin() + which[i]);
      }
      best++;
    } else {
      ++a;
    }
    Loop(i,N) {
      if (Q[i].empty()) finished = true;
    }
    if (finished) break;
  }
  assert(finished);

  rout << "Case #" << casenum << ": " << best << endl;
}

// }}}
// {{{ Main

int main(int argc, char **argv) {
  debug = getenv("NODEBUG") == NULL;

  string fnIn, fnOut, fnTest;
  if (argc > 1) {
    fnIn = string(argv[1]);
    if (fnIn.substr(fnIn.size() - 3) == ".in") {
      fnOut = fnIn.substr(0, fnIn.size() - 3) + ".last";
      fnTest = fnIn.substr(0, fnIn.size() - 3) + ".out";
    } else {
      fnOut = fnIn + ".last";
      fnTest = fnIn + ".out";
    }
  } else {
    fnIn = "B.test.in";
    fnOut = "B.test.last";
    fnTest = "B.test.out";
  }
  cout << "Input file: " << fnIn << endl
       << "Output file: " << fnOut << endl
       << "Testing file: " << fnTest << endl;
  freopen(fnIn.c_str(), "r", stdin);
  ofstream outfile(fnOut);

  auto startTime = std::chrono::steady_clock::now();

  int T = 0;
  cin >> T;
  assert(!!cin);
  Loop(i, T) solve(i + 1, outboth(cout, outfile));

  std::chrono::duration<double> elapsed = std::chrono::steady_clock::now() - startTime;
  cout << "Time taken: [1m" << elapsed.count() << "[0m" << endl;

  int exitcode = 0;
  string cmd = "diff \"" + fnOut + "\" \"" + fnTest + "\"";
  if (access(fnTest.c_str(), F_OK) != -1) {
    cout << "Diff command: " << cmd << endl;
    int ret = system(cmd.c_str());
    cout << "Diff result: " << ret << endl;
    if (WEXITSTATUS(ret))
      cout << "[41;4mOUTPUT FILE DIFFERS FROM TEST FILE.[0m" << endl;
    else
      cout << "[44;4mdiff succeeded.[0m" << endl;
    exitcode = WEXITSTATUS(ret);
  } else {
    cout << "Diff file missing: " << fnTest << endl;
  }

  return exitcode;
}

// }}}

// clang-format off
// // compile-command: "/opt/brew/opt/llvm/bin/clang++ -fmodules -std=c++11 -Wall -Wextra -g -O3 -o B.O B.cc && time ./B.O B.test.in"
// // compile-command: "/opt/brew/opt/llvm/bin/clang++ -L/opt/brew/opt/llvm/lib -Wl,-rpath,/opt/brew/opt/llvm/lib -fopenmp -fmodules -std=c++11 -Wall -Wextra -g -O3 -o B.omp B.cc && time ./B.omp B.test.in"
// Local variables:
// compile-command: "/opt/brew/opt/llvm/bin/clang++ -fmodules -fsanitize={undefined,address} -std=c++11 -Wall -Wextra -g -o B B.cc && time ./B B.test.in"
// irony-additional-clang-options: ("-std=c++11" "-Wall" "-Wextra" "-I/opt/brew/include")
// End:
