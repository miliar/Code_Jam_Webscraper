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

vector<pll> h;
vector<ll> g;
int n;

double f()
{
  double INF = 1e18;
  vector<double> mn(n, INF);
  mn[0] = 0;
  for (int i = 0; i < n - 1; ++i)
  {
    if (mn[i] == INF)
    {
      cout << "";
    }
    ll curDist = 0;
    for (int j = i + 1; j < n && (curDist + g[j - 1] <= h[i].first); ++j)
    {
       mn[j] = min(mn[j], mn[i] + (curDist + g[j - 1]) / (h[i].second + .0));
       curDist += g[j - 1];
    }
  }

  return mn.back();
}

int main()
{
  ios_base::sync_with_stdio(0);
  cout << fixed << std::setprecision(12);

  int ttt;
  cin >> ttt;
  for (int t = 0; t < ttt; ++t)
  {
    int q;
    cin >> n >> q;

    h.resize(n);
    for (int i = 0; i < n; ++i)
      cin >> h[i].first >> h[i].second;

    vector<vector<ll>> d(n, vector<ll>(n));
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < n; ++j)
        cin >> d[i][j];


    for (int i = 0; i < n - 1; ++i)
    {
      g.push_back(d[i][i + 1]);
    }

    ll xx;
    cin >> xx >> xx;
    g.clear();

    cout << "CASE #" << t+1 << ": " << f() << endl;
  }

  return 0;
}
