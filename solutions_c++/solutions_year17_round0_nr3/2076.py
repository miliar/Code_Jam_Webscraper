#include <iostream>
#include <map>
#include <vector>
#include <utility>

using namespace std;

// if N == 1000
// 499 500
// 249 249 | 249 250
// 124 124 | 124 124 | 124 124 | 124 125
// 61 62 | 61 62 | 61 62 | 61 62 | 61 62 | 61 62 | 61 62 | 62 62
pair<long long, long long> findTerminalState(long long N, long long K) {
  vector<map<long long, long long>> gapLayers;
  gapLayers.emplace_back();
  gapLayers.back()[N] = 1;
  // k is how many gaps we've enumerated here
  long long k = 1;         
  while (k < K) {
    map<long long, long long> gapLayer;
    for (pair<long long, long long> gap : gapLayers.back()) {
      gapLayer[(gap.first - 1)/2] += gap.second;
      gapLayer[gap.first/2] += gap.second;
      k += 2LL*gap.second;
    }
    gapLayers.push_back(std::move(gapLayer));
  }
  // now k is how far we want to explore this layer
  k = K - (1LL << (gapLayers.size() - 1));    
  map<long long, long long>::const_reverse_iterator lastGapIt =
    gapLayers.back().rbegin();
  while (k >= lastGapIt -> second) {
    k -= lastGapIt -> second;
    ++lastGapIt;
  }
  long long lastGap = lastGapIt -> first;
  return make_pair(lastGap/2, (lastGap - 1)/2);
}

int main(int argc, char *argv[]) {
  ios::sync_with_stdio(false); cin.tie(NULL);
  int T; cin >> T;
  for (int t = 1; t <= T; ++t) {
    long long N; cin >> N;
    long long K; cin >> K;
    pair<long long, long long> terminalState = findTerminalState(N, K);    
    cout << "Case #" << t << ": ";
    cout << terminalState.first << ' ' << terminalState.second;
    cout << '\n';
  }
  cout << flush;
  return 0;
}
