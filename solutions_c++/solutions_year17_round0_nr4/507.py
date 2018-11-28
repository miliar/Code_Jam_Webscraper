// CPPFLAGS=-std=c++14 -W -Wall -g -O2
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <limits>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

//#define all(c) (c).begin(),(c).end()
//#define foreach(i,c) for(auto i=(c).begin();i!=(c).end();++i)
template<class T> bool in(T e, const set<T>& s) { return s.find(e) != s.end(); }
template<class K, class V> bool in(K k, const unordered_map<K,V>& h) { return h.find(k) != h.end(); }

int n;
char board[128][128];

void parse_input() {
  int m; if (scanf("%d %d ",&n,&m)!=2) exit(2);
  int i, j, k;
  char c;
  for (i=0;i<n;++i) for (j=0;j<n;++j) board[i][j]='.';
  for (k=0;k<m;++k) {
    if (scanf("%c %d %d ",&c,&i,&j)!=3) exit(3);
    board[i-1][j-1] = c;
  }
}

map<pair<int,int>,char> moves;

void place_queen(int i, int j) {
  board[i][j] = 'o';
  moves[make_pair(i,j)] = 'o';
}

void place_rook(int i, int j) {
  if (board[i][j] == '+') place_queen(i, j);
  else {
    assert (board[i][j] == '.');
    board[i][j] = 'x';
    moves[make_pair(i,j)] = 'x';
  }
}

void place_bishop(int i, int j) {
  if (board[i][j] == 'x') place_queen(i, j);
  else {
    assert (board[i][j] == '.');
    board[i][j] = '+';
    moves[make_pair(i,j)] = '+';
  }
}

void solve() {
  int i, j;
  int score = 0;
  moves.clear();

  // place rooks (x)
  vector<bool> row(n), col(n);
  for (i=0;i<n;++i) for (j=0;j<n;++j) {
    if (board[i][j] == 'x' || board[i][j] == 'o') {
      ++score;
      row[i] = col[j] = true;
    }
  }
  j = 0;
  for (i=0;i<n;++i) if (!row[i]) {
    while (col[j]) ++j;
    ++score;
    place_rook(i,j++);
  }

  // place bishops (+)
  set<int> add, sub;
  for (i=0;i<n;++i) for (j=0;j<n;++j) {
    if (board[i][j] == '+' || board[i][j] == 'o') {
      ++score;
      add.insert(i+j);
      sub.insert(i-j);
    }
  }
  i=0;
  for (j=0;j<n;++j) if (!in(i+j,add) && !in(i-j,sub)) {
    ++score;
    place_bishop(i,j);
    add.insert(i+j);
    sub.insert(i-j);
  }
  i=n-1;
  for (j=0;j<n;++j) if (!in(i+j,add) && !in(i-j,sub)) {
    ++score;
    place_bishop(i,j);
    add.insert(i+j);
    sub.insert(i-j);
  }

  printf("%d %d\n",score,int(moves.size()));
  for (auto e : moves) {
    printf("%c %d %d\n",e.second,1+e.first.first,1+e.first.second);
  }
}

int main() {
  int tests; if (scanf("%d",&tests)!=1) return 1;
  for (int t=1;t<=tests;++t) {
    printf("Case #%d: ",t);
    parse_input();
    solve();
  }
}
