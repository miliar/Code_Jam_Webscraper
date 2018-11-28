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

const int D = 19;

long long dp[D][10][2];
int num[D];

void process(long long n) {
  for (int i = 0; i < D; ++i) {
    num[D-i-1] = n%10;
    n /= 10;
  }
}

long long f(int at, int last, int diverged) {
  if (at == D) return 1;
  long long &ret = dp[at][last][diverged];
  if (ret != -1) return ret;
  ret = 0;
  for (int d = last; d <= 9; ++d) {
    if (!diverged && (d > num[at])) break;
    ret += f(at+1, d, diverged || (d<num[at]));
  }
  return ret;
}

int main(int argc, char* argv[]) {
  int nocases;
  cin >> nocases;
  //  getchar();
  for (int rr = 1; rr <= nocases; ++rr) {
    long long n;
    cin >> n;
    process(n);
    memset(dp, -1, sizeof(dp));
    long long cnt = f(0, 0, 0);
    long long lo = 1, hi = n;
    while (lo < hi) {
      long long mid = (lo+hi)/2;
      process(mid);
      memset(dp, -1, sizeof(dp));
      if (f(0,0, 0) < cnt)
	lo = mid+1;
      else
	hi = mid;
    }
    printf("Case #%d: %lld\n", rr, lo);
  }
  return 0;
}
