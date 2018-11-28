//{{{ includes
#include <algorithm>
#include <chrono>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <memory>
#include <numeric>
#include <type_traits>
#include <utility>

#include <cassert>
#include <cinttypes>
#include <cstdio>
#include <cmath>

#include <array>
#include <deque>
#include <list>
#include <map>
#include <experimental/optional>
#include <set>
#include <stack>
#include <string>
#include <tuple>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;
using experimental::optional;
//}}}

//{{{ types
typedef int_fast64_t ll;
typedef int_fast32_t ii;
typedef vector<ii> vii;
typedef vector<ll> vll;
typedef vector<vii> vvii;
typedef vector<vll> vvll;
typedef set<ii> sii;
typedef set<ll> sll;
//}}}

//{{{ aliases
#define len(x) (x).size()
#define itall(x) (x).begin(), (x).end()
#define ritall(x) (x).rbegin(), (x).rend()
#define pb push_back
#define fst(x) (x).first
#define snd(x) (x).second
#define mp(a, b) make_pair((a), (b))
#define bains(x) back_inserter((x))
#define fold accumulate
#define fmap transform
#define zipWith transform
#define scanl1 partial_sum

#define isit istream_iterator
#define cini(type, i) \
  isit<type> i(cin); isit<type> eo ## i;
#define isitall(x) (x), (eo ## x)
#define osit ostream_iterator

#define rep(i, lo, hi) \
  for (typename common_type<decltype(lo), decltype(hi)>::type i = (lo); i <= (hi); i++)
#define repr(i, lo, hi) \
  for (typename common_type<decltype(lo), decltype(hi)>::type i = (hi); i >= (lo); i--)
#define repn(zzz, hi) \
  for (decltype(hi) zzz = 1; zzz <= hi; zzz++)

#define inf 1000000000
#define infll (2000000000000000000L)
//}}}

//{{{ util functions
template<class II, class SZ, class OI>
OI cpy_n(II _i, SZ _s, OI _o) {
  repn(_j, _s) {*(_o++) = *_i; if (_j != _s) {_i++;}}; return _o;
}
#define copy_n cpy_n // actual copy_n has uncertain behavior
template<class T> void slurp(vector<T> & v, ii n = inf) {cini(T, i); if (n == inf) {copy(isitall(i), bains(v));} else {v.reserve(n); copy_n(i, n, bains(v));}}
template<class T, class U> void slurp2(vector<T> & va, vector<U> & vb, ii n = inf) {cini(T, a); cini(U, b); if (n != inf) {va.reserve(n); vb.reserve(n);} auto ao = bains(va); auto bo = bains(vb); repn(i, n) {if (a == eoa) break; *(ao++) = *a; *(bo++) = *b; if (i != n) {a++; b++;} }}
//}}}
//{{{
chrono::time_point<chrono::system_clock> start_time;

#define MULTIPLE_TESTCASES
#define OUTPUT_CASE_NUMBERS
//}}}

//{{{ personal libraries
//
//{{{ slurpn
//}}} slurpn
//
//{{{ trie
//}}} trie
//
//{{{ segtree
//}}} segtree
//
//}}}

// --------------------------------------------------------------------------

void do_it() {
  ii n, c, m;
  cin >> n >> c >> m;
  ii a = 0, b = 0;
  vii apos(n), bpos(n);
  repn(zzz, m) {
    ii pos, buyer;
    cin >> pos >> buyer;
    if (buyer == 1) {
      a++;
      apos[pos-1]++;
    } else {
      b++;
      bpos[pos-1]++;
    }
  }
  ii proms = 0;
  ii rides = 0;
  rep(i, 0, n-1) {
  while (apos[i] && bpos[i]) {
    if (a > apos[i]) {
      bpos[i]--; b--;
      ii max_conf = -1;
      ii max_conf_idx = -1;
      rep(j, 0, n-1) {
        if (i == j) {
          continue;
        }
        if (apos[j]) {
          if (min(apos[j], bpos[j]) > max_conf) {
            max_conf = min(apos[j], bpos[j]);
            max_conf_idx = j;
          }
        }
      }
      apos[max_conf_idx]--;
      a--;
      rides++;
    } else if (b > bpos[i]) {
      apos[i]--; a--;
      ii max_conf = -1;
      ii max_conf_idx = -1;
      rep(j, 0, n-1) {
        if (i == j) {
          continue;
        }
        if (bpos[j]) {
          if (min(apos[j], bpos[j]) > max_conf) {
            max_conf = min(apos[j], bpos[j]);
            max_conf_idx = j;
          }
        }
      }
      bpos[max_conf_idx]--;
      b--;
      rides++;
    } else {
      a--; b--;
      apos[i]--; bpos[i]--;
      if (i == 0) {
        rides += 2;
      } else {
        rides += 1;
        proms += 1;
      }
    }
  }
  }
  rides += max(a, b);
  cout << rides << " " << proms;
}
// --------------------------------------------------------------------------

//{{{ boilerplate running code
void start() {
  start_time = chrono::system_clock::now();
}

void end() {
  chrono::time_point<chrono::system_clock> end_time;
  end_time = chrono::system_clock::now();
  chrono::duration<double> diff = end_time - start_time;
  cerr << fixed << setprecision(4) << diff.count() << "s" << endl;
}

void do_mult() {
  ii times;
  cin >> times;
  repn(i, times) {
#ifdef OUTPUT_CASE_NUMBERS
    cout << "Case #" << i << ": ";
#endif
    do_it();
    cout << endl;
  }
}

int main(int argc, char * argv[]) {
  ios::sync_with_stdio(false);
  start();
#ifdef MULTIPLE_TESTCASES
  do_mult();
#else
  do_it();
  cout << endl;
#endif
  end();
  return 0;
}
//}}}
