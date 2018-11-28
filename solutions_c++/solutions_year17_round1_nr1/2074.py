#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define DEBUG
#ifdef DEBUG
#define TRACE(x) cerr << #x << " = " << x << endl;
#define _ << " _ " <<
#else
#define TRACE(x) ((void)0)
#endif

char grid[28][28];
char ogrid[28][28];
int corns[256][4]; // top bottom left right
int ocorns[256][4];

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

  srand(15295);

  int T;
  cin >> T;
  for (int tt = 1; tt <= T; tt++) {
    int R, C;
    cin >> R >> C;

    set<pair<char, char>> os;

    for (int c = 'A'; c <= 'Z'; c++) {
      ocorns[c][0] = ocorns[c][2] = 100;
      ocorns[c][1] = ocorns[c][3] = -1;
    }
    for (int i = 0; i < R; i++)
      for (int j = 0; j < C; j++) {
        cin >> ogrid[i][j];
        char c = ogrid[i][j];
        if (ogrid[i][j] != '?') {
          ocorns[c][0] = min(ocorns[c][0], i);
          ocorns[c][1] = max(ocorns[c][1], i);
          ocorns[c][2] = min(ocorns[c][2], j);
          ocorns[c][3] = max(ocorns[c][3], j);
        }
      } 
    for (int c = 'A'; c <= 'Z'; c++) {
      if (ocorns[c][1] != -1) {
        for (int i = ocorns[c][0]; i <= ocorns[c][1]; i++)
          for (int j = ocorns[c][2]; j <= ocorns[c][3]; j++)
            ogrid[i][j] = c;

        for (int i = 0; i < 4; i++)
          os.emplace(c, i);
      } else
        for (int i = 0; i < 4; i++)
          corns[c][i] = -1;
    }

    while (1) {
      for (int i = 0; i < R; i++)
        for (int j = 0; j < C; j++)
          grid[i][j] = ogrid[i][j];
      for (int c = 'A'; c <= 'Z'; c++)
        if (ocorns[c][1] != -1)
          for (int i = 0; i < 4; i++)
            corns[c][i] = ocorns[c][i];
      set<pair<char, char>> s = os;

      while (!s.empty()) {
        int idx = rand() % s.size();
        char c, ty;
        tie(c, ty) = *std::next(s.begin(), idx);

        bool ok = true;
        const int xmin = corns[c][0];
        const int xmax = corns[c][1];
        const int ymin = corns[c][2];
        const int ymax = corns[c][3];
        if (ty == 0) {
          if (xmin == 0)
            ok = false;
          else {
            for (int j = ymin; j <= ymax; j++)
              if (grid[xmin - 1][j] != '?') {
                ok = false;
                break;
              }
          }
          if (ok) {
            for (int j = ymin; j <= ymax; j++)
              grid[xmin - 1][j] = c;
            corns[c][0]--;
          }
        } else if (ty == 1) {
          if (xmax == R - 1)
            ok = false;
          else {
            for (int j = ymin; j <= ymax; j++)
              if (grid[xmax + 1][j] != '?') {
                ok = false;
                break;
              }
          }
          if (ok) {
            for (int j = ymin; j <= ymax; j++)
              grid[xmax + 1][j] = c;
            corns[c][1]++;
          } 
        } else if (ty == 2) {
          if (ymin == 0)
            ok = false;
          else {
            for (int i = xmin; i <= xmax; i++)
              if (grid[i][ymin - 1] != '?') {
                ok = false;
                break;
              }
          }
          if (ok) {
            for (int i = xmin; i <= xmax; i++)
              grid[i][ymin - 1] = c;
            corns[c][2]--;
          }
        } else {
          if (ymax == C - 1)
            ok = false;
          else {
            for (int i = xmin; i <= xmax; i++)
              if (grid[i][ymax + 1] != '?') {
                ok = false;
                break;
              }
          }
          if (ok) {
            for (int i = xmin; i <= xmax; i++)
              grid[i][ymax + 1] = c;
            corns[c][3]++;
          }
        }

        if (!ok)
          s.erase(make_pair(c, ty));
      }

      for (int i = 0; i < R; i++)
        for (int j = 0; j < C; j++)
          if (grid[i][j] == '?') {
            goto tryagain;
          }
      break;
tryagain:;
    }
    cout << "Case #" << tt << ":\n";
    for (int i = 0; i < R; i++) {
      for (int j = 0; j < C; j++)
        cout << grid[i][j];
      cout << '\n';
    }
  }

  return 0;
}
