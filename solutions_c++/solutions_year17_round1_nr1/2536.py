#include <iostream>
#include <vector>
using namespace std;
int main()
{
  int t, tt, r, c, i, j, k, x, y;
  string m[26];
  vector<pair<int, int> > v;
  cin >> t;
  for (tt = 1; tt <= t; tt++)
  {
    cin >> r >> c;
    v.clear();
    for (i = 0; i < r; i++)
    {
      cin >> m[i];
      for (j = 0; j < c; j++)
        if (m[i][j] != '?') v.push_back(make_pair(i, j));
    }
    i = 0;
    while (i < v.size())
    {
      for (j = i; j < v.size() && v[j].first == v[i].first; j++);
      for (k = i; k < j; k++)
      {
        for (y = v[k].second - 1; y >= 0 && m[v[k].first][y] == '?'; y--)
          m[v[k].first][y] = m[v[k].first][v[k].second];
        for (x = v[k].first - 1; x >= 0; x--)
        {
          for (y = v[k].second; y >= 0 && m[x][y] == '?'; y--)
            m[x][y] = m[v[k].first][v[k].second];
          if (y == v[k].second) break;
        }
      }
      k--;
      for (x = v[k].first; x >= 0; x--)
      {
        for (y = v[k].second + 1; y < c && m[x][y] == '?'; y++)
          m[x][y] = m[v[k].first][v[k].second];
        if (y == v[k].second + 1) break;
      }
      i = j;
    }
    for (i = 0; i < r; i++)
    {
      if (m[i][0] == '?')
      {
        for (; i < r; i++)
          for (j = 0; j < c; j++)
            m[i][j] = m[i - 1][j];
        break;
      }
    }
    cout << "Case #" << tt << ": " << endl;
    for (i = 0; i < r; i++)
      cout << m[i] << endl;
  }
  return 0;
}
