#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <deque>
#include <map>
#include <utility>
#include <algorithm>

using namespace std;

vector<int> init_pos;
vector<int> max_spd;

double solve(int D, int N)
{
  double dist_remain, time_remain, max_time_remain = 0;
  for (int i = 0; i < N; i++)
  {
    dist_remain = D - init_pos[i];
    time_remain = dist_remain / max_spd[i];
    if (time_remain > max_time_remain) max_time_remain = time_remain;
  }

  return D / max_time_remain;
}

int main(int argc, char * argv[])
{
  int D, N, ms, ip;
  double res;
  int nr_cases;
  cin >> nr_cases;

  cout << fixed;

  for (int cas = 1; cas <= nr_cases; cas++)
  {
    cin >> D >> N;

    init_pos.erase(init_pos.begin(), init_pos.end());
    max_spd.erase(max_spd.begin(), max_spd.end());

    for (int i = 0; i < N; i++)
    {
      cin >> ip >> ms;
      init_pos.push_back(ip);
      max_spd.push_back(ms);
    }

    res = solve(D, N);

    cout << "Case #" << cas << ": " << setprecision(6) << res << endl;
  }
}
