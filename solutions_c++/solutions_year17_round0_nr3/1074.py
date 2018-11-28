#include <iostream>
#include <queue>
#include <cstdint>
#include <map>
using namespace std;

int64_t N, K;

int main() {
  int T;
  cin >> T;
  for(int caze = 1; caze <= T; caze++) {
    cin >> N >> K;
    map<int64_t, int64_t> split;
    split[N] = 1;
    int64_t lmin, lmax;
    for(int64_t i = 0; i < K; ) {
      int64_t key = split.rbegin()->first;
      int64_t count = split.rbegin()->second;
      int64_t length = key;
      lmin = min((length + 1) / 2, length + 1 - (length + 1) / 2) - 1;
      lmax = max((length + 1) / 2, length + 1 - (length + 1) / 2) - 1;
      split[lmin] += count;
      split[lmax] += count;
      split.erase(key);
      i += count;
    }
    
    cout << "Case #" << caze << ": " << lmax << " " << lmin << endl;
  }
}
