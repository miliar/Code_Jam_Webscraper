#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

//7 -> 4 / 3
//6 -> 3 / 3
pair<unsigned long long, unsigned long long> solve(unsigned long long N, unsigned long long K) {
  //cout << "solve (" << N << ", " << K << ")" << endl;
  if (N <= K) {
    return make_pair(0, 0);
  }

  if (K == 1) {
    if (N%2 == 0) {
      return make_pair(N/2, N/2-1);
    } else {
      return make_pair(N/2, N/2);
    }
  }

  if (K % 2 == 1) {
    if (N % 2 == 0) {
      return solve(N/2-1,K/2); // correct ?!
    } else {
      return solve(N/2,K/2); // correct ?!
    }
  } else {
    if (N % 2 == 0) {
      return solve(N/2,K/2); // maybe not correct...
    } else {
      return solve(N/2,K/2); // looks correct
    }
  }
}

int main() {
  int T;
  cin >> T;
  for (int i=1; i<=T; i++) {
    unsigned long long N, K;
    cin >> N >> K;

    auto res = solve(N, K);

    cout << "Case #" << i << ": " << res.first << " " << res.second << endl;
    //cout << endl;
  }

  return 0;
}

