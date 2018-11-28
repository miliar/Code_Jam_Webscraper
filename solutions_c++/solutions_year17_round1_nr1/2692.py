#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<ll, ll>;

int R, C;
char grid[30][30];

bool test(int i1, int j1, int i2, int j2, char ch) {
  int flag = 0;
  for (int r = i1; r <= i2; ++r) {
    for (int c = j1; c <= j2; ++c) {
      if (grid[r][c] == ch) flag = 1;
      if (!(grid[r][c] == ch || grid[r][c] == '?')) return false;
    }
  }
  return flag == 1;
}

void fill(int i1, int j1, int i2, int j2, char ch) {
  for (int r = i1; r <= i2; ++r) {
    for (int c = j1; c <= j2; ++c) {
      grid[r][c] = ch;
    }
  }
}

ll greedy(char ch) {
  tuple<int,int,int,int> maxr;
  ll max_area = -1;
  for (int i1 = 0; i1 < R; ++i1) {
    for (int j1 = 0; j1 < C; ++j1) {
      for (int i2 = i1; i2 < R; ++i2) {
	for (int j2 = j1; j2 < C; ++j2) {
	  //printf("%c %d %d %d %d\n", ch, i1,j1,i2,j2);
	  if (!test(i1,j1,i2,j2,ch)) continue;
	  ll area = (abs(i1 - i2)+1)*(abs(j1 - j2)+1);
	  //printf("%lld\n", area);
	  if (area > max_area) {
	    max_area = area;
	    maxr = make_tuple(i1,j1,i2,j2);
	  }
	}
      }
    }
  }
  if (max_area >= 0) {
    int i1, j1, i2, j2; tie(i1,j1,i2,j2) = maxr;
    //printf("%d %d %d %d\n", i1,j1,i2,j2);
    fill(i1,j1,i2,j2,ch);
  }
  return max_area;
}

void solve() {
  vector<bool> visit (26);
  for (int r = 0; r < R; ++r) {
    for (int c = 0; c < C; ++c) {
      char ch = grid[r][c];
      //putchar(ch);
      if (ch != '?' && !visit[ch-'A']) {
	greedy(ch);
	visit[ch-'A'] = true;
      }
    }
  }
}

void print() {
  for (int r = 0; r < R; ++r) {
    for (int c = 0; c < C; ++c) {
      char ch = grid[r][c];
      putchar(ch);
    }
    putchar('\n');
  }
}

int main() {
  int T; cin >> T;
  for (int i = 1; i <= T; ++i) {
    cin >> R >> C;
    for (int r = 0; r < R; ++r) {
      scanf("%s", grid[r]);
    }
    //print();
    printf("Case #%d:\n", i);
    solve();
    print();
  }
  return 0;
}
