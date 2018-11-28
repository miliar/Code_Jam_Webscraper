#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <iostream>
#include <limits>
#include <numeric>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define MP make_pair
#define all(v) (v).begin(), (v).end()
#define PROBLEM_ID "tidy_numbers"

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<vvb> vvvb;
typedef long double ld;
typedef pair<int, int> pii;
typedef long long ll;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<vvl> vvvl;
typedef pair<ll, ll> pll;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<vvd> vvvd;

ll FromString(const string& num) {
  ll res = 0;
  for (int i = 0; i < num.length(); ++i) {
    res = res * 10 + num[i] - '0';
  }
  return res;
}

string ToString(ll n) {
  string res;
  while (n > 0) {
    res += ('0' + n % 10);
    n /= 10;
  }
  reverse(res.begin(), res.end());
  return res;
}

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int tests;
  cin >> tests;
  for (int test_index = 0; test_index < tests; ++test_index) {
    ll n;
    cin >> n;
    string n_str = ToString(n);
    ll res;
    if (n < FromString(string(n_str.length(), '1'))) {
      res = FromString(string(n_str.length() - 1, '9'));
    }
    else {
      string res_str = "";
      int min_digit = 1;
      for (int pos = 0; pos < n_str.length(); ++pos) {
        for (int digit = 9; digit >= min_digit; --digit) {
          string min_complete = res_str + string(n_str.length() - pos, '0' + digit);
          if (n >= FromString(min_complete)) {
            res_str += ('0' + digit);
            min_digit = digit;
            continue;
          }
        }
      }
      res = FromString(res_str);
    }
    cout << "Case #" << (test_index + 1) << ": " << res << endl;
    cerr << "Case #" << (test_index + 1) << ": " << res << endl;
    
  }
  return 0;
}
