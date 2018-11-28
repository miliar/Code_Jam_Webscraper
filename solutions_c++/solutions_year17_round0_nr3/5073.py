/** \file

    inputs:
     N K
    (N = len of empty-stall run at start, filled by K<=N people)

    output last person's
    Case #x: y z
    y is max(LS, RS), and z is min(LS, RS)
    (z=floor(r/2) for largest remaining empty run r+1; y=z if r even else y=z+1
*/

#define MAXCASES 100
#include "codejam.hh"

struct Case : CaseBase {
  typedef map<u64, U> Runs;
  Runs runs;
  u64 N, K;
  u64 floorhalf;
  u64 ceilhalf;
  void read() {
    N = GETu64;
    K = GETu64;
    assert(N);
    assert(K);
    assert(K <= N);
    runs.clear();
    runs[N] = 1;
  }
  u64 take() {
    assert(!runs.empty());
    auto i = runs.end();
    --i;
    u64 k = i->first;
    U& n = i->second;
    if (!--n) runs.erase(i);
    return k;
  }
  void enter() {
    u64 last = take();
    assert(last);
    --last;
    floorhalf = last / 2;
    ceilhalf = last - floorhalf;
    add(floorhalf);
    add(ceilhalf);
  }
  void add(u64 x) {
    if (x) ++runs[x];
  }
  void print() {
    putU(ceilhalf);
    putsp();
    putU(floorhalf);
  }
  void show1() {
  }
  void solve() {
    for (u64 i = 0; i < K; ++i) enter();
  }
};

CASES_MAIN(Case)
