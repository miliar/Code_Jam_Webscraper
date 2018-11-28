#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <queue>
#include <string>
#include <set>
#include <queue>
#include <map>
#include <math.h>
#include <stack>
#include <sstream>
#include <bitset>
#include <ctime>
#include <chrono>

using namespace std;

#define lol long long
#define ll long long
#define pii pair<int, int>
#define pll pair<ll, ll>
#define pdd pair<double, double>
#define endl "\n"
#define mp make_pair
#define y1 asdskdjgsasdasd123
#define x1 sdkjfksdasdjfk
#define y2 sdkjfks123
#define x2 skaaaasd


#include <fstream>
ifstream in("input.in");
ofstream out("output.out");
#define cin in
#define cout out
/**/

int main()
{
  ios_base::sync_with_stdio(0);
  cout.precision(12);
  cout << fixed;

  int ttt;
  cin >> ttt;
  for (int t = 0; t < ttt; ++t)
  {
    int n;
    cin >> n;
    int r, o, y, g, b, v;
    cin >> r >> o >> y >> g >> b >> v;

    int mx = max(max(r,b), y);

    string w = "RYB";
    vector<int> ww = {r, y, b};

    if (mx > n / 2)
      cout << "CASE #" << t+1 << ": " << "IMPOSSIBLE" << endl;
    else
    {
      string val;

      if (r == 0)
      {
        for (int i = 0; i < b; ++i)
          val += "BY";
      }
      else if (b == 0)
      {
        for (int i = 0; i < r; ++i)
          val += "RY";
      }
      else if (y == 0)
      {
        for (int i = 0; i < b; ++i)
          val += "RB";
      }
      else
      {
        for (int i = 0; i < n; ++i)
        {

          int mmxx = max_element(ww.begin(), ww.end()) - ww.begin();
          int mmnn = min_element(ww.begin(), ww.end()) - ww.begin();

          if (ww[mmxx] == ww[mmnn])
          {
            string v[6] = {"RBY", "RYB", "BYR", "BRY", "YBR", "YRB"};
            string ss;
            for (int i = 0; i < 6; ++i)
              if (val.empty() || (val.back() != v[i][0] && val.front() != v[i][2]))
              {
                ss = v[i];
                break;
              }

            for (int j = 0; j < ww[mmnn]; ++j)
              val += ss;
            break;
          }

          if (val.empty())
          {
            val += w[mmxx];
            ww[mmxx]--;
          }
          else
          {
            if (val.back() == w[mmxx])
            {
              val.push_back(w[3 - mmxx - mmnn]);
              ww[3 - mmxx - mmnn]--;
            }
            else
            {
              val.push_back(w[mmxx]);
              --ww[mmxx];
            }
          }
        }
      }

      cout << "CASE #" << t+1 << ": " << val << endl;
    }
  }

  return 0;
}
