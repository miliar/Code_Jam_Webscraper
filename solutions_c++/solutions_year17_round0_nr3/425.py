#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const int MAX_N = 300030;
const ll  MODD = 1000000007;

int A[MAX_N];

void do_case(){
  ll n,k; cin >> n >> k;
  priority_queue<pair<ll,ll> > pq;
  pq.emplace(n,1);

  ll x;
  while(k > 0){
    ll m=0;
    x = pq.top().first;
    while(!pq.empty() && pq.top().first == x){
      m += pq.top().second;
      pq.pop();
    }
    k -= m;
    pq.emplace((x-1)/2,m);
    pq.emplace(x/2,m);
  }

  cout << x/2 << " " << (x-1)/2 << endl;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout << fixed << setprecision(9);
  
  int T,C=1; cin >> T;
  
  while(T--) {
    cout << "Case #" << C++ << ": ";
    //cout << do_case() << endl;
    do_case();
  }
  
  return 0;
}
