#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;
typedef long long ll;

priority_queue<ll> que[110];

void print_case(int ii, int mx, int mn){
  cout << "Case #" << ii << ": " << mx << " " << mn << endl;
}

void choose(int ii, ll N, ll K){
  que[ii].push(N);
  for(int i = 0; i < K-1; i++){
    ll n = que[ii].top(); que[ii].pop();
    ll l = (n-1)/2;
    ll r = n-1-l;
    que[ii].push(r);  que[ii].push(l);
  }
  ll n = que[ii].top();
  print_case(ii, n-1-(n-1)/2, (n-1)/2);
}

int main(){
  int T;  cin >> T;
  for(int ii = 1; ii <= T; ii++){
    ll N, K;  cin >> N >> K;
    choose(ii, N, K);
  }

  return 0;
}
