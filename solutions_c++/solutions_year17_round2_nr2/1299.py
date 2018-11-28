#include <iostream>

using namespace std;

int single[3], dual[3], augment[3];
int ret[1024];

int max_index(int exclude, int bias) {
  int ret = -1;
  int mx = 0;
  for (int i = 0; i < 3; ++i) {
    if (i == exclude || single[i] == 0) {
      continue;
    }

    if (single[i] > mx || (single[i] == mx && i == bias)) {
      mx = single[i];
      ret = i;
    }
  }
  return ret;
}

int solve() {
  int total = 0;
  for (int i = 0; i < 3; ++i) {
    if (single[i] < 0) {
      return -1;
    }
    total += single[i];
  }

  if (total == 0) {
    return 0;
  }

  int start = max_index(-1, -1);
  int it = 0;
  ret[it++] = start;
  single[start]--;
  for (int k = 0; k < total - 1; ++k) {
    int j = max_index(ret[it - 1], start);
    if (j == -1) {
      return -1;
    }
    ret[it++] = j;
    single[j]--;
  }
  if (ret[it - 1] == start) {
    return -1;
  }

  return it;
}

string single_colors = "RYB";
string dual_colors = "OGV";

int main() {
  int T; cin >> T;
  for (int t = 0; t < T; ++t) {
    int n; cin >> n;

    for (int i = 0; i < 3; ++i) {
      cin >> single[i] >> dual[i];
      augment[i] = 0;
    }
    for (int i = 0; i < 3; ++i) {
      int idx = (i + 2) % 3;
      single[idx] -= dual[i];
      augment[idx] = dual[i];
    }

    int total = solve();
    printf("Case #%d: ", t + 1);
    if (total == -1) {
      printf("IMPOSSIBLE\n");
    } else {
      string output;

      bool viz[3];
      for (int i = 0; i < 3; ++i) {
        viz[i] = false;
      }

      if (total == 0) {
        int augment_idx = -1;
        for (int i = 0; i < 3; ++i) {
          if (augment[i] > 0) {
            if (augment_idx != -1) {
              augment_idx = -1;
              break;
            }
            augment_idx = i;
          }
        }
        if (augment_idx == -1) {
          output = "IMPOSSIBLE";
        } else {
          for (int i = 0; i < augment[augment_idx]; ++i) {
            output += dual_colors[(augment_idx + 1) % 3];
            output += single_colors[augment_idx];
          }
        }
      } else {
        for (int i = 0; i < total; ++i) {
          int k = ret[i];
          output += single_colors[k];
          if (!viz[k] && augment[k] > 0) {
            viz[k] = true;
            for (int j = 0; j < augment[k]; ++k) {
              output += dual_colors[(k + 1) % 3];
              output += single_colors[k];
            }
          }
        }

        for (int i = 0; i < 3; ++i) {
          if (augment[i] > 0 && !viz[i]) {
            output = "IMPOSSIBLE";
            break;
          }
        }
      }
      cout << output << endl;
    }
  }
}
