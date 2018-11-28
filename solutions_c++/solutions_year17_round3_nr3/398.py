//#define NDEBUG

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
#include <array>

#include <sys/time.h>
#include <random>
#include <chrono>
#include <unordered_map>
#include <unordered_set>

#include <x86intrin.h>

using namespace std;
//#define DEBUG              // general information//

template<class T, class V> std::ostream&  operator <<(std::ostream& stream, const pair<T,V> & p) {
  stream << p.first << "," << p.second << " ";
  return stream;
}

template<class T> std::ostream&  operator <<(std::ostream& stream, const vector<T> & v) {
  for (auto el : v)
    stream << el << " ";
  return stream;
}

template<class T> std::ostream&  operator << (std::ostream& stream, const vector< vector<T> > & v) {
  for (auto line : v) {
    for (auto el : line)
      stream << el << " ";
    stream << "\n";
  }
  return stream;
}

class debugger {
public:
  template<class T> void output (const T& v) {
    cerr << v << " ";
  }
  
  template<class T> debugger& operator , (const T& v) {
    output(v);
    return *this;
  }
} dbg;

////////////////
// templates  //
////////////////

// general
//template size
template<typename T> int size(const T& c) { return int(c.size()); }
//template abs
template<typename T> T abs(T x) { return x < 0 ? -x : x; }
//template sqr
template<typename T> T sqr(T x) { return x*x; }
//template remin
template<typename T> bool remin(T& x, T y) { if (x <= y) return false; x = y; return true; }
//template remax
template<typename T> bool remax(T& x, T y) { if (x >= y) return false; x = y; return true; }
//template toStr
template<typename T> string toStr(T x) { stringstream ss; ss << x; return ss.str(); }
//helper len
inline int len(const string & x){ return x.length(); }
//helper print_mask
inline void print_mask(int mask, int n){for (int i = 0; i < n; ++i) cerr << (char)('0' + (mask >> i & 1));}
//helper stoi
//int stoi(const string & s){stringstream ss(s); int res; ss >> res; return res;}
//helper itos
string itos(const int & x){stringstream ss; ss << x; return ss.str();}

// types
//template int64
typedef long long            int64 ;
//template uint64
typedef unsigned long long   uint64 ;
typedef unsigned char uchar;
typedef unsigned short ushort;
typedef int64 hash_type;

// shortcuts
#define all(_xx)             _xx.begin(), _xx.end()

#define pb                   push_back
#define vl                   vector<long long>
#define vs                   vector<string>
#define vvi                  vector<vector<int>>
#define vvl                  vector<vector<long long>>
#define vd                   vector<double>
#define vvd                  vector<vector<double>>
#define vc                   vector<char>
#define vvc                  vector<vector<char>>
#define vpdd                 vector<pair<double,double> >

#define vi                   vector<int>
#define vpii                 vector<pair<int,int>> 
//#define vpii                 vector<pair<short,short> >


#define pii                  pair<int, int>
#define pcc                  pair<char, char>
#define pucc                 pair<uchar, uchar>
#define pll                  pair<long long, long long>
#define pdd                  pair<double, double>
#define mp(XX, YY)           make_pair(XX, YY)
#define fi                   first
#define se                   second

#define ll                   long long
#define ull                  unsigned long long
#define SS                   stringstream

#define ptype unsigned short

// for loops
#define re(II, NN)           for (int II(0), _NN(NN); (II) < (_NN); ++(II))
#define fod(II, XX, YY)      for (int II(XX), _YY(YY); (II) >= (_YY); --(II))
#define fo(II, XX, YY)       for (int II(XX), _YY(YY); (II) <= (_YY); ++(II))
#define foreach(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

// Useful hardware instructions
#define bitcount             __builtin_popcount
#define gcd                  __gcd

// Useful all around
#define checkbit(n,b)        ((n >> (b)) & 1)
#define pt2(b)               (1LL<<(b))
#define DREP(a)              sort(a.begin(), a.end());a.erase(unique(a.begin(), a.end()),a.end())
#define INDEX(arr,ind)       (lower_bound(arr.begin(), arr.end(),ind)-arr.begin())
#define PAUSE cerr << "Press any key to continue ..."; char xxxx; scanf("%c", &xxxx);

#define v_fill(xx,val) fill(all(xx), val)
#define m_fill(xx,val) memset(xx, val, sizeof(xx))

#define SUM(vv) accumulate(vv.begin(), vv.end(), 0)
#define oo (10001)

#define ALWAYS_INLINE inline __attribute__((always_inline))
#define ALIGNED __attribute__ ((aligned(16)))

#define likely(x)  __builtin_expect(!!(x),1)
#define unlikely(x) __builtin_expect(!!(x),0)

#define SSE_LOAD(a)    _mm_load_si128((const __m128i*)&a)
#define SSE_STORE(a, b) _mm_store_si128((__m128i*)&a, b)

ull getTicks() {
#ifdef __i386
    ull time;
    __asm__ volatile ("rdtsc" : "=A" (time));
    return time;
#else
    ull timelo, timehi;
    __asm__ volatile ("rdtsc" : "=a" (timelo), "=d" (timehi));
    return (timehi << 32) + timelo;
#endif
}

