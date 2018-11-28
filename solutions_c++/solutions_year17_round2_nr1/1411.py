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
    double d;
    int n;
    cin >> d >> n;

    vector<pii> a(n);

    for (int i = 0; i < n; ++i)
      cin >> a[i].first >> a[i].second;

    sort(a.begin(), a.end());

    double val = 1e18;
    for (int i = 0; i < n; ++i)
      val = min(val, (d * a[i].second) / (d - a[i].first));

    cout << "CASE #" << t+1 << ": " << val << endl;
  }

  return 0;
}
