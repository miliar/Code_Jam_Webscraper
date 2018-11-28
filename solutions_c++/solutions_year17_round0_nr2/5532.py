#include <sstream>
#include <cassert>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <queue>
#include <list>
#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

typedef long long tint;
typedef unsigned int uint;
const int MAXN = 1073741824;
const int MAX_INT = 2147483647;

int num_dig(tint n)
{
  int d = 0;
  while (n > 0) {
    n /= 10;
    d++;
  }
  return d;
}

void num2v(tint n, int d, vector<int> &v)
{
  while (n > 0) {
    v[--d] = n % 10;
    n /= 10;
  }
}

int main() {
  int T;
  cin >> T;
  for (int tt = 1; tt <= T; tt++) {
    tint n;
    cin >> n;
    int d = num_dig(n);
    vector<int> v(d);
    num2v(n, d, v);

    int mind = 10;
    vector<int> num(d, 0);
    for (int i = d - 1; i >= 0; i--) {
      if (v[i] <= mind) {
        num[i] = v[i];
        mind = v[i];
      } else {
        num[i] = v[i] - 1;
        for (int j = i + 1; j < d; j++) {
          num[j] = 9;
        }
        mind = num[i];
      }
    }

    tint last = 0;
    for (int i = 0; i < d; i++) {
        last = last*10 + num[i];
    }

    cout << "Case #" << tt << ": ";
    cout << last << endl;

  }

  return 0;
}
