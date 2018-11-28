#include <string>
#include <vector>
#include <cstring>
#include <cmath>
#include <utility>
#include <algorithm>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <list>
#include <iomanip>
#include <ctime>
#include <cassert>
#include <stack>
#include <unordered_map>
#include <unordered_set>

#define what_is(x) cout << #x << " is " << x << endl;

using namespace std;

typedef long long ll;

int main () {
  cout << fixed;
  cout << setprecision(9);
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    double d, maxTime = 0;
    int n;
    cin >> d >> n;
    for (int i = 0; i < n; i++) {
      double k, s;
      cin >> k >> s;
      if (maxTime < (d - k) / s) {
	maxTime = (d - k) / s;
      }
    }
    cout << "Case #" << (i + 1) << ": " << d / maxTime << endl;
  }
  return 0;
}
