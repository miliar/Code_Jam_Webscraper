/**

 */

#define MAXCASES 100
#include "codejam.hh"

typedef double R;
struct Case : CaseBase {
  I N;
  R D;
  R y;
  struct H {
    R k;
    R s;
    friend inline std::ostream& operator<<(std::ostream &out, H const& self) {
      self.print(out);
      return out;
    }
    void print(std::ostream &out) const {
      out << k << ',' << s;
    }
  };
  H hs[1000];
  void read() {
    D = GETU;
    N = GETU;
    REP(i,N) {
      hs[i].k = GETU;
      hs[i].s = GETU;
    }
    R t = 0;
    REP(i,N) {
      R d2 = D - hs[i].k;
      CO(d2);
      R t2 = d2 / hs[i].s;
      CO(t2);
      amax(t, t2);
      CO(t);
    }
    CO(D);
    y = D / t;
    CO(y);
  }
  void print() {
    printf("%.6f", y);
  }
  void show1() {
    CO(D);
    CO(y);
    REP(i,N) {
      cerr << ' ' << hs[i];
    }

    cerr << " => " << y; }
  void solve() {}
};

CASES_MAIN(Case)
