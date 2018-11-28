#include <bits/stdc++.h>

using namespace std;

double pi = 4*atan(1);

double calc(vector<int> &order, int K, vector<int> &R, vector<int> &H) {
  double ans = 0;
  int maxRad = -1;
  for (int i=0;i<K;i++) {
    if (i && R[order[i]] > R[order[i-1]]) {
      return -1.0;
    }
    ans += 2*pi*R[order[i]]*H[order[i]];
    maxRad = max(maxRad, R[order[i]]);
  }
  ans += pi*maxRad*maxRad;
  return ans;
}

double solve() {
  int N, K;
  cin >> N >> K;

  vector<int> R(N), H(N);
  for (int i=0;i<N;i++) {
    cin >> R[i] >> H[i];
  }

  vector<int> order(N);
  for (int i=0;i<N;i++)
    order[i] = i;

  double ans = -1;
  do {
    ans = max(ans, calc(order, K, R, H));
  } while (next_permutation(order.begin(), order.end()));

  return ans;
}

int main() {
  int T;
  cin >> T;
  for (int t=1;t<=T;t++) {
    printf("Case #%d: %lf\n", t, solve());
  }
  return 0;
}