#define SUBMIT

// changed NON SUBMIT from 3.6e9 * 1.32

double convertTicks(ull time) {
#ifndef SUBMIT 
    return time / 3.3e9 * 1.23;
#else
    return time / 3.6e9 * 1.46;
#endif
}

double getTime() {
  return convertTicks(getTicks()) * 1.05;
}


struct Timer {
  ull ticks;
  const string name;
  bool running;
  int count;
  
  Timer() {;}

  Timer(string _name) : name(_name) {
    ticks = 0;
    count = 0;
    running = false;
  }

  void reset() {
    ticks = 0;
    count = 0;
    running = false; 
  }

  double elapsed() {
    return convertTicks(running ? getTicks() - ticks : ticks);
  }

  void start() {
    if (running) return;
    ticks = getTicks() - ticks;
    running = true;
  }
  
  void stop() {
    if (!running) return;
    ticks = getTicks() - ticks;
    running = false;
    count++;
  }
  
  void check() {
    double delta = elapsed();
    cerr << name << ": " << delta << " count: " << count;
    if (count) cerr << " mean per sec: " << (1 / delta) * count;
    cerr << endl;
  }

//  double elapsed() {;}
//  void startTimer() {;}
//  void stopTimer() {;}
//  void checkTimer() {;}

};

class ChronoTimer {
public:
  double start, end, total;
  
  double getTime()
  { 
    timeval tv;
    gettimeofday(&tv, 0);
    return (tv.tv_sec + tv.tv_usec * 0.000001);
  }

  void startTimer() {
    start = getTime();
  }
  
  double stopTimer() {
    double elapsed_seconds = checkTimer();
    // total += elapsed_seconds;
    // cerr << "ChronoTimer: " << elapsed_seconds << "\n";
    return elapsed_seconds;
  }
  
  double checkTimer() {
    timeval tv;
    gettimeofday(&tv, 0);
    return tv.tv_sec + tv.tv_usec * 0.000001 - start;
  }
  
  ChronoTimer() {total = 0.0; startTimer();}
};

namespace Color {
  enum Code {
    FG_RED      = 31,
    FG_GREEN    = 32,
    FG_YELLOW   = 33,
    FG_BLUE     = 34,
    FG_DEFAULT  = 39,
    BG_RED      = 41,
    BG_GREEN    = 42,
    BG_BLUE     = 44,
    BG_DEFAULT  = 49
  };
  
  class Modifier {
    Code code;
  public:
    Modifier(Code pCode) : code(pCode) {}
    friend std::ostream&
    operator<<(std::ostream& os, const Modifier& mod) {
      return os << "\033[" << mod.code << "m";
    }
  };
}

const uchar
v_white[3]  = { 255, 255, 255 }, v_black[3] = { 0, 0, 0 },     v_red[3] = { 120, 50, 80 },
v_yellow[3] = { 200, 155, 0 },   v_green[3] = { 30, 200, 70 }, v_purple[3] = { 175, 32, 186 },
v_blue[3]   = { 55, 140, 185 },  v_grey[3] = { 127, 127, 127 };

Color::Modifier green(Color::FG_GREEN);
Color::Modifier red(Color::FG_RED);
Color::Modifier yellow(Color::FG_YELLOW);
Color::Modifier blue(Color::FG_BLUE);
Color::Modifier def(Color::FG_DEFAULT);

///////////////////////////////////////////////////////////

template <class T>
pair<T, T> operator - (const pair<T, T> & a, const pair<T, T> & b) {
    return mp(a.fi - b.fi, a.se - b.se);
}

template <class T>
pair<T, T> operator + (const pair<T, T> & a, const pair<T, T> & b) {
    return mp(a.fi + b.fi, a.se + b.se);
}

template <class T, class U>
pair<T, T> operator / (const pair<T, T> & a, const U d) {
    return mp(a.fi / d, a.se / d);
}

template <class T, class U>
pair<T, T> operator * (const U d, const pair<T, T> & a) {
    return mp(a.fi * d, a.se * d);
}

///////////////////////////////////////////////////////////

void SSE_CLEAR(const char * v, int size) {
    auto zero = _mm_set1_epi8 (0);
    for (int k = 0; k < size; k += 16) {
        SSE_STORE(v[k], zero);
    }
}

void SSE_CLEAR(const short * v, int size) {
    auto zero = _mm_set1_epi16 (0);
    for (int k = 0; k < size; k += 8) {
        SSE_STORE(v[k], zero);
    }
}

void SSE_CLEAR(const int * v, int size) {
    auto zero = _mm_set1_epi32 (0);
    for (int k = 0; k < size; k += 4) {
        SSE_STORE(v[k], zero);
    }
}

void SSE_COPY(const char * v, const char * to, int size) {
    for (int i = 0; i < size; i += 16) {
      __m128i m = SSE_LOAD(v[i]);
      SSE_STORE(to[i], m);
    }
}

