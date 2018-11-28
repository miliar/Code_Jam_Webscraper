#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <cstdlib>
#include <map>
#include <set>
#include <queue>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int tc;
	cin >> tc;
  for (int tt=1; tt<=tc; tt++)
  {
    int n, m;
    cin >> n >> m;
    string cake[100];
    for (int i=0;i<n;i++)
      cin >> cake[i];
    vector<int> allq;
    for (int i=0;i<n;i++)
    {
      int flag=1;
      char pre='@';
      for (int j=0;j<m;j++)
      {
        if (cake[i][j] == '?' && pre != '@')
          cake[i][j] = pre;
        else if (cake[i][j] != '?')
        {
          pre = cake[i][j];
          flag = 0;
        }

      }
      if (flag == 0)
      {
        char first;
        for (int j=0;j<m;j++)
          if (cake[i][j] != '?')
          {
            first = cake[i][j];
            break;
          }
        for (int j=0; cake[i][j] == '?';j++)
          cake[i][j] = first;
      }
      else
        allq.push_back(i);
    }
    for (int i=0; i<allq.size();i++)
      if (allq[i] != 0)
        cake[allq[i]] = cake[allq[i]-1];
    int firstr;
    for (int i=0;i<n;i++)
      if (cake[i][0] != '?')
      {
        firstr = i;
        break;
      }
    for (int i=0; i<firstr; i++)
      cake[i] = cake[firstr];

    cout << "Case #" << tt <<":" << endl;
    for (int i=0;  i<n; i++)
      cout << cake[i] << endl;

  }
}
