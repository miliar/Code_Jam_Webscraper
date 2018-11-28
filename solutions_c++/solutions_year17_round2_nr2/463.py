/*
 * b.cpp
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
    int n, r, o, y, g, b, v;
    cin >> n >> r >> o >> y >> g >> b >> v;
    y -= v;
    b -= o;
    r -= g;
    cout << "Case #" << it << ": ";
    vector<pair<int, char> > a(3);
    a[0] = mpair(y, 'Y');
    a[1] = mpair(b, 'B');
    a[2] = mpair(r, 'R');
    sort(all(a));

    if (y < 0 || b < 0 || r < 0) {
      cout << "IMPOSSIBLE\n";
      continue;
    }


    int total = a[0].first + a[1].first + a[2].first;
    if (a[2].first > total / 2) {
      cout << "IMPOSSIBLE\n";
      continue;
    }
    string res(total, ' ');
    for (int i = 0; i < a[2].first; ++i) {
      res[i * 2] = a[2].second;
    }
    int rem = (total - a[2].first * 2) + 1;
    if (a[0].first < rem / 2) {
      cout << "IMPOSSIBLE\n";
      continue;
    }
    for (int j = a[2].first * 2 - 1; j < total; ++j) {
      if ((j - (a[2].first * 2 - 1)) % 2 == 0) {
        res[j] = a[1].second;
        a[1].first--;
      } else {
        res[j] = a[0].second;
        a[0].first--;
      }
    }
    for (int i = 1; res[i] == ' '; i += 2) {
      if (a[0].first > 0) {
        res[i] = a[0].second;
        a[0].first --;
      } else {
        res[i] = a[1].second;
        a[1].first --;
      }
    }

    string real_res;
    for (int i = 0; i < (int)res.size(); ++i) {
      if (res[i] == 'Y') {
        if (v > 0) {
          real_res.push_back('Y');
          real_res.push_back('V');
          v--;
        }
        real_res.push_back('Y');
      } else if (res[i] == 'B') {
        if (o > 0) {
          real_res.push_back('B');
          real_res.push_back('O');
          o--;
        }
        real_res.push_back('B');
      } else if (res[i] == 'R') {
        if (g > 0) {
          real_res.push_back('R');
          real_res.push_back('G');
          g--;
        }
        real_res.push_back('R');
      }
    }
    cout << real_res << endl;
  }
  return 0;
}


