#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <string>
#include <stack>
#include <queue>
using namespace std;

string board[25][25];
bool logic[25];

int main() {
  int TC;
  scanf("%d", &TC);
  for(int t = 1; t <= TC; ++t) {
    int R, C;
    scanf("%d %d", &R, &C);
    string sentence;
    bool test;
    for(int i = 0; i < R; ++i) {
      test = false;
      cin >> sentence;
      for(int j = 0; j < C; ++j) {
        board[i][j] = sentence.substr(j, 1);
        if(board[i][j] != "?") {
          test = true;
        }
      }
      logic[i] = test;
    }

    for(int i = 0; i < R; ++i) {
      if(logic[i]) {
        int first = 0;
        for(int j = 0; j < C; ++j) {
          if(board[i][j] != "?") {
            first = j;
            break;
          }
        }

        for(int j = 0; j < first; ++j) {
          board[i][j] = board[i][first];
        }

        string cur = board[i][first];
        for(int j = first; j < C; ++j) {
          if(board[i][j] == "?") {
            board[i][j] = cur;
          } else {
            cur = board[i][j];
          }
        }
      }
    }

    int first_row = 0;
    for(int i = 0; i < R; ++i) {
      if(logic[i]) {
        first_row = i;
        break;
      }
    }

    for(int i = 0; i < first_row; ++i) {
      for(int j = 0; j < C; ++j) {
        board[i][j] = board[first_row][j];
      }
    }

    int cur_row = first_row;
    for(int i = first_row; i < R; ++i) {
      if(logic[i]) {
        cur_row = i;
      } else {
        for(int j = 0; j < C; ++j) {
          board[i][j] = board[cur_row][j];
        }
      }
    }

    printf("Case #%d:\n", t);
    for(int i = 0; i < R; ++i) {
      for(int j = 0; j < C; ++j) {
        cout << board[i][j];
      }
      cout << endl;
    }
  }
}