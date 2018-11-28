#include <iostream>
#include <iomanip>
#include <sstream>
#include <vector>
#include <map>
#include <unordered_map>

using namespace std;

struct act {
  int x, y;
  int a; // who
};

int main()
{
  int T;
  cin >> T;

  auto cmp = [] (const act& l, const act& r) {
    return l.x < r.x;
  };

  for (int i = 0; i < T; i++)
  {
    int ac, aj;
    cin >> ac >> aj;

    vector<act> acts(ac+aj);
    for (int j = 0; j < ac+aj; j++) {
      cin >> acts[j].x >> acts[j].y;
      acts[j].a = (j < ac ? 0 : 1);
    }

    int res = 2;

    if (acts.size() > 1) {
      res = 0;
      sort(acts.begin(), acts.end(), cmp);

      int x[2];
      x[0] = x[1] = 0;
      int a = 0;
      vector<int> vXX[2];

      for (int j = 0; j < ac+aj; j++) {
        auto& cur = acts[j];
        auto& next = acts[(j+1 < ac+aj ? (j+1): (0))];

        x[cur.a] += cur.y - cur.x;

        int dist = next.x - cur.y;
        if (dist < 0) dist += 24*60;
        if (cur.a == next.a) {
          vXX[cur.a].push_back(dist);
          x[cur.a] += dist;
        } else {
          res += 1;
        }
      }

      if (x[0] > 720 || x[1] > 720) {
        int iBad = x[0] > 720 ? 0 : 1;
        auto& vBad = vXX[iBad];
        auto& xBad = x[iBad];
        sort(vBad.rbegin(), vBad.rend());
        for (auto& c : vBad) {
          res += 2;
          xBad -= c;
          if (xBad <= 720) break;
        }
      }

    }

    cout << "Case #" << i+1 << ": " << setprecision(8) << res << endl;
  }

  return 0;
}
