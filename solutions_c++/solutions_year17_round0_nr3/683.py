#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <string>
#include <string.h>
#include <set>
#include <stdio.h>
#include <assert.h>
#include <sstream>
using namespace std;

int main(int argc, char* argv[]) {
  int nocases;
  cin >> nocases;
  for (int rr = 1; rr <= nocases; ++rr) {
    long long n, k;
    cin >> n >> k;
    long long m, M;
    long long tp = 1;
    while (tp <= k)
      tp *= 2;
    tp >>= 1;
    long long diff = n - k;
    if (diff < tp)
      M = 0;
    else
      M = (diff-tp)/(2*tp) + 1;
    m = diff/(2*tp);
    printf("Case #%d: %lld %lld\n", rr, M, m);
    
  }
  return 0;
}
