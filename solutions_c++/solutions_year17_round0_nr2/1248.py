#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<utility>
#include<iomanip>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout << fixed << setprecision(12);

  int64_t T;
  cin >> T;
  for (int64_t t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": ";
    string N;
    cin >> N;
    string foo;
    vector<pair<int64_t,int64_t>> blocks;
    for (int64_t bs = 0; bs < N.size();) {
      int64_t be = bs + 1;
      for (; be < N.size(); ++be) {
        if (N[be] != N[bs]) break;
      }
      // [bs,be) constitutes a block
      blocks.push_back({N[bs], be-bs});
      bs = be;
    }
    blocks.push_back({'9'+1, 0});
    bool fall = false;
    for (int64_t i = 0; i < blocks.size()-1; ++i) {
      if (fall) {
        for (int64_t j = 0; j < blocks[i].second; ++j) foo += '9';
      } else if (blocks[i].first < blocks[i+1].first) {
        for (int64_t j = 0; j < blocks[i].second; ++j) foo += blocks[i].first;
      } else {
        if (!(i == 0 && blocks[i].first == '1')) {
          foo += blocks[i].first-1;
        }
        for (int64_t j = 0; j < blocks[i].second-1;++j) foo += '9';
        fall = true;
      }
    }
    cout << foo << '\n';
  }
  return 0;
}

