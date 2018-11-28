#include <iostream>
#include <vector>
#include <cassert>
#include <algorithm>
#include <iomanip>

using namespace std;

double M_PI = 3.14159265359;
int N, K;
vector<long> hs, rs;

double check(int k) {
  vector<long> zs;
  for (int i = 0; i < N; i++) {
    if (i != k && rs[i] <= rs[k])
      zs.push_back(-rs[i] * hs[i]);
  }
  if (zs.size() < K - 1) 
    return -1.0;
  //sort(zs.begin(), zs.end(), std::greater<int>());
  sort(zs.begin(), zs.end());

  double total = 0.0;
  total += 2.0 * M_PI * rs[k] * hs[k];
  for (int i = 0; i < K - 1; i++) {
    total += 2.0 * M_PI * -zs[i];
  }
  total += M_PI * rs[k] * rs[k];
  //cout << "check " << k << " " << total << endl;
  return total;
}

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; t++) {
    cin >> N >> K;

    hs.clear();
    rs.clear();
    for (int i = 0; i < N; i++) {
      long r, h;
      cin >> r >> h;
      hs.push_back(h);
      rs.push_back(r);
    }

    double area = -1.0;
    for (int i = 0; i < N; i++) {
      area = max(area, check(i));
    }


    cout << setprecision(11);
    cout << "Case #" << (t + 1) << ": " << area << endl;
  }

  return 0;
}