void SSE_COPY(const short * v, const short * to, int size) {
    for (int i = 0; i < size; i += 8) {
      __m128i m = SSE_LOAD(v[i]);
      SSE_STORE(to[i], m);
    }
}
////////////////////////////////////////////////////////////

template <typename T>
vector<T> join_vector(const vector<T> & left, const vector<T> & right) {
    auto res = vector<T>(left);
    res.insert(res.end(), all(right));
    return res;
}

template <typename T>
void concat_vector(vector<T> & left, const vector<T> & right) {
    left.insert(left.end(), all(right));
}

template <typename T>
T sum_vector(vector<T> & v) {
    return accumulate(all(v), 0);
}

template <typename T>
T mean_vector(vector<T> & v) {
    return sum_vector(v) / size(v);
}

vi string_to_vector(const string & s) {
  vi res; for (auto c : s) res.pb(c); return res;
}

/////////////////////////////////////////////////////////////

mt19937 random_engine;

ALWAYS_INLINE double nextDouble() {return 1.0 * (random_engine() % (1<<30) + 1) / ((1<<30)-1);}
ALWAYS_INLINE int nextInt() {return random_engine();}
ALWAYS_INLINE int nextInt(int range) {return random_engine() % range;}
ALWAYS_INLINE int nextInt(int first, int last) {return random_engine() % (last - first + 1) + first;}

/////////////////////////////////////////////////////////////

struct RNG {
  unsigned int x = 123456789;
  unsigned int y = 362436069;
  unsigned int z = 521288629;
  
    unsigned int rand() {
    x ^= x << 16;
    x ^= x >> 5;
    x ^= x << 1;

    unsigned int t = x;
    x = y;
    y = z;
    z = t ^ x ^ y;

    return z;   
    }
    
    inline int nextInt(int x) {
        return rand() % x;
    }
    
    inline int nextInt(int a, int b) {
        return a + (rand() % (b - a + 1));
    }
    
    inline double nextDouble() {
        return (rand() + 0.5) * (1.0 / 4294967296.0);
    }
};

static RNG rng;
////////////////////////////////////////////////////////////
double dist_l2 (const pii& A, const pii& B) {
  return hypot (1.0 * A.fi - B.fi, 1.0 * A.se - B.se);
}

template<typename T>
pair<double, double> computeMeanVariance (const vector<T>& v) {
  pair<double, double> result;
  for (const auto& x : v) {
    result.fi += x;
  } 
  result.fi /= size(v);
  for (const auto& x : v) {
    result.se += sqr(x - result.fi);
  }
  result.se = sqrt(result.se / size(v));
  return result;
}

////// START
int N, K;
vd P;
double U;

double solve() {
  double best_prob = 0.0;

  sort (all(P));

  while (true) {
    bool found = false;
    re (i, N - 1) {
      if (P[i] < P[i + 1] - 1e-9) {
        found = true;
        double delta = P[i + 1] - P[i];
        if (U >= delta - 1e-9) {
          U -= delta;
          P[i] = P[i + 1];
          remax (U, 0.0);
        } else {
          P[i] += U;
          goto end_while;
        }
        break;
      }
    }

    if (!found) {
      // all equal
      double sprinkle = U / N;
      re (i, N) {
        P[i] += sprinkle;
        assert (P[i] <= 1.0);
      }
      break;
    }
  }

  end_while:;

  double result = 1.0;
  re (i, N)
    result *= P[i];
  return result;
}

double solve_int() {
  vi prob (N);
  re (i, N) {
    prob[i] = 10000 * P[i];
  }
  int budget = int (U * 10000);

  sort (all(prob));

  while (budget) {
    bool found = false;
    re (i, N - 1) {
      if (prob[i] < prob[i + 1]) {
        found = true;
        int delta = prob[i + 1] - prob[i];
        if (budget >= delta) {
          budget -= delta;
          prob[i] = prob[i + 1];
        } else {
          prob[i] += budget;
          goto end_while;
        }
        break;
      }
    }

    if (!found) {
      // all equal
      // sort (all(prob));
      // reverse (all(prob));
      U = 1.0 * budget / 10000.0;
      double sprinkle = U / N;
      re (i, N) {
        P[i] = prob[i] / 10000.0;
        P[i] += sprinkle;
        assert (P[i] <= 1.0);
      }
      
      double result = 1.0;
      re (i, N)
        result *= P[i];
      return result;
    }
  }

  end_while:;
  // sort (all(prob));
  // reverse (all(prob));
  double result = 1.0;
  re (i, N) {
    result *= prob[i] / 10000.0;
  }
  return result;
}

double solve_iter() {
  const int max_iter = 10000000;
  double delta = U / max_iter;
  re (iter, max_iter) {
    sort (all(P));
    P[0] += delta;
  }
  double result = 1.0;
  re (i, N)
    result *= P[i];
  return result;
}

int main() {
  int T;
  cin >> T;

  re (t, T) {
    cin >> N >> K >> U;
    P.resize(N);
    re (i, N)
      cin >> P[i];
    printf("Case #%d: %.12lf\n", t + 1, solve_iter()); 
  }

  return 0;
}

