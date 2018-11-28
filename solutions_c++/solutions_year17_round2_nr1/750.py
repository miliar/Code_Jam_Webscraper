#include <algorithm>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
#include <cstring>

#define SIZE(s) ((int)((s).size()))
#define FOREACH(it,vec) for(typeof((vec).begin())it=(vec).begin();it!=(vec).end();++it)
#define REP(i,n) for(int i=0;i<(int)(n);++i)

using namespace std;

long long D, N, T;

int main(void) {
  cin >> T;
  REP(t, T) {
    cin >> D >> N;
    vector<long long> K(N);
    vector<long long> S(N);
    long double h = 0;
    REP(n, N) {
      cin >> K[n] >> S[n];
      h = max(h, (long double)(D - K[n]) / (long double) S[n]);
    }
    printf("Case #%d: %.10Lf\n", t+1, (long double) D / h);
  }
  return 0;
}
