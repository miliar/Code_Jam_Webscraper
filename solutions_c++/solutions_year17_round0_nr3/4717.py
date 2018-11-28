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
vvll ans;
void output_ans() {
  rep (i, testcase) {
    printf("Case #%d: ", i+1);

    printf("%lld %lld", ans[i][1], ans[i][0]);

    printf("\n");
  }

  exit(0);
}

ll n;
ll k;

void get_input() {
  cin >> n >> k;
}

vll solve() {
  priority_queue<ll> pq;
  pq.push(n);
  rep (i, k-1) {
    ll ma = pq.top() - 1;
    pq.pop();
    ll left = ma / 2;
    ll right = ma - left;
    pq.push(left);
    pq.push(right);
  }
  vll ret(2);
  ll ma = pq.top() - 1;
  ret[0] = ma / 2;
  ret[1] = ma - ret[0];
  return ret;
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
