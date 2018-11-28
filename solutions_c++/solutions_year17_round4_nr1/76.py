#include <iostream>
#include <vector>
#include <cassert>
#include <map>

using namespace std;
typedef long long ll;

ostream& operator<<(ostream& o, vector<ll>& V) {
  o << "[";
  for(ll x : V) {
    o << " " << x;
  }
  o << "]";
  return o;
}

map<ll, ll> DP;
ll f(vector<ll>& C, ll sum) {
  assert(0 <= sum && sum < C.size());
  ll key = C.size() + (sum << 4);
  for(ll i=0; i<C.size(); i++) {
    key += (C[i]<<(8+10*i));
  }
  if(DP.count(key)==1) { return DP[key]; }

  bool done = true;
  ll best = 0;
  for(ll i=0; i<C.size(); i++) {
    if(C[i] > 0) {
      done = false;
      C[i]--;
      best = max(best, f(C, (sum+i)%C.size()));
      C[i]++;
    }
  }
  ll ans = best + (sum==0 && !done ? 1 : 0);
  DP[key] = ans;
  return ans;
}

int main() {
  ll T;
  cin >> T;
  for(ll cas=1; cas<=T; cas++) {
    ll n, p;
    cin >> n >> p;
    vector<ll> C(p, 0);
    for(ll i=0; i<n; i++) {
      ll gi;
      cin >> gi;
      C[gi%p]++;
    }
    cout << "Case #" << cas << ": " << f(C, 0) << endl;
  }
}
