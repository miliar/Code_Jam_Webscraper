#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
#define DEBUG
#ifdef DEBUG
#define TRACE(x) cerr << #x << " = " << x << endl;
#define _ << " _ " <<
#else
#define TRACE(x) ((void)0)
#endif

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

  ll T;
  cin >> T;
  for (int tt = 1; tt <= T; tt++) {
    ll D, N;
    cin >> D >> N;
    ll K, S;
    ld maxt = 0;
    for (int i = 0; i < N; i++) {
      cin >> K >> S;
      maxt = max(maxt, ((ld)(D - K)) / S);
    }
    cout << "Case #" << tt << ": " << fixed << setprecision(10) << (ld)D / maxt << '\n';
  }

  return 0;
}
