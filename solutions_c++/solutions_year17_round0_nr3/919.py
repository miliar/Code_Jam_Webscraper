#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main(){
  int T; cin >> T;
  for(int ttt=1;ttt<=T;ttt++){
    ll N,K; cin >> N >> K;
    cout << "Case #" << ttt << ": ";

    map<ll,ll> mp;
    mp[N] = 1;
    priority_queue<ll> q; q.push(N);
    ll i = 0;
    while( !q.empty() ) {
      auto it = make_pair( q.top(), mp[q.top()] ); q.pop();
      
      i += it.second;
//      cout << it.first << " "  << "  " << it.second << " " << i << endl;
      if( i >= K ) {
        cout << it.first / 2 << " " << it.first / 2 - ( it.first%2==0 ? 1 : 0 ) <<  endl;
        break;
      }
      if( it.first%2 == 0 ) {
        if(mp.count( it.first / 2LL ) == 0 )
          q.push( it.first / 2LL );
        if( mp.count( it.first / 2LL - 1 ) == 0 )
          q.push( it.first / 2LL - 1 );
        mp[it.first / 2LL] += it.second;
        mp[it.first / 2LL - 1] += it.second;
      }
      else {
        if( mp.count( it.first / 2LL ) == 0 )
          q.push( it.first / 2LL );
        mp[it.first / 2LL]+=it.second*2LL;
      }


    }

  }
}