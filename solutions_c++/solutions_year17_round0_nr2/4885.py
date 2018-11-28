/** \file


*/

#define MAXCASES 100
constexpr int DIGITS = 20;
#include "codejam.hh"
struct Case : CaseBase {
  i8 s[DIGITS];
  I ns;
  u64 N;
  void read() {
    N = GETu64;
    ns = 0;
    while (N) {
      s[ns++] = N % 10;
      N /= 10;
    }
    assert(ns);
  }
  void print() {
    I i = ns;
    assert(ns);
    if (s[i - 1] == 0) --i;
    while (i) put0(s[--i]);
  }
  void show1() {
    cerr << ' ';
    for (I i = ns; i;) cerr << digit0(s[--i]);
    cerr << ' ';
  }
    bool tidy() {
    return true;
  }
  void dec(I i) {
    for (; i < ns; ++i) {
      i8& d = s[i];
      if (d == 0) {
        d = 9;
      } else {
        --d;
        break;
      }
    }
  }
  void solve() {
    i8 prev = 10;
    I i = 0;
    for (; i < ns; ++i) {
      if (s[i] > prev) {
        for (I j = i; j ; )
          s[--j] = 9;
        dec(i);
      }
      prev = s[i];
    }
  }
};

CASES_MAIN(Case)
