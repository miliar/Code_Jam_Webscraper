/*
 * a.cpp
 *
 *  Created on: Apr 22, 2017
 *      Author: istrandjev
 */

#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <queue>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <math.h>
#include <stack>
#include <deque>
#include <numeric>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <bitset>
#include <functional>
#define all(x) x.begin(),x.end()
#define mpair make_pair
using namespace std;
typedef long long ll;
typedef long double ld;
const ld epsylon = 1e-9;

const string PROGRAM_NAME = "google";

int main() {
  freopen((PROGRAM_NAME + ".in").c_str(), "r", stdin);
  freopen((PROGRAM_NAME + ".out").c_str(), "w", stdout);
  int nt;
  cin >> nt;
  for (int it = 1; it <= nt; it++) {
    int d, n;
    cin >> d >> n;
    double maxs = -1.0;
    for (int i = 0; i < n; ++i) {
      int k, s;
      scanf("%d %d", &k, &s);
      double t = double(d - k) / double(s);
      if (maxs < -0.5 || maxs > (d / t)) {
        maxs = d /t;
      }
    }
    cout << "Case #" << it << ": ";
    printf("%.9lf\n", maxs);
  }
  return 0;
}


