#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ll> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;

#define INF 1e9
#define FOR(i, a, b) for(int i=int(a); i<int(b); i++)
#define FORC(cont, it) for(decltype((cont).begin()) it = (cont).begin(); it != (cont).end(); it++)
#define pb push_back

vvi board;
int r, c;
int neigh[3][2] = {{-1, 0}, {0, -1}, {1, 0}};

int getCode(char ch) {
  switch(ch) {
    case '?':
      return 0;
    default:
      return ch - 'A' + 1;
  };
}

void spread(int i, int j) {
  int z = board[i][j];
  board[i][j] = 0;
  for (int x = i; x >= 0; x--)
    if (board[x][j] == 0) {
      for (int y = j; y >= 0; y--)
        if (board[x][y] == 0)
          board[x][y] = z;
        else
          break;
    } else {
      break;
    }

  for (int x = i + 1; x < r; x++)
    if (board[x][j] == 0) {
      for (int y = j; y >= 0; y--)
        if (board[x][y] == 0)
          board[x][y] = z;
        else
          break;
    } else {
      break;
    }
}

void solve() {
  FOR(j, 0, c)
    FOR(i, 0, r)
      if (board[i][j] != 0)
        spread(i, j);
}

void fix() {
  FOR(i, 0, r)
    FOR(j, 1, c)
      if (board[i][j] == 0)
        board[i][j] = board[i][j-1];
}

void printBoard() {
  FOR(i, 0, r) {
    FOR(j, 0, c)
      cout << (char)(board[i][j] - 1 + 'A');
    cout << endl;
  }
}

int main() {
  ios::sync_with_stdio(false);
  int t;
  cin >> t;
  FOR(tc, 1, t+1) {
    char ch;
    cin >> r >> c;
    board = vvi(r, vi(c));
    FOR(i, 0, r) {
      FOR(j, 0, c) {
        cin >> ch;
        board[i][j] = getCode(ch);
      }
    }
    solve();
    fix();
    cout << "Case #" << tc << ": " << endl;
    printBoard();
  }
}
