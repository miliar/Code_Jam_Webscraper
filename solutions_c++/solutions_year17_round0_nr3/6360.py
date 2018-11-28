#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <climits>
#include <map>
#include <sstream>
#include <string>
// www.boost.org
#include <boost/multiprecision/cpp_int.hpp>
#include <boost/utility/binary.hpp>
#include <queue>

using namespace std;
using namespace boost::multiprecision;

unsigned long long ullpow(unsigned long long base, unsigned long long exp)
{
    unsigned long long result = 1;
    while (exp)
    {
        if (exp & 1)
            result *= base;
        exp >>= 1;
        base *= base;
    }

    return result;
}

void stalls(unsigned long long n, unsigned long long k) {
  priority_queue<unsigned long long> pq;
  pq.push(n);

  unsigned long long l, r;
  unsigned long long ki = 1;
  while (ki <= k && !pq.empty()) {
    unsigned long long gapSize = pq.top();
    pq.pop();

    unsigned long long leftEmpty = gapSize - 1;
    l = leftEmpty / 2;
    unsigned long long remainder = leftEmpty % 2;
    r = l + remainder;

    pq.push(l);
    pq.push(r);
    ki++;
  }

  cout << r << ' ' << l;
  
  

  // unsigned long long flooredLog2K = 0;
  // unsigned long long powerValue = 1;
  // unsigned long long remainderLog2K = k - 1;

  // unsigned long long nextPowerValue;
  // unsigned long long nextRemainder;
  // unsigned long long nextFlooredLog2K = 1;
  // while (true) {
  //   nextPowerValue = ullpow(2, nextFlooredLog2K);
  //   nextRemainder = k - nextPowerValue;

  //   if (nextPowerValue > k) {
  //     break;
  //   } else {
  //     flooredLog2K = nextFlooredLog2K;
  //     powerValue = nextPowerValue;
  //     remainderLog2K = nextRemainder;
  //   }

  //   nextFlooredLog2K++;
  // }
  // //  cout << flooredLog2K << ' ' << remainder;

  // unsigned long long nHalvingFactor = powerValue * 2;
  // unsigned long long mx = n / nHalvingFactor;
  // unsigned long long remainderAfterHalfingN = n % nHalvingFactor;
  // unsigned long long mn;
  // cout << "remainderAfterHalfingN " << remainderAfterHalfingN << endl;
  // cout << "remainderLog2K " << remainderLog2K << endl;
  // if (remainderAfterHalfingN > 0) {
  //   if (mx > 0) {
  //     mn = (remainderLog2K == 0) ? mx : mx - 1;
  //   } else {
  //     mn = 0;
  //   }
  // } else {
  //   if (mx > 0) {
  //     mn = (remainderLog2K == 0) ? mx - 1: mx;
  //   } else {
  //     mn = 0;
  //   }
  // }

  // cout << mx << ' ' << mn;
}

int main() {
  int t;
  scanf("%d\n", &t);

  for (int i = 1; i <= t; i++) {
    unsigned long long n, k;
    cin >> n >> k;

    cout << "Case #" << i << ": ";

    stalls(n, k);
    cout << endl;
  }
}
