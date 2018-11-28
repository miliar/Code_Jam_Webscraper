#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <unordered_map>

typedef int64_t II;

using namespace std;

int main()
{
  int T;
  cin >> T;

  for (int i = 0; i < T; i++)
  {
    II N, P;
    cin >> N >> P;
    vector<II> G(4);
    for (int i = 0; i < N; i++) {
      II x;
      cin >> x;
      x = x % P;
      G[x]++;
    }

    II res = 0;
    if (P == 2) {
      res = G[0] + (G[1]+1)/2;
    } else if (P == 3) {
      res = G[0] + min(G[1], G[2]) + (max(G[1], G[2]) - min(G[1], G[2]) + 2) / 3;
    } else {
      res = G[0];
      res += G[2] / 2;
      G[2] = G[2] % 2;
      auto x = min(G[1], G[3]);
      res += x;
      auto y = max(G[1], G[3]) - x;
      res += y / 4;
      y = y % 4;
      if (y >= 2 && G[2] > 0) {
        res += 1;
        y -= 2;
        G[2] = 0;
      }
      if (y > 0 || G[2] > 0) {
        res += 1;
      }
    }

    cout << "Case #" << i+1 << ": " << res << endl;
  }

  return 0;
}
