#include <iostream>
#include <cmath>
#include <utility>
#include <vector>
#include <iomanip>
#include <set>

using namespace std;

static const double PI = 3.141592653589793238463;
int T, N, K;
double R[1005], H[1005]; 

double small_solve() {
  double res = 0.0;
  for (int msk = 0; msk < (1 << N); ++msk) {
    if (__builtin_popcount(msk) != K) {
      continue;
    }
    vector<pair<double, double> > cakes;
    for (int i = 0; i < N; ++i) {
      if ((msk >> i) & 1) {
        cakes.push_back(make_pair(R[i], H[i]));
      }
    }
    sort(cakes.rbegin(), cakes.rend());
    double area = PI * cakes[0].first * cakes[0].first;
    for (int i = 0; i < K; ++i) {
      area += 2 * PI * cakes[i].first * cakes[i].second;
    }
    res = max(res, area);
  }
  return res;
}

double solve() {
  vector<pair<double, double> > cakes;
  for (int i = 0; i < N; ++i) {
    cakes.push_back(make_pair(R[i] * H[i], i));
  }
  sort(cakes.rbegin(), cakes.rend());

  set<int> topK;
  double area1 = 0.0, area2 = cakes[K-1].first * 2 * PI;
  for (int i = 0; i < K; ++i) {
    area1 += cakes[i].first * 2 * PI;
    topK.insert(cakes[i].second);
  }

  double res = 0.0;
  for (int i = 0; i < N; ++i) {
    double area = PI * R[i] * R[i];
    if (topK.count(i) != 0) {
      res = max(res, area + area1);
    } else {
      double tmp = 2 * PI * R[i] * H[i];
      res = max(res, area + area1 - area2 + tmp);
    }
  }
  return res;
}

int main() {
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cin >> N >> K;
    for (int i = 0; i < N; ++i) {
      cin >> R[i] >> H[i];
    }
    cout << "Case #" << t << ": ";
    cout << setprecision(100) << solve() << endl;
  }
  return 0;
}