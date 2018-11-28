#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<ll, ll> ii;
typedef vector<ll> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;

#define INF 1e9
#define FOR(i, a, b) for(int i=int(a); i<int(b); i++)
#define FORC(cont, it) for(decltype((cont).begin()) it = (cont).begin(); it != (cont).end(); it++)
#define pb push_back

ii solve(ll n, ll k) {
  if (k == 1)
    return ii(n/2, (n-1)/2);
  if (k%2 == 1) 
    return solve((n-1)/2, k/2);
  else
    return solve(n/2, k/2);
}

int main() {
  ios::sync_with_stdio(false);
  ll t, n, k;
  cin >> t;
  for (int tc = 1; tc <= t; tc++) {
    cin >> n >> k;
    cout << "Case #" << tc << ": ";
    ii r = solve(n, k);
    cout << r.first << " " << r.second << endl;
  }
}
