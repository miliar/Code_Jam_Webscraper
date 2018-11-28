#include <map>
#include <set>
#include <list>
#include <cmath>
#include <stack>
#include <queue>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <cstdlib>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <string>
#include <cstring>
#include <algorithm>
#include <assert.h>
#include <functional>
#define _USE_MATH_DEFINES
#include <math.h>
using namespace std;
#define ll long long
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pb push_back
#define ft first
#define sd second
#define rep(i,n) for(ll i=0;i<(n);++i)
#define FOR(i,b,e) for(ll i=b;i<=(e);++i)
#define FORR(i,b,e) for(ll i=b;i>=(e);--i)
#define Fill(a,b) memset(a,b,sizeof(a))
#define all(a) a.begin(),a.end()
template<typename T1, typename T2> void Max(T1& a, T2 b) { a = max(a, (T1)b); }
template<typename T1, typename T2> void Min(T1& a, T2 b) { a = min(a, (T1)b); }



const int N = 100000;
pair<double, pair<double,double>> a[1000];


void solve() {
  ll n, k;
  cin >> n >> k;
  rep(i, n) {
    cin >> a[i].sd.ft >> a[i].sd.sd;
    a[i].ft = a[i].sd.ft*a[i].sd.sd;
  }
  sort(a, a + n);
  reverse(a, a + n);
  double t = 0, r = 0;
  rep(i, k - 1) {
    t += a[i].ft;
    Max(r, a[i].sd.ft);
  }
  double ans = 0;
  FOR(i, k - 1, n - 1) {
    double cur = t + a[i].ft;
    double rr = max(r, a[i].sd.ft);
    cur *= 2;
    cur += rr*rr;
    Max(ans, cur);
  }
  ans *= M_PI;
  cout << setprecision(8) << ans << endl;
}

void init() {
 
}

int main(void) {
  ios::sync_with_stdio(false); cin.tie(0);
  //freopen("C:\\Users\\LENOVO\\Documents\\Visual Studio 2015\\Projects\\Test\\Input\\in.in", "r", stdin);

  init();
  int T; cin >> T;
  FOR(TI, 1, T) {
    cout << "Case #" << TI << ": ";
    //cout << "Case " << TI << ": ";
    solve();
  }
  

  return 0;
}
