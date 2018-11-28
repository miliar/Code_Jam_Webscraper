#include <cstdio>
#include <algorithm>
#include <utility>
#include <cmath>
#include <queue>
#include <cassert>

const int dr[4] = {0, 1, 0, -1};
const int dc[4] = {1, 0, -1, 0};

const int ref1[4] = {3, 2, 1, 0};
const int ref2[4] = {1, 0, 3, 2};

int main()
{
  int T;
  scanf("%d", &T);
  for (int t=1; t<=T; t++)
  {
    int R, C;
    scanf("%d%d ", &R, &C);
    char grid[52][52];
    for (int r = 0; r < R; r++)
    {
      scanf("%s", grid[r+1]+1);
      grid[r+1][0] = '#';
      grid[r+1][C+1] = '#';
    }
    for (int c = 0; c < C+2; c++)
      grid[0][c] = grid[R+1][c] = '#';
      
    bool implies[205][205] = {{}};
    int beam[52][52] = {{}};
    int beamid = 0;
    std::pair<int, int> beampos[105];
    for (int r = 1; r <= R; r++)
    for (int c = 1; c <= C; c++)
    {
      if (grid[r][c] == '-' || grid[r][c] == '|')
      {
        beampos[beamid] = std::make_pair(r, c);
        for (int dir = 0; dir < 2; dir++)
        {
          char mark[52][52] = {};
          bool bad = false;
          std::queue<std::pair<std::pair<int,int>, int> > q;
          q.push(std::make_pair(std::make_pair(r+dr[dir], c+dc[dir]), dir));
          q.push(std::make_pair(std::make_pair(r-dr[dir], c-dc[dir]), dir+2));
          while (!q.empty())
          {
            int rr = q.front().first.first;
            int cc = q.front().first.second;
            int d = q.front().second;
            q.pop();
            if (grid[rr][cc] == '-' || grid[rr][cc] == '|')
            {
              bad = true;
              break;
            }
            if (grid[rr][cc] == '#') continue;
            if (grid[rr][cc] == '/') d = ref1[d];
            if (grid[rr][cc] == '\\') d = ref2[d];
            if (grid[rr][cc] == '.') mark[rr][cc] = 1;
            q.push(std::make_pair(std::make_pair(rr+dr[d], cc+dc[d]), d));
          }
          if (bad)
          {
            implies[2*beamid+dir][2*beamid+!dir] = true;
          }
          else
          {
            for (int rr = 1; rr <= R; rr++)
            for (int cc = 1; cc <= C; cc++)
            {
              if (mark[rr][cc])
              {
                int me = 2*beamid + dir;
                if (beam[rr][cc])
                {
                  assert(beam[rr][cc] != -1);
                  int b = beam[rr][cc] - 1;
                  beam[rr][cc] = -1;
                  implies[b^1][me] = true;
                  implies[me^1][b] = true;
                }
                else
                {
                  beam[rr][cc] = me + 1;
                }
              }
            }
          }
        }
        beamid++;
      }
    }
    bool bad = false;
    for (int r = 1; r <= R; r++)
    for (int c = 1; c <= C; c++)
    {
      if (grid[r][c] == '.')
      {
        if (beam[r][c] == 0)
        {
          bad = true;
        }
        else if (beam[r][c] != -1)
        {
          int b = beam[r][c] - 1;
          implies[b^1][b] = true;
        }
      }
    }
    for (int k = 0; k < 2*beamid; k++)
    for (int i = 0; i < 2*beamid; i++)
    for (int j = 0; j < 2*beamid; j++)
      if (implies[i][k] && implies[k][j]) implies[i][j] = true;
    for (int i = 0; i < beamid; i++)
      if (implies[2*i][2*i+1] && implies[2*i+1][2*i])
        bad = true;
    if (bad)
    {
      printf("Case #%d: IMPOSSIBLE\n", t);
      continue;
    }
    printf("Case #%d: POSSIBLE\n", t);
    int beamstatus[105] = {};
    for (int i = 0; i < beamid; i++)
    {
      if (beamstatus[i]) continue;
      int badid;
      if (implies[2*i][2*i+1])
      {
        beamstatus[i] = -1;
        badid = 2*i;
      }
      else
      {
        beamstatus[i] = 1;
        badid = 2*i+1;
      }
      for (int j= 0; j < beamid; j++)
      {
        if (implies[2*j][badid])
        {
          assert(beamstatus[j] != 1);
          beamstatus[j] = -1;
        }
        if (implies[2*j+1][badid])
        {
          assert(beamstatus[j] != -1);
          beamstatus[j] = 1;
        }
      }
    }
    for (int i = 0; i < beamid; i++)
    {
      grid[beampos[i].first][beampos[i].second] = beamstatus[i] == 1 ? '-' : '|';
    }
    
    for (int i = 1; i <= R; i++)
    {
      for (int j = 1; j <= C; j++)
        putchar(grid[i][j]);
      putchar('\n');
    }
    putchar('\n');
  }
}