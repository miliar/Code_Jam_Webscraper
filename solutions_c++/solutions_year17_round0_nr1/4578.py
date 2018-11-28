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
vi ans;
void output_ans() {
  rep (i, testcase) {
    printf("Case #%d: ", i+1);
    if (ans[i] < 0) {
      printf("IMPOSSIBLE\n");
    } else {
      printf("%d\n", ans[i]);
    }
  }
  exit(0);
}

vi pancakes;
int k;

int n;

void get_input() {
  pancakes.clear();
  string s;
  cin >> s;
  n = s.length();
  rep (i, n) {
    if (s[i] == '+') {
      pancakes.push_back(0);
    } else if (s[i] == '-') {
      pancakes.push_back(1);
    } else {
      break;
    }
  }
  cin >> k;
}

void flip(int start) {
  FOR (i, start, start + k) {
    pancakes[i] = 1 - pancakes[i];
  }
}

void solve(int testcase_index) {
  rep (i, n) {
    if (pancakes[i] == 0) continue;
    if (i + k > n) {
      ans[testcase_index] = -1;
      return;
    }
    flip(i);
    ans[testcase_index] += 1;
  }
}

int main() {
  cin >> testcase;
  ans.assign(testcase, 0);

  rep (i, testcase) {
    get_input();
    solve(i);
  }

  output_ans();

  return 0;
}
