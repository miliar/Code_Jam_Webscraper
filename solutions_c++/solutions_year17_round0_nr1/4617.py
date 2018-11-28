#include <iostream>
#include <bitset>

using namespace std;

#define N_MAX (1001)

int solve(bitset<N_MAX> &pancake_row, bitset<N_MAX> &mask, int K, int N) {
  //cout << "solve\n";
  int flips = 0;
  for (int start=0; start<=N-K; start++) {
    if (!pancake_row[start]) {
      //cout << "flip!\n";
      pancake_row ^= mask;
      flips++;
    }
    //cout << mask.to_string() << "\n";
    //cout << pancake_row.to_string() << "\n\n";
    mask <<= 1;
  }

  if (pancake_row.count() == N) return flips;
  return -1;
}


int main() {
  int T, K, flips;
  string s;
  bitset<N_MAX> pancake_row, mask;

  cin >> T;
  for (int i=0; i<T; i++) {
    cin >> s >> K;

    pancake_row.reset();
    mask.reset();

    for (int j=0; j<s.length(); j++) {
      if (s[j] == '+') pancake_row.set(j);
      if (j<K) mask.set(j);
    }

    flips = solve(pancake_row, mask, K, s.length());

    cout << "Case #" << i+1 << ": ";
    if (flips == -1) {
      cout << "IMPOSSIBLE\n";
    } else {
      cout << flips << "\n";
    }
  }
  return 0;
}
