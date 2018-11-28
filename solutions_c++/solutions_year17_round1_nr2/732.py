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

ii min_can_make(ii avail, ii each) {
  each *= 11;
  avail *= 10;
  ii k = avail / each;
  if (k * each >= avail) {
    return max(k, (ii) 1);
  }
  k++;
  if (k * each >= avail) {
    return max(k, (ii) 1);
  }
  return inf;
}

ii max_can_make(ii avail, ii each) {
  each *= 9;
  avail *= 10;
  ii k = avail / each + 1;
  if (k * each <= avail) {
    return k;
  }
  k--;
  if (k * each <= avail) {
    return k;
  }
  return -1;
}

void do_it() {
  ii ingn, packsn;
  vii ings;
  cin >> ingn;
  cin >> packsn;
  slurp(ings, ingn);
  vvii packs(ingn, vii());
  rep(i, 0, ingn-1) {
    slurp(packs[i], packsn);
    sort(itall(packs[i]));
  }
  vii its(ingn, 0);
  ii acc = 0;
  while (1) {
    for (auto e : its) {
      if (e >= packsn) {
        goto done;
      }
    }
    rep(i, 0, ingn - 1) {
      ii t = its[i];
      while (min_can_make(packs[i][t], ings[i]) >
             max_can_make(packs[i][t], ings[i])) {
        t++;
        if (t >= packsn) {
          goto done;
        }
      }
      its[i] = t;
    }
    ii max_min = 0;
    ii min_max = inf;
    rep(i, 0, ingn - 1) {
      max_min = max(max_min, min_can_make(packs[i][its[i]], ings[i]));
      min_max = min(min_max, max_can_make(packs[i][its[i]], ings[i]));
    }
    if (min_max >= max_min) {
      acc++;
      rep(i, 0, ingn - 1) {
        its[i]++;
      }
    } else {
      rep(i, 0, ingn - 1) {
        if (max_can_make(packs[i][its[i]], ings[i]) < max_min) {
          its[i]++;
        }
      }
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
