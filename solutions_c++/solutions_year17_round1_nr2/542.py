#include <cmath>
#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;

fstream in, out;

int T;
int N;
int P;
vector<int> R;
vector<vector<int> > Q, mins, maxs;
vector<vector<bool> > used;

int min(int x, int y) {
  if (x < y) {
    return x;
  } return y;
}

int max(int x, int y) { if(x < y) { return y; } return x;}

int get_min(int val, int R_val) {
  return (10 * val + 11 * R_val - 1) / (11 * R_val);
}

int get_max(int val, int R_val) {
  return (10 * val) / (9 * R_val);
}

bool get_cand(int mult) {
  vector<int> idxs;
  for (int j = 0; j < N; ++j) {
    bool found = false;
    for (int k = 0; k < P; ++k) {
      if (!used[j][k] && mins[j][k] <= mult && maxs[j][k] >= mult) {
        idxs.push_back(k);
        found = true;
        break;
      }
    }
    if (!found) {
      return false;
    }
  }
  for (int j = 0; j < N; ++j) {
    used[j][idxs[j]] = true;
  }
  return true;
}

int main() {
  in.open("B-small-attempt0.in", fstream::in);
  out.open("probb-small.out", fstream::out);
  
  in >> T;
  for (int i = 0; i < T; i++) {
    in >> N >> P;
    R.clear();
    Q.clear();
    used.clear();
    mins.clear();
    maxs.clear();

    int end = 0;
    for (int j = 0; j < N; ++j) {
      int temp;
      in >> temp;
      R.push_back(temp);
    }
    for (int j = 0; j < N; ++j) {
      Q.push_back(vector<int>());
      mins.push_back(vector<int>(P));
      maxs.push_back(vector<int>(P));
      used.push_back(vector<bool>());
      for (int k = 0; k < P; ++k) {
        int temp;
        in >> temp;
        Q[j].push_back(temp);
        used[j].push_back(false);
      }
      sort(Q[j].begin(), Q[j].end());
      for (int k = 0; k < P; ++k) {
        mins[j][k] = get_min(Q[j][k], R[j]);
        maxs[j][k] = get_max(Q[j][k], R[j]);
        if (maxs[j][k] > end) {
          end = maxs[j][k];
        }
      }
    }

    int ans = 0;
    int pack_size = 1;
    while (pack_size <= end) {
      if (get_cand(pack_size)) {
        ++ans;
      } else {
        ++pack_size;
      }      
    }
    out << "Case #" << i + 1 << ": " << ans << endl;
  }
    
  in.close();
  out.close();
  return 0;
}
