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

using namespace std;

int k, nmoves;
string s;
bool res;

void read_input()
{
  cin >> s >> k;
}

void print_output(int tc)
{
  cout << "Case #" << tc << ": ";
  if (res)
    cout << nmoves << endl;
  else
    cout << "IMPOSSIBLE" << endl;
}

inline void inverse(string& s, int start_pos)
{
  for (int i = 0; i < k; ++i)
    s[i+start_pos] = (s[i+start_pos] == '+') ? '-' : '+';
}

bool all_plus(string& s)
{
  for (size_t i = 0; i < s.length(); ++i)
    if (s[i] != '+') return false;
  return true;
}

void solve()
{
  nmoves = 0;
  size_t pos = 0;
//  cout << s.length() - k << endl;;
  while (pos <= s.length()-k)
  {
    if (s[pos] == '-')
    {
      inverse(s ,pos);
//      cout << s << endl;
      nmoves++;
    }
    pos++;
  }
  if (all_plus(s))  res = true;
  else              res = false;
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

