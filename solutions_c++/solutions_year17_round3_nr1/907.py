#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <numeric>
#include <map>
#include <set>
#include <queue>
#include <string.h>
#include <math.h>

typedef long long ll;
using namespace std;

const double PI = atan(1.0) * 4.0;

double solve(int N, int K, int *R, int *H) {
  double ans = 0.0;
  static pair<int, int> rh[1000100];
  for (int i = 0; i < N; i++) {
    rh[i] = make_pair(R[i], H[i]);
  }
  sort(rh, rh+N);
  int max_r = 0;
  priority_queue<double, vector<double>, greater<double> > q;
  double h = 0;
  for (int i = 0; i < K; i++) {
    max_r = max(max_r, rh[i].first);
    q.push(2.0 * PI * rh[i].first * rh[i].second);
    h += 2.0 * PI * rh[i].first * rh[i].second;
    //printf("max_r = %d, h = %g\n", max_r, h);
  }
  ans = h + PI * max_r * max_r;
  for (int i = K; i < N; i++) {
    max_r = max(max_r, rh[i].first);
    double next_h = q.top();
    q.pop();
    q.push(2.0 * PI * rh[i].first * rh[i].second);
    h += 2.0 * PI * rh[i].first * rh[i].second - next_h;
    ans = max(ans, h + PI * max_r * max_r);
    //printf("h = %d, next_h = %g\n", rh[i].second, next_h);
    //printf("max_r = %d, h = %g\n", max_r, h);
  }
  return ans;
}

int main()
{
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    int N, K;
    cin >> N >> K;
    static int R[1000100];
    static int H[1000100];
    for (int j = 0; j < N; j++) {
      cin >> R[j] >> H[j];
    }
    double ans = solve(N, K, R, H);
    printf("Case #%d: %.13f\n", i+1, ans);
  }
}
