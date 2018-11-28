#include <iostream>
#include <stdio.h>
using namespace std;
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};
char map[100][100];
int cnt[100][100], R, C;

void place(int ox, int oy)
{
  bool heng = true, shu = true;
  for (int i = 0; i < 4; i++) {
    int x = ox, y = oy;
    while (x + dx[i] >= 0 && x + dx[i] < R && y + dy[i] >= 0 && y + dy[i] < C) {
      x = x + dx[i]; y = y + dy[i];
      if (map[x][y] == '#') break;
      if (map[x][y] == '-' || map[x][y] == '|' || map[x][y] == '+') {
        if (i < 2) heng = false; else shu = false;
        break;
      }
    }
  }

  if (heng && shu) map[ox][oy] = '+';
  else if (heng) map[ox][oy] = '-';
  else if (shu) map[ox][oy] = '|';
  else map[ox][oy] = 'X';
}

void apply(int ox, int oy, int startd) {
  for (int i = startd; i < startd + 2; i++) {
    int x = ox, y = oy;
    while (x + dx[i] >= 0 && x + dx[i] < R && y + dy[i] >= 0 && y + dy[i] < C) {
      x = x + dx[i]; y = y + dy[i];
      if (map[x][y] == '#') break;
      if (map[x][y] == '.') cnt[x][y] ++;
    }
  }
}

bool reverse(int ox, int oy) {
  for (int i = 0; i < 4; i++) {
    int x = ox, y = oy;
    while (x + dx[i] >= 0 && x + dx[i] < R && y + dy[i] >= 0 && y + dy[i] < C) {
      x = x + dx[i]; y = y + dy[i];
      if (map[x][y] == '+') {
        if (i < 2) map[x][y] = '-';
        else map[x][y] = '|';
        return true;
      }
      if (map[x][y] != '.') break;
    }
  }
  return false;
}

int main()
{
  int numTests;
  cin >> numTests;
  for (int test = 1; test <= numTests; test++) {
    cin >> R >> C;
    string str;
    for (int i = 0; i < R; i++) {
      cin >> str;
      for (int j = 0; j < C; j++) {
        map[i][j] = str[j];
        if (map[i][j] == '|' or map[i][j] == '-') map[i][j] = '+';
      }
    }

    bool okay = true;
    for (int i = 0; i < R; i++) {
      for (int j = 0; j < C; j++) if (map[i][j] == '+') {
        place(i, j);
        if (map[i][j] == 'X') okay = false;
      }
    }

    bool changed = true;
    while (okay) {
      //for (int i = 0; i < R; i++) {
      //  for (int j = 0; j < C; j++) cout << map[i][j];
      //  cout << endl;
      //}
      //cout << endl;

      bool changed = false;
      for (int i = 0; i < R; i++)
        for (int j = 0; j < C; j++) cnt[i][j] = 0;
      for (int i = 0; i < R; i++)
        for (int j = 0; j < C; j++) {
          if (map[i][j] == '+' || map[i][j] == '|') apply(i, j, 2);
          if (map[i][j] == '+' || map[i][j] == '-') apply(i, j, 0);
        }
      for (int i = 0; i < R; i++)
        for (int j = 0; j < C; j++) {
          if (map[i][j] == '.' && cnt[i][j] == 0) okay = false;
          if (map[i][j] == '.' && cnt[i][j] == 1) {
            bool ret = reverse(i, j);
            //cout << "ret = " << ret << endl;
            if (ret) changed = true;
          }
        }

      if (!changed) {
        for (int i = 0; i < R; i++) if (!changed) {
          for (int j = 0; j < C; j++) if (map[i][j] == '+') {
            map[i][j] = '-'; changed = true; break;
          }
        }
      }
      if (!changed) break;
    }

    if (!okay) cout << "Case #" << test << ": IMPOSSIBLE" << endl;
    else {
      cout << "Case #" << test << ": POSSIBLE" << endl;
      for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) cout << map[i][j];
        cout << endl;
      }
    }
  }
}
