#include <iostream>
#include <vector>
#include <string.h>
#include <algorithm>

using namespace std;

int T, K, N;
string S;
int main() {
  cin >> T;
  for(int t = 1; t <= T; t++) {
    cin >> S >> K;
    N = S.length();
    
    int ans = 0;
    int imp = 0;

    for(int i = 0; i + K - 1 < N; i++) {
      if (S[i] == '-') {
        ans++;
        for (int j = i; j <= i + K - 1; j++) S[j] = S[j] == '+' ? '-' : '+';
      }
    }

    for (int i = N - K + 1; i < N; i++) if (S[i] == '-') imp = 1;
    printf("Case #%d: %s\n", t, (imp ? "IMPOSSIBLE" : to_string(ans)).c_str());
  }
	return 0;
}
