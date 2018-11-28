#include <bits/stdc++.h>
using namespace std;
#define F first
#define S second
typedef long long ll;
typedef pair<int, int> ii;
long double d;
int n;
pair<long double, long double> a[1005];
bool chk(long double speed){
  long double tim = 1.0 * d/speed;
  for(int i = 0; i < n; i++){
    if(a[i].F + (a[i].S * tim) < d)
      return 0;
  }
  return 1;
}
int main(){
  freopen("A-large.in", "r", stdin);;
  freopen("out.out","w",stdout);
  ll t;
  cin >> t;
  int cas = 0;
  while(t--){
      cin >> d >> n;
      for(int i = 0; i < n; i++)
        cin >> a[i].F >> a[i].S;
      sort(a, a + n);
      long double lo = 0.0, hi = 1e18;
      for(int i = 0; i < 100; i++){
        long double md = (lo + hi)/2;
        if(chk(md))
          lo = md;
        else
          hi = md;
      }
      cout << fixed << setprecision(6) << "Case #" << ++cas << ": " << lo << '\n';
  }
}
