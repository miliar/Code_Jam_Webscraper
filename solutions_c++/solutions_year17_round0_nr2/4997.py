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

ll to_int(const string & s)
{
  ll res = 0;
  for (int i = s.size() - 1; i >= 0; --i)
  {
    res *= 10;
    res += (s[i] - '0');
  }

  return res;
}

int main()
{
  ios_base::sync_with_stdio(0);
  cout.precision(12);
  cout << fixed;

  int q;
  cin >> q;

  for (int t = 0; t < q; ++t)
  {
    ll n;
    cin >> n;
    stringstream ss;
    ss << n;
    string parsed = ss.str();
    int len = parsed.length();

    cout << "CASE #" << (t + 1) << ": ";

    if (len == 1)
    {
      cout << n << endl;
      continue;
    }

    ll res = to_int(string(len - 1, '9'));
    string cur;
    int prev = 0;
    bool ok = true;
    for (int i = 0; i < len; ++i)
    {
      if (parsed[i] < prev)
      {
        int j = cur.size() - 1;
        while (j >= 0 && cur[j] == cur.back())
          --j;
        if (cur[j + 1] == '1')
          ok = false;
        else
        {
          cur[j + 1]--;
          cur.resize(len);
          for (int k = j + 2; k < len; ++k)
            cur[k] = '9';
        }
        break;
      }
      else
      {
        cur.push_back(parsed[i]);
        prev = parsed[i];
      }
    }

    if (ok)
    {
      reverse(cur.begin(), cur.end());
      res = max(res, to_int(cur));
    }

    cout << res << endl;
  }

  return 0;
}
