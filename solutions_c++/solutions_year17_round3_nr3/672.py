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



const int N = 51;
ll a[N];

ll getn() {
  ll a, b;
  char ch;
  cin >> a >> ch >> b;
  return a * 10000 + b;
}


void solve() {
  ll n, k;
  cin >> n >> k;
  ll u = getn();
  rep(i, n) a[i] = getn();
  sort(a, a + n);
  a[n] = 10000;
  rep(i, n) {
    if (a[i + 1] > a[i]) {
      ll diff = a[i + 1] - a[i];
      if (u >= diff * (i + 1)) {
        rep(j, i + 1) a[j] = a[i + 1];
        u -= diff *(i + 1);
      }
      else {
        ll diff2 = u / (i + 1);
        ll rem = u % (i + 1);
        rep(j, i+1-rem) {
          a[j] += diff2;
        }
        FOR(j, i+1-rem, i) a[j] += diff2 + 1;
        break;
      }
    }
  }
  double ans = 1;
  rep(i, n) {
    ans *= (double)a[i] / 10000.0;
  }
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
