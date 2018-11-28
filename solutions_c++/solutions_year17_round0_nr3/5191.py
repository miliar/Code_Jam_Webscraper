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
    ll n, k;
    cin >> n >> k;

    cout << "CASE #" << (t + 1) << ": ";

    set<pii> s;
    s.insert(mp(-n, 0));
    for (int i = 0; i < k - 1; ++i)
    {
      pii const cur = *s.begin();
      int dist = -cur.first - 1;
      int idx = cur.second;

      s.erase(s.begin());
      int left = dist / 2;
      int right = dist - left;
      s.insert(mp(-left, idx));
      s.insert(mp(-right, idx + left + 1));
    }

    pii const cur = *s.begin();
    int const d = -cur.first - 1;
    cout << d - d / 2 << " " << d/2 << endl;
  }

  return 0;
}
