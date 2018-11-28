#include <bits/stdc++.h>
using namespace std;
int R, C;

const int MAXN = 30;
char board[MAXN][MAXN];

void bfs()
{
  queue<int> Q;
  for (int i = 1; i <= R; i++)
  {
    if (board[i][1] != '?')
      Q.push(i);
  }
  while (!Q.empty())
  {
    int cur = Q.front();
    Q.pop();
    if (cur > 1 && board[cur - 1][1] == '?')
    {
      memcpy(board[cur - 1], board[cur], sizeof(board[cur - 1]));
      Q.push(cur - 1);
    }
    if (cur < R && board[cur + 1][1] == '?')
    {
      memcpy(board[cur + 1], board[cur], sizeof(board[cur + 1]));
      Q.push(cur + 1);
    }
  }
}

int main()
{
  freopen("input", "r", stdin);
  freopen("output", "w", stdout);
  int T;
  cin >> T;
  for (int kase = 1; kase <= T; kase++)
  {
    cin >> R >> C;
    for (int i = 1; i <= R; i++)
    {
      scanf("%s", board[i] + 1);
    }
    for (int i = 1; i <= R; i++)
    {
      bool first = true;
      for (int j = 1; j <= C; j++)
      {
        if (first)
        {
          if (board[i][j] == '?')
            continue;
          else
          {
            for (int k = 1; k < j; k++)
              board[i][k] = board[i][j];
            char cur = board[i][j];
            for (++j; j <= C && board[i][j] == '?'; j++)
            {
              board[i][j] = cur;
            }
            --j;
            first = false;
          }
        }
        else
        {
          char cur = board[i][j];
          for (++j; j <= C && board[i][j] == '?'; j++)
          {
            board[i][j] = cur;
          }
          --j;
        }
      }
    }
    bfs();
    cout << "Case #" << kase << ": " << endl;
    for (int i = 1; i <= R; i++)
    {
      for (int j = 1; j <= C; j++)
      {
        cout << board[i][j];
      }
      cout << endl;
    }
  }
  return 0;
}