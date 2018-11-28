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

  int q;
  cin >> q;

  for (int t = 0; t < q; ++t)
  {
    ll n;
    ll k;
    string s;
    cin >> s;
    cin >> k;
    n = s.size();

    cout << "CASE #" << (t + 1) << ": ";

    vector<int> a;
    for (int i = 0; i < n; ++i)
      if (s[i] == '+')
        a.push_back(1);
    else
        a.push_back(0);

    int cnt = 0;

    for (int i = 0; i + k - 1 < n; ++i)
    {
      if (a[i] == 0)
      {
        ++cnt;
        for (int j = i; j < i + k; ++j)
          a[j] = 1 - a[j];
      }
    }

    bool ok = true;
    for (int i = 0; i < n; ++i)
      ok = ok && a[i];

    if (ok)
      cout << cnt << endl;
    else
      cout << "IMPOSSIBLE" << endl;
  }

  return 0;
}
