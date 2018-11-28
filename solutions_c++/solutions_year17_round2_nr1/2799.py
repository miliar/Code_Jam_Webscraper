#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <limits>
using namespace std;

int main() {
  int n;
  cin >> n;
  double maxhour;
  for (int i = 0; i < n; i++) {
    int d, ni;
    cin >> d >> ni;
    maxhour = 0;
    for (int j = 0; j < ni; j++) {
      int pos, speed;
      cin >> pos >> speed;
      double hour = 1.0 * (d - pos) / speed;
      maxhour = max(hour, maxhour);
    }
    printf("Case #%d: %f\n", i+1, d/maxhour);
  }

}

