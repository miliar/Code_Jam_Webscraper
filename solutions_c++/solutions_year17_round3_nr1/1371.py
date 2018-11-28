#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <cmath>
#include <cstdlib>
#include <cstdint>

using namespace std;

uint64_t N, K;

bool f(const pair<uint64_t, uint64_t>& p1, const pair<uint64_t, uint64_t>& p2) {
  return p1.first > p2.first;
}

bool f2(const uint64_t& u1, const uint64_t& u2) {
  return u1 > u2;
}

int main() {
  int T = 0;
  scanf("%d\n", &T);
  for (int t = 1; t <= T; ++t) {
    cin >> N >> K;
    vector<pair<uint64_t, uint64_t>> v;
    for (uint64_t i = 0; i < N; ++i) {
      uint64_t r, h;
      cin >> r >> h;
      v.push_back(make_pair(r, h * r));
    }
    sort(v.begin(), v.end(), f);
    /*
    for (uint64_t i = 0; i < N; ++i) {
      cout << v[i].first << " " << v[i].second << endl;
    }
    */
    double m = 0;
    for (uint64_t i = 0; i < N; ++i) {
      double s = v[i].first * v[i].first * M_PI + 2 * v[i].second * M_PI;
      //cout << "m1: " << v[i].first << endl;
      vector<uint64_t> rr;
      for (uint64_t j = i + 1; j < N; ++j) {
        rr.push_back(v[j].second);
      }
      if (rr.size() < K - 1) {
        break;
      }
      sort(rr.begin(), rr.end(), f2);
      for (uint64_t j = 0; j < K - 1; ++j) {
        //cout << "m2: " << rr[j] << endl;
        s += 2 * M_PI * rr[j];
      }
      m = max(m, s);
    }
    cout << "Case #" << t << ": ";
    printf("%.6f", m);
    cout << endl;
  }
}
