#include <bits/stdc++.h>
using namespace std;
const int p[] = {1, 4, 16, 64, 256, 1024};

int n, m, coveredCol[5];
string a[55];
int f[55][1111];
pair<int,int> tr[55][1111];

int isShooter(int x, int y)
{
  return a[x][y] == '|' || a[x][y] == '-';
}

void flip(int x, int y)
{
  a[x][y] = a[x][y] == '|' ? '-' : '|';
}

int checkCol(int y, int state[], int covered[])
{
  for (int x = 0; x < m; x++)
    covered[x] = 0;

  for (int x = 0; x < m; x++)
    if (a[x][y] == '-')
    {
      if (state[x] == 1 || state[x] == 2)
        return 0;
    }
    else if (a[x][y] == '|')
    {
      if (state[x] == 3)
        return 0;
      for (int i = x - 1; i >= 0; i--)
        if (isShooter(i, y)) return 0;
        else if (a[i][y] == '#') break;
        else covered[i] = 1;
      for (int i = x + 1; i < m; i++)
        if (isShooter(i, y)) return 0;
        else if (a[i][y] == '#') break;
        else covered[i] = 1;
    }

  for (int x = 0; x < m; x++)
  {
    if (a[x][y] == '#' && state[x] == 3)
      return 0;
    if (a[x][y] == '.' && !covered[x] && state[x] == 2)
      return 0;
  }

  return 1;
}

void checkAll()
{
  int covered[55][55] = {0};
  for (int x = 0; x < m; x++)
    for (int y = 0; y < n; y++)
      if (a[x][y] == '|')
      {
        for (int i = x - 1; i >= 0; i--)
          if (a[i][y] == '#') break;
          else covered[i][y] = 1;
        for (int i = x + 1; i < m; i++)
          if (a[i][y] == '#') break;
          else covered[i][y] = 1;
      }
      else if (a[x][y] == '-')
      {
        for (int i = y - 1; i >= 0; i--)
          if (a[x][i] == '#') break;
          else covered[x][i] = 1;
        for (int i = y + 1; i < n; i++)
          if (a[x][i] == '#') break;
          else covered[x][i] = 1;
      }
  for (int x = 0; x < m; x++)
    for (int y = 0; y < n; y++)
      if (a[x][y] == '.')
        assert(covered[x][y] == 1);
}

void solveSmall()
{
  memset(f, 0, sizeof f);
  f[0][0] = 1;
  for (int j = 0; j < n; j++)
    for (int mask = 0; mask < p[m]; mask++)
      if (f[j][mask])
      {
        int ok = 1, state[5], tmp = mask;
        vector<int> pos;
        for (int i = 0; i < m; i++)
        {
          state[i] = tmp % 4;
          tmp /= 4;
        }

        for (int i = 0; i < m; i++)
          if (isShooter(i, j))
          {
            pos.push_back(i);
            if (state[i] == 1)
              ok = 0;
          }
        if (!ok) continue;

        for (int rotateMask = 0; rotateMask < 1 << pos.size(); rotateMask++)
        {
          for (int u = 0; u < pos.size(); u++)
            if (rotateMask >> u & 1)
              flip(pos[u], j);

          if (checkCol(j, state, coveredCol))
          {
            int newMask = 0;
            for (int i = 0; i < m; i++)
            {
              if (a[i][j] == '#') continue;
              if (a[i][j] == '-') newMask += p[i];
              else if (a[i][j] == '|') newMask += p[i] * 2;
              else if (state[i]) newMask += p[i] * state[i];
              else if (!coveredCol[i]) newMask += p[i] * 3;
            }
            f[j + 1][newMask] = 1;
            tr[j + 1][newMask] = {mask, rotateMask};
          }  

          for (int u = 0; u < pos.size(); u++)
            if (rotateMask >> u & 1)
              flip(pos[u], j);  
        }
      }

  for (int mask = 0; mask < p[m]; mask++)
    if (f[n][mask])
    {
      int tmp = mask, valid = 1;
      for (int i = 0; i < m; i++)
      {
        if (tmp % 4 == 3) valid = 0;
        tmp /= 4;
      }
      if (!valid) continue;

      cout << "POSSIBLE" << endl;
      for (int y = n, curMask = mask; y; y--)
      {
        int rotateMask = tr[y][curMask].second;
        curMask = tr[y][curMask].first;
        int cnt = 0;
        for (int x = 0; x < m; x++)
          if (isShooter(x, y - 1))
          {
            if (rotateMask >> cnt & 1)
              flip(x, y - 1);
            cnt++;
          }
      }
      checkAll();
      for (int i = 0; i < m; i++)
        cout << a[i] << endl;
      return;
    }

  cout << "IMPOSSIBLE" << endl;
}

int main()
{
  int test;
  cin >> test;
  for (int iTest = 1; iTest <= test; iTest++)
  {
    cerr << "Running test " << iTest << endl;
    cin >> m >> n;
    for (int i = 0; i < m; i++)
      cin >> a[i];
    cout << "Case #" << iTest << ": ";
    solveSmall();
  }
}