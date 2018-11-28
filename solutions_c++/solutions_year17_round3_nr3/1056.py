#include <algorithm>
#include <assert.h>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <iterator>
#include <map>
#include <math.h>
#include <queue>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)
#define TR(x) cout << #x << " = " << x << endl
#define _ << " _ " <<

typedef long long ll;

int N, K;
double U;
double P[55];




double minA(int &k) {
  double min = 2;
  F0(i, N) {
    if (min > P[i]) {
      min = P[i];
      k = i;
    }
  }
  return min;
}


// double minAndNb(int &mNb) {
//   double min = 2;
//   F0(i, N) {
//     if (min > P[i]) {
//       min = P[i];
//     }
//   }
//   double secondMin = 2;
//   mNb = 0;
//   F0(i, N) {
//     if (min == P[i]) {
//       mNb++;
//       continue;
//     }
//     if (secondMin > P[i]) {
//       secondMin = P[i];
//     }
//   }
//   return min;
// }


int main(int argc, const char **argv) {
  int cases;
  cin >> cases;
  int minNb;
  double min;
  int k;
  F1(caseI, cases) {
    cin >> N >> K;
    cin >> U;
    minNb = 0;
    F0(i, N) {
      cin >> P[i];
    }

    min = minA(k);
    while (min != 1 && U >= 0.00000001) {
      // std::cout << "U:" << U << std::endl;
      // cout << (U!=0) << endl;
      P[k] += 0.0001;
      U -= 0.0001;
      min = minA(k);
    }

    double r = 1;
    F0(i, N) {
      r *= P[i];
    }

    cout << "Case #" << caseI << ": ";
    printf("%.9f\n", r);
  }

  return 0;
}
