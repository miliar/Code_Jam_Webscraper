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
pair<pll, bool> a[200];


void solve() {
  ll n, m;
  cin >> n >> m;
  rep(i, n) {
    cin >> a[i].ft.ft >> a[i].ft.sd;
    a[i].sd = 0;
  }
  FOR(i, n, n + m - 1) {
    cin >> a[i].ft.ft >> a[i].ft.sd;
    a[i].sd = 1;
  }
  n += m;
  sort(a, a + n);
  /*rep(i, n) {
    if (a[i].ft.ft == a[(i + n - 1) % n].ft.sd) a[i].ft.ft++;
  }*/
  bool last = a[n - 1].sd;
  ll last_t = a[n - 1].ft.sd - 1440;
  vector<ll> v1, v2;
  ll ans = 0;
  ll dur = 0;
  ll buf = 0;
  rep(i, n) {
    if (a[i].sd  && last) {
      v1.push_back(a[i].ft.ft - last_t);
      dur += a[i].ft.ft - last_t;
    }
    else if (!a[i].sd && !last) v2.push_back(a[i].ft.ft - last_t);
    else {
      ans++;
      buf += a[i].ft.ft - last_t;
    }

    if (a[i].sd) {
      dur += a[i].ft.sd - a[i].ft.ft;
    }
    last_t = a[i].ft.sd;
    last = a[i].sd;
  }
  sort(v1.rbegin(), v1.rend());
  sort(v2.rbegin(), v2.rend());
  //cout << "dur " << dur << " buf " << buf << endl;
  Min(buf, abs(dur - 720));
  if (dur >= 720) dur -= buf;
  else dur += buf;
  if (dur == 720) {
    cout << ans << endl;
    return;
  }
  if (dur > 720) {
    ll diff = dur - 720;
    for (ll e : v1) {
      //cout << "diff " << diff << " e " << e << endl;
      diff -= e;
      ans += 2;
      if (diff <= 0) {
        break;
      }
    }
  }
  else {
    ll diff = 720 - dur;
    for (ll e : v2) {
      //cout << "diff " << diff << " e " << e << endl;
      diff -= e;
      ans += 2;
      if (diff <= 0) {
        break;
      }
    }
  }
  cout << ans << endl;
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
