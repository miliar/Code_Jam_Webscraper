// C++11
#include <cstdio>
#include <algorithm>
#include <vector>
#include <functional>
using namespace std;

const int dy[4] = {0, 1, 0, -1};
const int dx[4] = {1, 0, -1, 0};
const int dirconv0[4] = {3, 2, 1, 0};
const int dirconv1[4] = {1, 0, 3, 2};

int main() {
  int T; scanf("%d", &T);
  for(int tci = 0; tci < T; ++tci) {
    int R, C; scanf("%d%d", &R, &C);
    static char tbl[52][52];
    for(int i = 0; i < R; ++i) {
      scanf(" %s", tbl[i]);
    }
    vector<pair<int,int>> beam_positions;
    int whole_ok = true;
    vector<vector<int>> constraints;
    vector<vector<vector<int>>> covers(R, vector<vector<int>>(C));
    for(int by = 0; by < R; ++by) {
      for(int bx = 0; bx < C; ++bx) {
        if(tbl[by][bx] != '-' && tbl[by][bx] != '|') continue;
        int beam_id = beam_positions.size();
        beam_positions.push_back(make_pair(by, bx));
        bool ok[2] = {true, true};
        vector<vector<pair<int,int>>> local_covers(2);
        for(int start_dir = 0; start_dir < 4; ++start_dir) {
          int y = by, x = bx, dir = start_dir;
          // printf("(%d, %d, %d)...\n", by, bx, dir);
          y += dy[dir];
          x += dx[dir];
          while(0 <= y && y < R && 0 <= x && x < C) {
            // printf("  (%d, %d, %d)\n", y, x, dir);
            if(tbl[y][x] == '#') break;
            if(tbl[y][x] == '-' || tbl[y][x] == '|') {
              ok[start_dir%2] = false;
              break;
            }
            if(tbl[y][x] == '.') {
              local_covers[start_dir%2].push_back(make_pair(y, x));
            }
            if(tbl[y][x] == '/') {
              dir = dirconv0[dir];
            } else if(tbl[y][x] == '\\') {
              dir = dirconv1[dir];
            }
            y += dy[dir];
            x += dx[dir];
          }
        }
        if(!ok[0] && !ok[1]) {
          whole_ok = false;
        } else if(!ok[0]) {
          constraints.push_back(vector<int>{beam_id*2+1, beam_id*2+1});
        } else if(!ok[1]) {
          constraints.push_back(vector<int>{beam_id*2, beam_id*2});
        }
        for(int i : {0, 1}) {
          if(!ok[i]) continue;
          for(pair<int,int> yx : local_covers[i]) {
              covers[yx.first][yx.second].push_back(beam_id * 2 + i);
          }
        }
        // printf("(%d, %d): ok=%d, %d\n", by, bx, ok[0], ok[1]);
      }
    }
    if(!whole_ok) {
      printf("Case #%d: IMPOSSIBLE\n", tci + 1);
      continue;
    }
    for(int by = 0; by < R; ++by) {
      for(int bx = 0; bx < C; ++bx) {
        if(tbl[by][bx] != '.') continue;
        vector<int> &c = covers[by][bx];
        if(c.size() == 0) {
          whole_ok = false;
        } else if(c.size() == 1) {
          constraints.push_back(vector<int>{c[0], c[0]});
        } else {
          constraints.push_back(vector<int>{c[0], c[1]});
        }
      }
    }
    if(!whole_ok) {
      printf("Case #%d: IMPOSSIBLE\n", tci + 1);
      continue;
    }
    // for(auto &x : constraints) {
    //   printf("(%d, %d)\n", x[0], x[1]);
    // }
    int len = beam_positions.size() * 2;
    static bool wf[200][200];
    for(int i = 0; i < len; ++i) fill(wf[i], wf[i]+len, false);
    for(auto &x : constraints) {
      wf[x[0]^1][x[1]] = true;
      wf[x[1]^1][x[0]] = true;
    }
    for(int i = 0; i < len; ++i) wf[i][i] = true;
    for(int k = 0; k < len; ++k) {
      for(int i = 0; i < len; ++i) {
        for(int j = 0; j < len; ++j) {
          wf[i][j] = wf[i][j] || (wf[i][k] && wf[k][j]);
        }
      }
    }
    vector<int> ordering(len, -2);
    int ordering_fresh = 0;
    function<void(int)> visit = [&](int v) {
      if(ordering[v] != -2) return;
      ordering[v] = -1;
      for(int w = 0; w < len; ++w) {
        if(wf[w][v]) visit(w);
      }
      ordering[v] = ordering_fresh++;
    };
    for(int v = 0; v < len; ++v) visit(v);
    for(int beam_id = 0; beam_id < (int)beam_positions.size(); ++beam_id) {
      int y = beam_positions[beam_id].first;
      int x = beam_positions[beam_id].second;
      if(wf[beam_id*2][beam_id*2+1] && wf[beam_id*2+1][beam_id*2]) {
        whole_ok = false;
      }
      if(ordering[beam_id*2+1] < ordering[beam_id*2]) {
        tbl[y][x] = '-';
      } else {
        tbl[y][x] = '|';
      }
    }
    if(!whole_ok) {
      printf("Case #%d: IMPOSSIBLE\n", tci + 1);
      continue;
    }
    printf("Case #%d: POSSIBLE\n", tci + 1);
    for(int i = 0; i < R; ++i) {
      printf("%s\n", tbl[i]);
    }
  }
  return 0;
}
