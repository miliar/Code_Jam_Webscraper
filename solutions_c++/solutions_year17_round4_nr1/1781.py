#include <iostream>
#include <iomanip>
#include <vector>
#include <queue>
#include <algorithm> // sort
#include <utility>
#include <cmath>

typedef long long ll;
using namespace std;


int main(){
  ll T;
  cin >> T;

  for(int t=0; t<T; t++){
    ll N, P;
    cin >> N >> P;

    vector<ll> Gs(N);
    for(int i=0; i<N; i++){
      cin >> Gs[i];
    }

    //
    ll ans = 0;
    vector<int> cnt(P);
    for(int i=0; i<N; i++){
      cnt[Gs[i]%P]++;
    }

    ans += cnt[0];
    if(P==2){
      ans += cnt[1]/2 + cnt[1]%2;
    } else if(P==3){
      int mm = min(cnt[1], cnt[2]);
      ans += mm; // 3n+1 + 3m+2
      int rest = cnt[1] + cnt[2] - 2*mm;
      ans += rest/3;
      ans += rest%3==0 ? 0 : 1;
    } else if(P==4){
      ans += cnt[2]/2; // 4n+2
      int mm = min(cnt[1], cnt[3]);
      ans += mm; // 4n+1 + 4m+3
      int rest = cnt[1] + cnt[3] - 2*mm;
      if(cnt[2]%2 == 1 && rest >= 2){
        ans++;
        rest -=2;
      }
      ans += rest/4;
      ans += rest%4==0 ? 0 : 1;
    }

    cout << "Case #" << t+1 << ": " << setprecision(8) << ans << endl;
  }

  return 0;
}
