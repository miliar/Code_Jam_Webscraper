#include <bits/stdc++.h>
using namespace std;

const int MAXN = 50;
const double ep = 1e-10;

bool stop = false;
int N, P;
int R[MAXN];
int Q[MAXN][MAXN];
int cursor[MAXN];
int cnt = 0;

void clear()
{
  stop = false;
  memset(R, 0, sizeof R);
  memset(Q, 0, sizeof Q);
  memset(cursor, 0, sizeof cursor);
  cnt = 0;
}

bool satisfy()
{
  const int inf = 1e6;
  for (int r = 1; r <= inf; r++) {
    bool flag = true;
    for (int i = 0; i < N; i++) {
      double ratio = Q[i][cursor[i]] * 1.0 / r;
      if (!(ratio >= 0.9 * R[i] && ratio <= 1.1 * R[i])) {
        flag = false;
        break;
      }
    }
    if (flag) {
      return true;
    }
  }
  return false;
}

void move_max_ratio(int pos)
{
  while (cursor[pos] < P)
  {
    double ratio = Q[pos][cursor[pos]] * 1.0 / R[pos];
    if (ratio > 0.9)
    {
      cursor[pos]++;
      if (cursor[pos] == P)
      {
        stop = true;
      }
    }
  }
}

int main()
{
  freopen("input", "r", stdin);
  // freopen("output", "w", stdout);
  int T;
  cin >> T;
  for (int kase = 1; kase <= T; kase++)
  {
    clear();
    cin >> N >> P;
    for (int i = 0; i < N; i++)
    {
      cin >> R[i];
    }
    for (int i = 0; i < N; i++)
    {
      for (int j = 0; j < P; j++)
      {
        cin >> Q[i][j];
      }
    }

    for (int i = 0; i < N; i++)
    {
      sort(Q[i], Q[i] + P);
    }

    while (!stop)
    {
      if (satisfy())
      {
        cnt++;
        for (int i = 0; i < N; i++)
        {
          cursor[i]++;
          if (cursor[i] == P)
          {
            stop = true;
          }
        }
        continue;
      }
      // max not satisfy, move to the end
      double max_ratio = 0.0;
      int pos = -1;
      for (int i = 0; i < N; i++)
      {
        double ratio = Q[i][cursor[i]] * 1.0 / R[i];
        if (ratio > max_ratio)
        {
          max_ratio = ratio;
          pos = i;
        }
      }
      if (0.9 > max_ratio)
      {
        move_max_ratio(pos);
        continue;
      }
      // get min ratio, and move 1
      double min_ratio = 2 * 1e6;
      pos = -1;
      for (int i = 0; i < N; i++)
      {
        double ratio = Q[i][cursor[i]] * 1.0 / R[i];
        if (ratio < min_ratio)
        {
          min_ratio = ratio;
          pos = i;
        }
      }
      cursor[pos]++;
      if (cursor[pos] == P)
      {
        stop = true;
      }
    }
    cout << "Case #" << kase << ": " << cnt << endl;
  }
  return 0;
}