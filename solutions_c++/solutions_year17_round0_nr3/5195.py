#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
ll t,n,k;
int main() {
  ios::sync_with_stdio(false);
  cin>>t;
  for(int cislo=1;cislo<=t;cislo++){
    cin>>n>>k;
    priority_queue<pair<pair<ll,ll>,ll> > Q;
    Q.push({{n,n%2LL}, -1LL});
    for(int i=1;i<k;i++){
      pair<pair<ll,ll>,ll> teraz=Q.top();Q.pop();
      //cout <<i<<" "<<teraz.first.first<<" "<<teraz.first.second<<" "<<teraz.second<<endl;
      ll stred=-teraz.second+(teraz.first.first-1LL)/2LL;
      pair<pair<ll,ll>,ll> dalsi1={{(teraz.first.first-1LL)/2LL,0LL},teraz.second},dalsi2={{teraz.first.first/2LL,0LL},-stred-1LL};
      dalsi1.first.second=dalsi1.first.first%2LL;
      dalsi2.first.second=dalsi2.first.first%2LL;
      //cout <<dalsi2.first.first<<" "<<dalsi2.first.second<<" "<<dalsi2.second<<endl;
      Q.push(dalsi1);Q.push(dalsi2);
    }
    pair<pair<ll,ll>,ll> teraz=Q.top();
    ll stred=-teraz.second+(teraz.first.first-1LL)/2LL,zac=-teraz.second,kon=-teraz.second+teraz.first.first-1LL;
    //cout <<stred<<"df"<<endl;
    cout <<"Case #"<<cislo<<": "<<max(stred-zac, kon-stred)<<" "<<min(stred-zac, kon-stred)<<endl;
  }
  return 0;
}