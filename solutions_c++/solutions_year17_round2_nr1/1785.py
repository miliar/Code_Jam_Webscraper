#include <ctime>
#include <climits>
#include <cstdlib>
#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <stack>
#include <utility>
#include <queue>
#include <list>
#include <iomanip>
#include <set>

#define PI 3.14159265
#define INF LLONG_MAX
#define MAXN 1001

using namespace std;

int n;
long double d;
long double vi[MAXN], si[MAXN];
long double res;

void read_input()
{
  cin >> d >> n;
  for (int i = 0; i < n; ++i)
    cin >> si[i] >> vi[i];
}

void print_output(int tc)
{
  cout << "Case #" << tc << ": " << res << endl;;
}

long double get_max_speed( int i )
{
  return (vi[i] * d) / (d - si[i]);
}

void solve()
{
  res = numeric_limits<long double>::max();
  for (int i = 0; i < n; ++i)
    res = min(res, get_max_speed(i));
}


int main(int argc, const char *argv[])
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout << std::fixed;
  cout << std::setprecision(7);
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i)
  {
    read_input();
    solve();
    print_output(i+1);
  } 
  return 0;
}

