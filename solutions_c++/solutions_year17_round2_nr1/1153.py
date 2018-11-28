#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <vector>
#include <map>
#include <set>
#include <stdlib.h>
#include <string>
#include <queue>
#include <iomanip>
#include <unordered_map>
using namespace std;

int main() {

  freopen("in", "r", stdin);
  freopen("out", "w", stdout);

  int testN; cin >> testN;

  for (int i = 1; i <= testN; i++) {
    cout << "Case #" << i << ": ";
    int d, n; cin >> d >> n;
    long double result = -1;
    for (int i = 0; i < n; i++) {
      int k, s; cin >> k >> s;
      long double currentTime = (d - k) / (double) s;
      if (result == -1) result = d / currentTime;
      else
      result = min(result, d / currentTime);
    }
    cout << fixed << setprecision(6) << result << "\n";
  }

  return 0;
}
