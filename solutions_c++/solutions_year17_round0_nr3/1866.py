#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

struct Result {
  long long fstCount;
  long long fstLength;
  long long scdCount;
  long long scdLength;

  Result(long long a, long long b, long long c, long long d) {
    fstCount = a;
    fstLength = b;
    scdCount = c;
    scdLength = d;
  }
};

int main() {
  int T;
  cin >> T;
  for(int t = 1; t <= T; ++t) {
    long long n, k;
    cin >> n >> k;
    Result res = Result( 1, n, 0, 0 );
    // printf("%lld %lld %lld %lld\n", res.fstCount, res.fstLength, res.scdCount, res.scdLength );
    long long i = 1;
    for(; i < k; i <<= 1) {
      if( res.fstLength & 1 ) {
        res = Result( 2*res.fstCount+res.scdCount, res.fstLength/2, res.scdCount, res.fstLength/2 - 1 );
      } else {
        res = Result( res.fstCount, res.fstLength/2, res.fstCount + 2*res.scdCount, res.fstLength/2 - 1 );
      }
      k -= i;
      // printf("%lld %lld %lld %lld\n", res.fstCount, res.fstLength, res.scdCount, res.scdLength );
    }
    if( k <= res.fstCount ) {
      printf("Case #%d: %lld %lld\n", t, res.fstLength/2, (res.fstLength - 1)/2);
    } else {
      printf("Case #%d: %lld %lld\n", t, res.scdLength/2, (res.scdLength - 1)/2);
    }
  }
  return 0;
}