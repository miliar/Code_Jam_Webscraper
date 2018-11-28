#include <algorithm>
#include <cinttypes>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <map>
#include <unordered_map>
#include <vector>
using namespace std;

struct pancake {
  long long int R;
  long long int H;
  long long int RH;
  long long int R2P2RH;
};

int T, N, K;
vector<pancake> P;
double pi = 3.141592653589793238;

int main(int argc, char *argv[]) {
  P.resize(1000);

  cout << fixed;
  cout << setprecision(20);

  double area = 0;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    P.clear();
    area = 0;
    cin >> N;
    cin >> K;
    P.resize(N);
    for (int j = 0; j < N; ++j) {
      cin >> P[j].R;
      cin >> P[j].H;
      P[j].RH = 2 * P[j].R * P[j].H;
      P[j].R2P2RH = P[j].R * P[j].R + P[j].RH;
    }

    sort(P.begin(), P.end(), [](const auto& x, const auto& y) { return x.RH > y.RH; });

    for (int j = 0; j < K - 1; ++j) {
      area += P[j].RH;
    }

    long long int kth = P[K - 1].RH;
    long long int max = -1;
    int max_j = -1;
    for (int j = 0; j < N; ++j) {
      if (P[j].R2P2RH > max) {
        max = P[j].R2P2RH;
        max_j = j;
      }
    }

    long long int rtestmax = P[max_j].R;

    if (max_j < K - 1) {
      area += kth;
      long long int max_r = rtestmax;
      int max_k = max_j;
      for (int j = 0; j < K; ++j) {
        if (P[j].R > max_r) {
          max_r = P[j].R;
          max_k = j;
        }
      }
      area += max_r * max_r;
    } else {
      area += max;
    }

    area *= pi;
    cout << "Case #" << i << ": " << area << endl;
  }

  return 0;
}
