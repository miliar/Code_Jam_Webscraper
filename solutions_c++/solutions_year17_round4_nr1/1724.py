// {{{ Includes
#ifndef ONLINE_JUDGE
#pragma clang diagnostic warning "-Wall"
#pragma clang diagnostic warning "-Wextra"
#pragma clang diagnostic warning "-Weverything"
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
#pragma clang diagnostic ignored "-Wcomma"
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
Real isapprox(Real x, Real y, Real rtol = sqrt(numeric_limits<Real>::epsilon()), Real atol = Real(0.0), bool nans = false) { return x == y || (nans && isnan(x) && isnan(y)) || (isfinite(x) && isfinite(y) && abs(x - y) <= atol + rtol*max(abs(x), abs(y))); }
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
template <typename T> T pop(vector<T>& v) { assert(!v.empty()); T u = v.back(); v.pop_back(); return u;}
template <typename T> T pop(queue<T>& v) { assert(!v.empty()); T u = v.back(); v.pop(); return u;}
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
template <typename T> T read() { T x; cin >> x; return x; }
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
#ifdef ONLINE_JUDGE
template <typename T> dout_ &operator<<(dout_ &out, const T &thing) { return out; }
dout_ &operator<<(dout_ &out, ostream &(*thing)(ostream &)) { return out; }
#else
template <typename T> dout_ &operator<<(dout_ &out, const T &thing) { if (debug) cerr << thing; return out; }
dout_ &operator<<(dout_ &out, ostream &(*thing)(ostream &)) { if (debug) cerr << thing; return out; }
#endif

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

void solve(int casenum, outboth rout) {
  printf("==================================================% 3d\n", casenum);
  TIMING0();

  int N, P; cin >> N >> P;
  dout << db(N) << db(P) << endl;
  Vi G(N); read(G);
  dout << show(G) << endl;

  Vi counts(P);
  for (int g : G) counts[g%P]++;
  dout << show(counts) << endl;

  int ans = INT_MAX;
  if (P == 2) {
    ans = counts[0] + (counts[1] + 1) / 2;
  } else if (P == 3) {
    ans = counts[0] + min(counts[1], counts[2]) + (max(counts[1], counts[2]) - min(counts[1], counts[2]) + 2) / 3;
  }

  assert(ans != INT_MAX);
  rout << "Case #" << casenum << ": " << ans << endl;
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
    fnIn = "A.test.in";
    fnOut = "A.test.last";
    fnTest = "A.test.out";
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
  string cmd = "colordiff \"" + fnOut + "\" \"" + fnTest + "\"";
  if (access(fnTest.c_str(), F_OK) != -1) {
    cout << "Diff command: " << cmd << endl;
    int ret = system(cmd.c_str());
    cout << "Diff result: " << ret << endl;
    if (WEXITSTATUS(ret))
      cout << "[41;1;4mOUTPUT FILE DIFFERS FROM TEST FILE.[0m" << endl;
    else
      cout << "[44;1;4mdiff succeeded.[0m" << endl;
    exitcode = WEXITSTATUS(ret);
  } else {
    cout << "Diff file missing: " << fnTest << endl;
  }

  return exitcode;
}

// }}}

// clang-format off
// // compile-command: "/opt/brew/opt/llvm/bin/clang++ -fsanitize=undefined -fmodules -std=c++11 -Wall -Wextra -g -O3 -o A.O A.cc && time ./A.O A.test.in"
// // compile-command: "/opt/brew/opt/llvm/bin/clang++ -L/opt/brew/opt/llvm/lib -Wl,-rpath,/opt/brew/opt/llvm/lib -fopenmp -fmodules -std=c++11 -Wall -Wextra -g -O3 -o A.omp A.cc && time ./A.omp A.test.in"
// Local variables:
// compile-command: "make A && time ./A A.test.in"
// irony-additional-clang-options: ("-std=c++11" "-Wall" "-Wextra" "-I/opt/brew/include")
// End:
