#include <fstream>
#include <algorithm>
#include <queue>
#include <vector>
#include <iostream>
#include <cmath>
#include <string>

using namespace std;

void flip( char & s )
{
  if (s == '+')
    s = '-';
  else
    s = '+';
}

bool check( string & s )
{
  bool flag = true;

  for (int i = 0; i < s.size(); i++)
    if (s[i] != '+')
      flag = false;
  return flag;
}

int main( void )
{                   
  ifstream fin("A-large.in");
  ofstream fout("output.txt");
  int t, k;
  string s;
  fin >> t;
  for (int i = 0; i < t; i++)
  {
    int cnt = 0;
    fin >> s >> k;
    if (!check(s))
    {
      for (int j = 0; j < s.size() - k + 1; j++)
      {
        if (s[j] == '-')
        {
          for (int p = 0; p < k; p++)
            flip(s[j + p]);
          cnt++;
          if (check(s))
            break;
        }
      }
      if (!check(s))
        cnt = -1;
    }
    fout << "Case #" << i + 1 << ": ";
    if (cnt == -1)
      fout << "IMPOSSIBLE" << endl;
    else
      fout << cnt << endl;
  }
  return 0;
}