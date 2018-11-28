#include <iostream>
#include <map>
using namespace std;

typedef long long ll;

void do_case(int te) {
  ll n, k;
  cin >> n >> k;
  map<ll,ll> M;
  M[n] = 1;
  while(k > 0) {
    typeof(M.rbegin()) it = M.rbegin();
    ll nl = (it->first - 1) / 2;
    ll nh = it->first / 2;
    if (k > it->second) {
      k -= it->second;
      M[nl] += it->second;
      M[nh] += it->second;
      M.erase(it->first);
    } else {
      cout << "Case #" << te << ": " << nh << " " << nl << endl;
      k = 0;
    }
  }
}

int main () {
  int te, T=1;
  cin >> te;
  while(te--) {
    do_case(T);
    ++T;
  }
  return 0;
}