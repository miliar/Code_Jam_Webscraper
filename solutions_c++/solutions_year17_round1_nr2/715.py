#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <unordered_set>
#include <set>
#include <unordered_map>
#include <map>

#include <cmath>
#include <climits>

using namespace std;

bool is_valid(vector<bool>& update, const vector<int>& required, const vector<int>& given, int N) {
  bool valid = true;
  int total_min = 0;
  fill(update.begin(), update.end(), 0);
  for (int i = 0; i < N; i++) {
    float ratio = (float)given[i] / (float)required[i];

    int min = ceil(ratio);
    int max = floor(ratio);

    while ((min - 1) * required[i] * 1.1 >= given[i]) {
      min--;
    }
    while ((max + 1) * required[i] * 0.9 <= given[i]) {
      max++;
    }

    // cout << given[i] << " " << required[i] << " " << min << " " << max << endl;

    if (min > max) {
      update[i] = true;
      valid = false;
    } else if (min > total_min) {
      total_min = min;
    }
  }

  for (int i = 0; i < N; i++) {
    float ratio = (float)given[i] / (float)required[i];
    int max = floor(ratio);

    while ((max + 1) * required[i] * 0.9 <= given[i]) {
      max++;
    }

    if (max < total_min) {
      update[i] = true;
      valid = false;
    }
  }

  // cout << valid << " " << total_min << "\n";

  return valid;
}

int main(int, char**) {

  int T;
  cin >> T;

  for (int t = 0; t < T; t++) {

    int N, P;
    cin >> N >> P;

    vector<int> required(N);
    for (int i = 0; i < N; i++) {
      cin >> required[i];
    }

    vector<vector<int>> packages(N, vector<int>(P));
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < P; j++) {
        cin >> packages[i][j];
      }
      std::sort(packages[i].begin(), packages[i].end());
    }

    vector<bool> update(N);
    vector<int> given(N, 0);
    vector<int> given_indices(N, 0);


    for (int i = 0; i < N; i++) {
      given[i] = packages[i][0];
    }

    int kits = 0;
    for(;;) {
      bool valid = is_valid(update, required, given, N);
      if (valid) {
        kits++;
      }
      for (int i  = 0; i < N; i++) {
        if (valid || update[i]) {
          given_indices[i]++;
          if (given_indices[i] >= P) {
            goto b1;
          }
          given[i] = packages[i][given_indices[i]];
        }
      }

    }
    b1:;

    cout << "Case #" << t + 1 << ": " << kits << "\n";

  }


  return 0;
}
