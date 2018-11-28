#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;

int counts[1010];
int positions[1010];

int get_ceil(int N, int d) {
  if (N == 0) return 0;
  return (N - 1) / d + 1;
}

int main() {
  int T;
  cin >> T;
  for (int cas = 1; cas <= T; cas++) {
    int N;
    cin >> N;
    int C;
    cin >> C;
    int M;
    cin >> M;
    memset(counts, 0, sizeof(counts));
    memset(positions, 0, sizeof(positions));
    int B, P;
    int maximum = 0;
    for (int i = 0; i < M; i++) {
      cin >> P >> B;
      counts[B]++;
      maximum = max(maximum, counts[B]);
      positions[P]++;
    }
    cout << "Case #" << cas << ": ";
    int sum = 0;
    for (int i = 1; i <= N; i++) {
      sum += positions[i];
      maximum = max(maximum, get_ceil(sum, i));
    }
    cout << maximum << " ";
    int promotions = 0;
    for (int i = N; i >= 1; i--) {
      if (positions[i] > maximum) {
        promotions += positions[i] - maximum;
      }
    }
    cout << promotions << endl;
  }
}