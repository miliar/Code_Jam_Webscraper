#include<bits/stdc++.h>
#define pb   push_back
using namespace std;
typedef long long ll;
typedef long double ld;

int val[30];

int main(){
  ios_base::sync_with_stdio(false);cin.tie(0);
  int T, n, p;
  cin >> T;
  for(int it=0;it<T;it++){
    ll ans = 0;
    cin >> n >> p;
    int a;
    memset(val,0,sizeof val);
    for(int i=0;i<n;i++){
      cin >> a;
      val[a%p]++;
    }
    ans+=val[0];
    if (p==3){
      ans+=min(val[1],val[2]);
      int m = min(val[1],val[2]);
      val[1]-=m;
      val[2]-=m;
      //cout << val[1] <<" " << val[2];
      for(int i=1;i<3;i++){
        ans+=val[i]/3;
      }
      for(int i=1;i<3;i++){
        if (val[i]%3) {
          ans++;
          break;
        }
      }
    }
    if (p==2){
      ans+=val[1]/2;
      if (val[1]%2) ans++;
    }
    cout <<"Case #" <<it+1 <<": " << ans <<endl;
  }
}
