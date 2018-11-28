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

#define NOCOLOR -1
#define RED 1
#define YELLOW 2
#define BLUE 3

using namespace std;

int n, r, o, y, g, b, v;
bool possible;
int color[MAXN];
string res;

void read_input()
{
  cin >> n >> r >> o >> y >> g >> b >> v;
}

void print_output(int tc)
{
  cout << "Case #" << tc << ": ";
  if (possible)
    cout << res;
  else
    cout << "IMPOSSIBLE";
  cout << endl;
}

inline bool check_possibility()
{
  return (((r + y) >= b) && ((r + b) >= y) && ((y + b) >= r));
}

char color_to_letter(int c)
{
  switch (c)
  {
    case RED:
      return 'R';
      break;
    case BLUE:
      return 'B';
      break;
    case YELLOW:
      return 'Y';
      break;
  }
  return 'Y';
}

inline void dec_color(int c)
{
  switch (c)
  {
    case RED:
      r--;
      break;
    case BLUE:
      b--;
      break;
    case YELLOW:
      y--;
      break;
  }
}

void solve()
{
  for (int i = 0; i < n; ++i)
    color[i] = -1;
  int max_color = max(r,max(y,b));
  if (max_color == r)       max_color = RED;
  else if (max_color == b) max_color = BLUE;
  else                   max_color = YELLOW;
  possible = check_possibility();
  if (possible)
  {
    color[0] = max_color;
    dec_color(max_color);
    int last_max = max_color;
    for (int i = 1; i < n; ++i)
    {
      last_max = max_color;
      if (last_max == RED)    max_color = (y > b) ? YELLOW : BLUE;
      else if (last_max == BLUE) max_color = (r > y) ? RED : YELLOW;
      else  max_color = (r > b) ? RED : BLUE;
      dec_color(max_color);
      color[i] = max_color;
    }
    if (color[0] == color[n-1]) 
    {
      int ttmp = color[n-2];
      color[n-2] = color[n-1];
      color[n-1] = ttmp;
    }
    res.resize(n);
    for (int i = 0; i < n; ++i)
      res[i] = color_to_letter(color[i]);
  }
}


int main(int argc, const char *argv[])
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
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

