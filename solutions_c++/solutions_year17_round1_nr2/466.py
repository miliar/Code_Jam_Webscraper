// C++11
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
  int T; scanf("%d", &T);
  for(int tci = 0; tci < T; ++tci) {
    int N, P; scanf("%d%d", &N, &P);
    vector<int> R(N);
    vector<vector<int>> Q(N, vector<int>(P));
    for(int i = 0; i < N; ++i) {
      scanf("%d", &R[i]);
    }
    for(int i = 0; i < N; ++i) {
      for(int j = 0; j < P; ++j) {
        scanf("%d", &Q[i][j]);
      }
      sort(Q[i].begin(), Q[i].end());
      reverse(Q[i].begin(), Q[i].end());
    }
    int count = 0;
    while(true) {
      int minidx = 0;
      for(int i = 0; i < N; ++i) {
        if((long long)Q[i].back() * R[minidx] < (long long)Q[minidx].back() * R[i]) {
          minidx = i;
        }
      }
      int ub = Q[minidx].back() * 10 / (R[minidx] * 9);
      bool ok = true;
      for(int i = 0; i < N; ++i) {
        int lb = (Q[i].back() * 10 + R[i] * 11 - 1) / (R[i] * 11);
        if(lb > ub) ok = false;
      }
      bool fin = false;
      if(ok) {
        ++count;
        for(int i = 0; i < N; ++i) {
          Q[i].pop_back();
          if(Q[i].empty()) fin = true;
        }
      } else {
        Q[minidx].pop_back();
        if(Q[minidx].empty()) fin = true;
      }
      if(fin) break;
    }
    printf("Case #%d: %d\n", tci + 1, count);
  }
  return 0;
}
