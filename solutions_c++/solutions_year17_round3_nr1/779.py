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

// cout pair
template<typename T1, typename T2> ostream& operator<<(ostream& s, const pair<T1, T2>& p) {
  s << p.first << " " << p.second << "\n"; return s;
}

// cout vector<pair>
template<typename T1, typename T2> ostream& operator<<(ostream& s, const vector<pair<T1, T2> >& vp) {
  int len = vp.size(); s << "\n";
  for (int i = 0; i < len; ++i) { s << vp[i]; }
    s << "\n"; return s;
}

// cout vector
template<typename T> ostream& operator<<(ostream& s, const vector<T>& v) {
  int len = v.size(); s << "\n";
  for (int i = 0; i < len; ++i) {
    s << v[i]; if (i < len - 1) s << "\t";
  }
  s << "\n"; return s;
}

// cout 2-dimentional vector
template<typename T> ostream& operator<<(ostream& s, const vector< vector<T> >& vv) {
  int len = vv.size();
  for (int i = 0; i < len; ++i) { s << vv[i]; }
  return s;
}

int testcase;
vector<double> ans;
void output_ans() {
  rep (i, testcase) {
    printf("Case #%d: ", i+1);

    // output ans
    // e.g.) printf("%d\n", ans[i]);

    printf("%.9lf", ans[i]);
    printf("\n");
  }
  exit(0);
}

int n, k;
vvll rh;

void get_input() {
  // Do not forget initialization or clear
  
  cin >> n >> k;
  rh.assign(n, vll(3));
  rep (i, n) {
    cin >> rh[i][1] >> rh[i][2];
    rh[i][0] = rh[i][1] * rh[i][2];
  }

}

void solve(int index_testcase) {
  sort(all(rh));
  ll maxr = 0;
  ll minrh = LLONG_MAX;
  ll sum = 0;
  rep (i, k) {
    int ind = n-1 - i;
    sum += rh[ind][0] * 2;
    maxr = max(maxr, rh[ind][1]);
    minrh = min(minrh, rh[ind][0]);

    /*
    if (maxr <= rh[ind][1]) {
      maxr = rh[ind][1];
      thatrh = min(thatrh, rh[ind][0]);
    }
    */
  }

  sum += maxr * maxr;

  ll maxdelta = 0;
  FOR (i, k, n) {
    int ind = n-1 - i;
    maxdelta = max(maxdelta, 2 * rh[ind][0] - 2 * minrh + rh[ind][1] * rh[ind][1] - maxr * maxr);
  }
  ans[index_testcase] = M_PI * (sum + maxdelta);
}

int main() {
  cin >> testcase;
  ans.resize(testcase);

  rep (i, testcase) {
    get_input();
    //ans[i] = solve();
    solve(i);
  }

  output_ans();

  return 0;
}
