#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

const int MAXN = 1111;
const double eps = 1e-7;

double D;
int N;
double K[MAXN], S[MAXN];
pair<int, int> all[MAXN];

inline bool sgn(double x) {
  return x < -eps ? -1 : x > eps;
}

bool check(double s)
{
  double t = D / s;
  for (int i = N - 1; i >= 0; --i) {
    if (S[i] * t + K[i] < D) {
      return false;
    }
  }
  return true;
}

double meet[MAXN], finish[MAXN];

int main() {
  int T;
  cin >> T;
  for (int cases = 0; cases < T; ++cases) {
    cin >> D >> N;
    for (int i = 0; i < N; ++i) {
      cin >> all[i].first >> all[i].second;
    }
    sort(all, all + N);
    for (int i = 0; i < N; ++i) {
      K[i] = all[i].first;
      S[i] = all[i].second;
    }
    meet[N - 1] = D;
    finish[N - 1] = double(D - K[N - 1]) / double(S[N - 1]);
    for (int i = N - 2; i >= 0; --i) {
      double t = double(K[i + 1] - K[i]) / double(S[i] - S[i + 1]);
      double dis = K[i] + S[i] * t;
      if (t <= 0) {
        finish[i] = double(D - K[i]) / double(S[i]);
      } else if (dis > meet[i + 1]) {
        meet[i] = meet[i + 1];
        finish[i] = (finish[i + 1] - double(meet[i + 1] - K[i + 1]) / double(S[i + 1])) + double(meet[i] - K[i]) / double(S[i]);
      } else {
        meet[i] = dis;
        finish[i] = finish[i + 1];
      }
    }
    // double l = 0, r = 1e9 + 5;
    // while (r - l >= eps) {
    //   double mid = (l + r) / 2.0;
    //   if (check(mid)) {
    //     l = mid + eps;
    //   } else {
    //     r =  mid - eps;
    //   }
    // }
    // cout << finish[0] << endl;
    printf("Case #%d: %.9lf\n", cases + 1, D / finish[0]);
  }
}