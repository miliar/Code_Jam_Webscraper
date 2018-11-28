#include<iostream>
using namespace std;

bool check(char *x)
{
  for (int i = 0; i < strlen(x) ; i++)
  {
    if (x[i] == '-') return false;
  }
  return true;
}
int fliping(char *x, int start, int size)
{
  for (int i = start; i < size + start ; i++)
  {
    if (x[i] == '-')
    {
      x[i] = '+';
    }
    else
    {
      x[i] = '-';
    }
  }
  return 1;
}
int main()
{
  freopen("A-large.in", "r", stdin);
  int t;
  cin >> t;
  for (int z = 1 ; z <= t; z++)
  {
    char x[1001];
    int size;
    cin >> x >> size;
    int nub = 0;
    int cakesize = strlen(x);
    cout << "Case #" << z << ": ";
    if (size == cakesize && check(x) == false)
    {
      nub += fliping(x, 0, size);
      if (check(x) == false)
      {
        cout << "IMPOSSIBLE" << endl;
        continue;
      }
      cout << nub << endl;
      continue;
    }
    int i;
    for (i = 0 ; i < strlen(x) - size; i++)
    {
      if (x[i] == '-')
      {
        nub += fliping(x, i, size);
      }
    }
    if (check(x) == false)
    {
      nub += fliping(x, i, size);
      if (check(x) == false)
      {
        cout << "IMPOSSIBLE" << endl;
        continue;
      }
      cout << nub << endl;
      continue;
    }
    cout << nub << endl;
  }
  return 0;
}
