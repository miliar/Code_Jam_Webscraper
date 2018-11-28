#include<iostream>
#include<string>
#include<queue>

using namespace std;
using ll = long long;

void solve(const int t, ll N, ll K);

int main() {
  int T; cin>>T; cerr<<"Total case: "<<T<<endl;
  for(int i=0;i<T;++i) {
    ll N,K; cin>>N>>K;
    cerr << "Case #" << i+1 << ": N:"<< N << " K:" << K << endl;
    solve(i+1,N,K);
  }
  return 0;
}

void solve(const int t, ll N, ll K) {
  ll mini=N,maxi=0;

  priority_queue<ll> q;
  q.push(N);
  
  for(ll i=0;i<K;++i) {
    ll a = q.top(); q.pop();
    maxi = a/2;
    mini = (a-1)/2;
    q.push(maxi);
    q.push(mini);
    //cerr << "maxi:"<<maxi<<" mini:"<<mini<<endl;
  }

  cout << "Case #" << t << ": " << maxi << " " << mini << endl;
  cerr << " -> " << maxi <<" "<<mini << endl;
}

