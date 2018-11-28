#include <iostream>
#include <iomanip>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <unordered_map>

using namespace std;

struct Incoming
{
  double time;
  int city;
  int horse;
  int64_t fuel;

  Incoming(double a,
    int b,
    int c,
    int64_t d)
  {
    time = a;
    city = b;
    horse = c;
    fuel = d;
  }

  bool operator<(const Incoming& rhs) const
  {
    return this->time > rhs.time;
  }
};

double solve(
  int u,
  int v,
  vector<int64_t> horseDist,
  vector<double> horseSpeed,
  const vector<vector<pair<int, int64_t>>>& outBound)
{
  set<pair<int, int>> visited;
  visited.emplace(u, u);
  vector<Incoming> queue;
  queue.emplace_back(0.0, u, u, horseDist[u]);

  while(true)
  {
    pop_heap(queue.begin(), queue.end());
    auto x = queue.back();
    queue.pop_back();
    if (x.city == v)
    {
      return x.time;
    }

    // don't change horse
    for (const auto& out : outBound[x.city])
    {
      if (out.second <= x.fuel)
      {
        // enter out.first with same horse
        pair<int, int> entrance(out.first, x.horse);
        if (visited.count(entrance) == 0) {
          visited.insert(entrance);
          queue.emplace_back(x.time + out.second / horseSpeed[x.horse], out.first, x.horse, x.fuel - out.second);
          push_heap(queue.begin(), queue.end());
        }
      }
    }

    // change horse
    for (const auto& out : outBound[x.city])
    {
      if (out.second <= horseDist[x.city])
      {
        // enter out.first with new horse
        pair<int, int> entrance(out.first, x.city);
        if (visited.count(entrance) == 0) {
          visited.insert(entrance);
          queue.emplace_back(x.time + out.second / horseSpeed[x.city], out.first, x.city, horseDist[x.city] - out.second);
          push_heap(queue.begin(), queue.end());
        }
      }
    }
  }
}

int main()
{
  int T;
  cin >> T;


  for (int i = 0; i < T; i++)
  {
    int N, Q;
    cin >> N >> Q;

    vector<int64_t> horseDist(N);
    vector<double> horseSpeed(N);
    for (int j = 0; j < N; j++)
    {
      cin >> horseDist[j] >> horseSpeed[j];
    }

    vector<vector<pair<int, int64_t>>> outBound(N);
    for (int j = 0; j < N; j++)
    {
      for (int k = 0; k < N; k++)
      {
        int64_t dist;
        cin >> dist;
        if (dist >= 0)
        {
          outBound[j].emplace_back(k, dist);
        }
      }
    }

    stringstream res;
    for (int q = 0; q < Q; q++)
    {
      int u, v;
      cin >> u >> v;
      u--;
      v--;
      if (q != 0) res << ' ';
      res << setprecision(8) << solve(u, v, horseDist, horseSpeed, outBound);
    }

    cout << "Case #" << i+1 << ": " << res.str() << endl;
  }

  return 0;
}
