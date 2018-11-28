#include<iostream>
#include<cstdlib>
#include<vector>

using namespace std;
int main()
{
  freopen("B-large.in", "r", stdin);
  //freopen("./output.txt", "w", stdout);
  int t, n;
  char x[20];
  cin >> t;
  for (int i = 1 ; i <= t; i++)
  {
    cin >> x;
    vector<char> p;
    cout << "Case #" << i << ": ";
    int pos = 0;
    if (strlen(x) == 1)
    {
      cout << x << endl;
      continue;
    }
    for (int j = 0; j < strlen(x) - 1 ; j++)
    {
      if (x[j] < x[j + 1])
      {
        pos = j + 1;
      }
      else if (x[j] > x[j + 1])
      {
        x[pos]--;
        for (int k = pos + 1; k < strlen(x); k++)
        {
          x[k] = '9';
        }
        break;
      }
    }
    for (int j = 0; j < strlen(x); j++)
    {
      if (j == 0 && x[j] == '0') continue;
      cout << x[j];
    }
    cout << endl;
  }
  return 0;
}
