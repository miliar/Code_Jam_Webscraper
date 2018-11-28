/*
 * b.cpp
 *
 *  Created on: Apr 8, 2017
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
    string s;
    cin >> s;
    for (int i = (int)s.size() - 1; i > 0; --i) {
      if (s[i] < s[i - 1]) {
        s[i - 1]--;
        for (int j = i; j < (int)s.size(); ++j) {
          s[j] = '9';
        }
      }
    }
    ll answer = 0;
    for (int i = 0; i < (int)s.size(); ++i) {
      answer = answer * 10LL + (ll)(s[i] - '0');
    }
    cout << "Case #" << it << ": " << answer << endl;
  }
  return 0;
}



