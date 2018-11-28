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
  ii n, p;
  vii gs;
  cin >> n >> p;
  slurp(gs, n);
  ii left = 0;
  vii ps(p);
  for (auto e : gs) {
    ps[e % p]++;
  }
  ii acc = ps[0];
  ps[0] = 0;
  n -= acc;
  for (; n > 0; n--) {
    if (left == 0) {
      acc++;
    }
    if (p == 2) {
      ps[1]--;
      left += 1;
      left %= p;
    } else if (p == 3) {
      if (ps[1] > 0 && ps[2] > 0) {
        ps[1]--;
        ps[2]--;
        n--;
      } else if (ps[1] > 2) {
        ps[1] -= 3;
        n -= 2;
      } else if (ps[2] > 2) {
        ps[2] -= 3;
        n -= 2;
      } else {
        n = 0;
      }
    } else { /* p == 4 */
      rep(i, 1, p-1) {
        if (ps[i] <= 0) {
          continue;
        }
        rep(j, 1, p-1) {
          if (ps[j] <= 0 || (i == j && ps[j] <= 1)) {
            continue;
          }
          if (i + j == p) {
            n--;
            ps[i]--;
            ps[j]--;
            goto out4;
          }
        }
      }
      if (ps[2] > 0 && ps[1] > 1) {
        n -= 2;
        ps[2]--;
        ps[1] -= 2;
        goto out4;
      }
      if (ps[2] > 0 && ps[3] > 1) {
        n -= 2;
        ps[2]--;
        ps[3] -= 2;
        goto out4;
      }
      if (ps[1] > 3) {
        n -= 3;
        ps[1] -= 4;
        goto out4;
      }
      if (ps[3] > 3) {
        n -= 3;
        ps[3] -= 4;
        goto out4;
      }
      n = 0;
out4:
      ;
    }
  }
done:
  cout << acc;
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
