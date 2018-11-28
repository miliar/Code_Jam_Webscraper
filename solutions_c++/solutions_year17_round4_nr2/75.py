#include <iostream>
#include <vector>
#include <cassert>
#include <map>

using namespace std;
typedef long long ll;

int main() {
  ll T;
  cin >> T;
  for(ll cas=1; cas<=T; cas++) {
    ll n, c, m;
    cin >> n >> c >> m;
    vector<ll> CC(c, 0);
    vector<ll> CP(n, 0);
    for(ll i=0; i<m; i++) {
      ll p, b;
      cin >> p >> b;
      b--;
      p--;
      CC[b]++;
      CP[p]++;
    }

    ll rides = 0;
    for(ll i=0; i<c; i++) {
      rides = max(rides, CC[i]);
    }

    ll sum = 0;
    for(ll i=0; i<n; i++) {
      sum += CP[i];
      rides = max(rides, (sum+i)/(i+1));
    }

    ll promotions = 0;
    for(ll i=0; i<n; i++) {
      if(CP[i] > rides) {
        promotions += CP[i]-rides;
      }
    }

    cout << "Case #" << cas << ": " << rides << " " << promotions << endl;
  }
}
