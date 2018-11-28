#include <iostream>
#include <string>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

int gL(int base, int per) {
  return (base*10 + per*11-1)/(per*11);
}
int gM(int base, int per) {
  return (base*10)/(per*9);
}

int main() {
  int T;

  cin >> T;

  for (int t=1;t<=T;t++) {
    int N, P;
    cin >> N >> P;
    vector<int> R(N);
    for (int i=0;i<N;i++) {
      cin >> R[i];
    }
    vector<vector<int>> Q(N, vector<int>(P));
    set<pair<int,int>> least, most;
    for (int i=0;i<N;i++) {
      for (int j=0;j<P;j++) {
        cin >> Q[i][j];
      }
      sort(Q[i].begin(), Q[i].end());
      //cout << Q[i].back() << "/" << R[i] << endl;
      //cout << gL(Q[i].back(), R[i]) << endl;
      //cout << gM(Q[i].back(), R[i]) << endl;
      least.emplace(gL(Q[i].back(), R[i]), i);
      most.emplace(gM(Q[i].back(), R[i]), i);
    }

    int kits = 0;
    while (true) {
      auto maxleast = *least.rbegin();
      auto minmost = *most.begin();
      //cout << maxleast.first << endl;
      //cout << minmost.first << endl;
      if (maxleast.first <= minmost.first) {
        kits++;
        least.clear();
        most.clear();
        for (int i=0;i<N;i++) {
          Q[i].pop_back();
          if (Q[i].empty()) break;
          least.emplace(gL(Q[i].back(), R[i]), i);
          most.emplace(gM(Q[i].back(), R[i]), i);
        }
        if (least.size() != N) break;
      }
      else {
        int pop = maxleast.second;
        most.erase(make_pair(gM(Q[pop].back(), R[pop]), pop));
        least.erase(maxleast);

        Q[pop].pop_back();
        if (Q[pop].empty()) break;
        least.emplace(gL(Q[pop].back(), R[pop]), pop);
        most.emplace(gM(Q[pop].back(), R[pop]), pop);
      }
    }

    printf("Case #%d: %d\n", t, kits);
  }

}
