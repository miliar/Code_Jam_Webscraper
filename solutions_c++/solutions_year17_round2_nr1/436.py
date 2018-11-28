#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<utility>
#include<iomanip>

using namespace std;

typedef long double ld;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout << fixed << setprecision(12);

  int64_t T;
  cin >> T;

  for (int64_t t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": ";
    int64_t D, N;
    cin >> D >> N;
    ld maxhit = 0;
    for (int64_t i = 0; i < N; ++i) {
      int64_t K, S;
      cin >> K >> S;
      maxhit = max(maxhit, (ld)(D-K)/(ld)S);
    }
    cout << (ld)D/maxhit << '\n';
  }
  return 0;
}
