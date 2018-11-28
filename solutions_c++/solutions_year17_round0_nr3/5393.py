#include <bits/stdc++.h>

using namespace std;

const int N = int(1e6 + 5);

bool used[N];

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; i++) {
    memset(used, false, sizeof(used));
    int n, k;
    cin >> n >> k;
    for (int j = 0; j < k; j++) {
      int minMax = -1, maxMax = -1, pos = -1;
      vector<int> occupied = {-1};
      for (int t = 0; t < n; t++) {
        if (used[t]) {
          occupied.push_back(t);
        }    
      }
      occupied.push_back(n);
      int p = 0;
      for (int t = 0; t < n; t++) {
        if (t > occupied[p + 1]) {
          p++;  
        }
        if (!used[t]) {
          int ls = t - occupied[p] - 1;
          int rs = occupied[p + 1] - t - 1;
          if (min(ls, rs) > minMax || min(ls, rs) == minMax && max(ls, rs) > maxMax) {
            minMax = min(ls, rs);
            maxMax = max(ls, rs);
            pos = t;
          }  
        }  
      }
      used[pos] = 1;  
      if (j == k - 1) {
        cout << "Case #" << i + 1 << ": " << maxMax << " " << minMax << endl;
      }
    }
  }
}