#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

int main() {
  int T; cin >> T;
  for(int i = 0; i < T; ++i) {
    int N, K; cin >> N >> K;
    vector<pair<long long,long long> > HRs(N);
    for(int j = 0; j < N; ++j) {
      long long R,H; cin >> R >> H;
      HRs[j] = make_pair(2*R*H,R*R);
    }
    sort(HRs.rbegin(), HRs.rend());
    long long area = 0;
    long long max_R_R = 0;
    long long max_R_H = 0;
    for(int j = 0; j < K; ++j) {
      area += HRs[j].first;
      if(HRs[j].second > max_R_R) {
        max_R_R = HRs[j].second;
      }
    }
    long long max_potential = (area + max_R_R);
    for(int j = K; j < N; ++j) {
      if(max_potential < (area - HRs[K-1].first + HRs[j].first + HRs[j].second )) {
        max_potential = (area - HRs[K-1].first + HRs[j].first + HRs[j].second);
      }
    }
    cout << fixed << setprecision(9) << "Case #" << i+1 << ": " << M_PI * (long double)max_potential << "\n";
  }
  return 0;
}
