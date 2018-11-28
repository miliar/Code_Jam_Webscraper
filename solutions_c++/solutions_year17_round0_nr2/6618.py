#include <ctime>
#include <climits>
#include <cstdlib>
#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <vector>
#include <utility>
#include <queue>
#include <iomanip>
#include <sstream>

#define PI 3.14159265
#define INF LLONG_MAX

using namespace std;

string in;
long long n, res;

void read_input()
{
  cin >> in;

}

void print_output(int tc)
{
  cout << "Case #" << tc << ": " << res << endl;
}

long long str_to_number(string& s)
{
  istringstream is(string(s.begin(), s.end()));
  long long r;
  is >> r;
  return r;
}

// str -> n of type string
long long get_solution(string& str, size_t first_pos, int bigegst_digit, int len)
{
  long long pref = 0;
  if (first_pos > 0)
  {
    string buffer = str.substr(0, first_pos);
    istringstream is(buffer);
    is >> pref;
  }
  else
    pref = 0;
  pref *= 10;
  pref += bigegst_digit;
  len -= (first_pos + 1);
  while (len > 0)
  {
    pref *= 10;
    pref += 9;
    len--;
  }
  return pref;
}

long long my_min(long long a, long long b)
{
  if (a == -1) return b;
  if (b == -1) return a;
  if (a < b) return a;
  return b;
}

bool is_tidy(long long r)
{
  int prevd = r % 10;
  r = r/10;
  while (r > 0)
  {
    int curd = r % 10;
    if ( curd > prevd ) return false;
    prevd = curd;
    r = r/10;
  }
  return true;
}

void solve()
{
  int ndigits = in.length();
  res = -1;
  n = str_to_number(in);
  for (int i = 0; i < ndigits; ++i)
  {
    for (int d = 0; d <= in[i]-'0'; ++d)
    {
      long long tmp = get_solution(in, i, d, ndigits);
      if ((tmp <= n) && (is_tidy(tmp)))
        res = max(res,tmp);
    }
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

