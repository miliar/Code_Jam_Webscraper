#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <utility>
using namespace std;

int T, N, C, M, rides, dp[1001], prom[1001], maxc, maxb, countr[1001], alive[1001], last[1001];
vector<vector<int>> plane(1001);

int main() {
  ifstream fin("B-large.in");
  ofstream fout("B-large.out");
  fin >> T;
  for (int t = 1 ; t <= T ; t++) {
    fin >> N >> C >> M;
    for (int i = 0 ; i <= N ; i++) {
      plane[i].clear();
      alive[i] = 0;
    }
    for (int i = 0 ; i <= 1000 ; i++) {
      dp[i] = 0;
      prom[i] = 0;
      last[i] = 0;
    }
    for (int i = 1 ; i <= C ; i++) {
      countr[i] = 0;
    }
    for (int i = 0 ; i < M ; i++) {
      int b, c;
      fin >> b >> c;
      plane[b].push_back(c);
      countr[c]++;
    }
    maxc = 0;
    for (int i = 1 ; i <= C ; i++) {
      maxc = max(maxc, countr[i]);
    }
    maxb = maxc;
    for (int p = N ; p >= 1 ; p--) {
      int num = plane[p].size();
      maxb = max(maxb, num);
      for (int i = maxc ; i <= maxb ; i++) {
        if (num > i) {
          prom[i] += num - i;
          dp[i] += num - i;
        } else {
          dp[i] = max(0, dp[i] - (i - num));
        }
      }
    }
    for (int i = maxc ; i <= maxb ; i++) {
      last[i+dp[i]] = prom[i] - dp[i] + 1;
    }
    rides = 0;
    while (last[rides] == 0) rides++;

    fout << "Case #" << t << ": " << rides << " " << last[rides]-1 << endl;
  }
  return 0;
}