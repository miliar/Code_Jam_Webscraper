#include <algorithm>
#include <cassert>
#include <cfloat>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <deque>
#include <iostream>
#include <limits>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <vector>
 
#define FOR(i,k,n) for (int (i)=(k); (i)<(n); ++(i))
#define rep(i,n) FOR(i,0,n)
#define all(v) begin(v), end(v)
#define debug(x) cerr<< #x <<": "<<x<<endl
#define debug2(x,y) cerr<< #x <<": "<< x <<", "<< #y <<": "<< y <<endl
 
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<ll> vll;
typedef vector<vector<ll> > vvll;
typedef deque<bool> db;
template<class T> using vv=vector<vector< T > >;

int testcase;
vll ans;
void output_ans() {
  rep (i, testcase) {
    printf("Case #%d: ", i+1);

    // output ans
    // e.g.) printf("%d\n", ans[i]);

    printf("%lld", ans[i]);
    printf("\n");
  }
  exit(0);
}

vi digits;

int n;

void get_input() {
  string s;
  cin >> s;
  n = s.length();
  digits.resize(n);

  rep (i, n) {
    digits[i] = s[i] - '0';
  }
}

ll pow10(int x) {
  ll ret = 1;
  rep (i, x) {
    ret *= 10;
  }
  return ret;
}

ll vi_to_ll(vi &d) {
  ll ret = 0;
  int n_ = d.size();
  rep (i, n_) {
    ret += d[i] * pow10(n_-1 - i);
  }
  return ret;
}

ll solve() {
  for (int j = n-1; j >= 0; --j) {
    FOR (i, j+1, n) {
      if (digits[j] > digits[i]) {
        digits[j] = digits[j] - 1;
        FOR (k, j+1, n) {
          digits[k] = 9;
        }
      }
    }
  }

  return vi_to_ll(digits);
}

int main() {
  cin >> testcase;
  ans.resize(testcase);

  rep (i, testcase) {
    get_input();
    ans[i] = solve();
  }

  output_ans();

  return 0;
}
