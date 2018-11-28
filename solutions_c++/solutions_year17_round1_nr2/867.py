#include <iostream>
#include <vector>
#include <cassert>
#include <algorithm>

using namespace std;

typedef pair<int, int> pii;

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; t++) {

    int N;
    int P;
    cin >> N >> P;

    vector<int> rs(N);
    for (int i = 0; i < N; i++) {
      cin >> rs[i];
    }

    vector<vector<int> > Q(N);
    vector<vector<pii> > W(N);
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < P; j++) {
        int x;
        cin >> x;
        Q[i].push_back(x);
      }
      sort(Q[i].begin(), Q[i].end());

      for (int j = 0; j < P; j++) {
        int r = rs[i];
        int a = (Q[i][j] * 10 + (r * 11) - 1) / (r * 11);
        int b = (Q[i][j] * 10) / (r * 9);
        W[i].push_back(make_pair(a, b));
        //cout << "W " << i << " " << a << " " << b << endl;
      }
    }

    int z = 0;
    for (int k = 1; ; ) {
      vector<int> ixs(N);
      int found = 1;
      int stop = 0;

      for (int i = 0; i < N; i++) {
        while (W[i].size() && W[i][0].second < k) {
          W[i].erase(W[i].begin());
        }
        if (W[i].size() == 0) {
          stop = 1;
          break;
        }
        if (k < W[i][0].first) {
          found = 0;
          break;
        }
      }

      if (stop) break;

      if (found) {
        //cout << "found ";
        for (int i = 0; i < N; i++) {
          //cout << ixs[i] << " ";
          W[i].erase(W[i].begin() + ixs[i]);
        }
        //cout << endl;
        z += 1;
      } else {
        k++;
      }
    }

    cout << "Case #" << (t + 1) << ": " << z << endl;
  }

  return 0;
}
