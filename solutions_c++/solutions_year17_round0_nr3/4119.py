#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(){
  int q,cnt=0;
  cin>>q;
  while(q--){
    ll n,K;
    cin>>n>>K;
    
    priority_queue<ll> Q;
    Q.push(n);
    ll L,R;
    while(K--){
      ll len = Q.top();Q.pop();
      L = len/2;
      R = len/2-(len%2==0);
      Q.push(L);
      Q.push(R);
    }
    cout<<"Case #"<<++cnt<<": "<<L<<" "<<R<<endl;
  }
  return 0;
}
