#include <iostream>
#include <string>
#include <cstdio>
#include <vector>

using namespace std;

int main() {
  long long T;

  cin >> T;

  for (int t=1;t<=T;t++) {
    long long n, k;
    cin >> n >> k;

    k--;
    long long x = n; // size of large range
    long long v0 = 1; // number of empty ranges size x
    long long v1 = 0; // # ranges size x+1

    long long y = (n-1)/2; // size of small
    long long w0 = 0, w1 = 0; // # ranges size y, y+1

    long long i = 0;

    while (i < k) {
      long long t;
      long long a, b;
      if (v1 != 0) {
        t = min(v1, k - i);
        v1 -= t;

        a = x/2;
        b = x-a;
      }
      else if (v0 != 0) {
        t = min(v0, k - i);
        v0 -= t;
        a = (x-1)/2;
        b = (x-1)-a;
      }
      if (a == y) w0 += t;
      else w1 += t;
      if (b == y) w0 += t;
      else w1 += t;
      i += t;

      if (v0 == 0 && v1 == 0) {
        x = y;
        v0 = w0;
        v1 = w1;
        y = (x-1)/2;
        w0 = w1 = 0;
      }
    }

    long long size = x;
    if (v1 > 0) size++;

    long long ansz = (size-1)/2;
    long long ansy = (size-1) - ansz;

    printf("Case #%d: %lld %lld\n", t, ansy, ansz);
  }

}
