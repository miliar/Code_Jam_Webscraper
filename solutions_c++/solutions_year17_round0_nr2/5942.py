#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main (){
  ll t,n;
  cin >> t;
  for (int i = 0 ; i < t ; ++i){
    cout << "Case #" << i+1 << ": ";
    cin >> n;
    ll ans = n;
    ll aux = n;
    ll base = 1;
    while (aux >= 10){
      ll r1 = aux%10;
      ll r2 = (aux%100)/10;
      if (r2 > r1) ans-=(ans%(base*10)+1);
      aux = ans/(10*base);
      base*=10;
    }
    cout << ans << endl;
  }
  return 0;
}
