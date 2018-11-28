#include <algorithm>
#include <bitset>
#include <cassert>
#include <cfloat>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <memory>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

// c++11
#include <array>
#include <tuple>
#include <unordered_map>
#include <unordered_set>

#define mp make_pair
#define mt make_tuple
#define rep(i, n) for (int i = 0; i < (n); i++)

using namespace std;

using ll = long long;
using ull = unsigned long long;
using pii = pair<int, int>;

const int INF = 1 << 29;
const double EPS = 1e-9;
const ll MOD = 1000000007;

const int dx[] = {1, 0, -1, 0}, dy[] = {0, -1, 0, 1};


void fill_color(int y, int x, int ty, int tx, vector<string> &board, char c){
    for (int i = y; i <= ty; i++){
      for (int j = x; j <= tx; j++){
        if (board[i][j] != '?')return ;
        board[i][j] = c;
      }
    }
}

void output(const vector<string> &board){
  for (int i = 0; i <board.size(); i++){
    cout << board[i] << endl;
  }
}

char check_vertical(int y, int x, vector<string> &board){
  for (int i = y - 1; i >= 0; i--){
    if (board[i][x] != '?'){
      return board[i][x];
    }
  }
  //right
  for (int i = y + 1; i < board.size(); i++){
    if (board[i][x] != '?'){
      return board[i][x];
    }
  }
  return '?';
}
char check_horizontal(int y, int x, vector<string> &board){
  //left
  for (int i = x - 1; i >= 0; i--){
    if (board[y][i] != '?'){
      return board[y][i];
    }
  }
  for (int i = x + 1; i < board[0].size(); i++){
    if (board[y][i] != '?'){
      return board[y][i];
    }
  }
  return '?';
}
void solve(const int test_case){
  int R,C;
  cin >> R >> C;
  vector<string> board;
  for (int i = 0; i < R; i++){
    string tmp;
    cin >> tmp;
    board.push_back(tmp);
  }
  set<char> colors;
  for (char i = 'A'; i <= 'Z'; i++){
    colors.emplace(i);
  }
  for (int i = 0; i < R; i++){
    for (int j = 0; j < C; j++){
      if (board[i][j] != '?'){
        colors.erase(board[i][j]);
      }
    }
  }

  auto check = [&](){
    for (int i = 0; i < R; i++){
      for (int j = 0; j < C; j++){
        if (board[i][j] == '?'){
          char res;
          //vertical
          res = check_horizontal(i,j, board);
          if (res != '?'){
            fill_color(i, j, i, C - 1, board, res);
            continue;
          }
          //horiznotal
        }
      }
    }
  };
  auto check1 = [&](){
    for (int i = 0; i < R; i++){
      for (int j = 0; j < C; j++){
        if (board[i][j] == '?'){
          char res;
          //vertical
          res = check_vertical(i,j, board);
          if (res != '?'){
            fill_color(i, j, R - 1, j, board, res);
            continue;
          }
          //horiznotal
        }
      }
    }
  };
  check();
  check1();

  cout << "Case #" << test_case << ":" << endl;
  output(board);
}
int main() {
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++){
    solve(i);
  }
  return 0;
}
