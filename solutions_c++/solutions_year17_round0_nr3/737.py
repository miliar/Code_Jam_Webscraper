#include <iostream>
#include <map>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    int64_t N, K;
    cin >> N >> K;
    map<int64_t, int64_t> m;
    m[N] = 1;
    int64_t A, B;
    while (true) {
      auto e = m.rbegin();
      auto s = e->first;
      auto count = e->second;
      m.erase(s);
      A = (s-1) / 2;
      B = s / 2;
      if (count >= K) {
        break;
      }
      K -= count;
      m[A] += count;
      m[B] += count;
    }
    cout << "Case #" << i + 1 << ": " << B << " " << A << endl;
  }

  return 0;
}
