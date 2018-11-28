#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> pii;

void solve(){
  priority_queue<pii> Q;
  ll numserved = 0;
  ll n, k; cin >> n >> k;
  Q.push(pii(n,1));
  while(true){
    pii x = Q.top(); Q.pop();
    numserved += x.second;
    if(numserved >= k){
      cout << x.first/2 << " " << (x.first - 1) / 2 << "\n";
      return;
    }
    if(x.first % 2 == 1){
      Q.push(pii(x.first/2, 2 * x.second));
    }
    else{
      Q.push(pii(x.first/2, x.second));
      Q.push(pii((x.first-1)/2, x.second));
    }
  }
  assert(false);
}


int main(){
  int T; cin >> T;
  for(int i=0;i<T;i++){
    cout << "Case #" << i+1 <<": ";
    solve();
  }
}


