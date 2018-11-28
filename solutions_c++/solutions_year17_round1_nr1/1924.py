// Author: Krzysztof Bochenek
// Email:  kpbochenek@gmail.com
// --------------------------------
#include <stdio.h>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <math.h>
#include <algorithm>
#include <string>
#include <iostream>

typedef long long int ll;
typedef unsigned long long ull;

using namespace std;

string A[25];

int T, R, C;

void expand(int r, int c) {
  if (A[r][c] != '?') {
    int i=r-1;
    while (i >= 0 && A[i][c] == '?') {
      A[i][c] = A[r][c];
      i--;
    }
    i = r+1;
    while (i < R && A[i][c] == '?') {
      A[i][c] = A[r][c];
      i++;
    }
  }
}

void find(int r, int c) {
  if (A[r][c] != '?') return;

  int i=c-1;
  while (i >= 0) {
    if (A[r][i] != '?') {
      A[r][c] = A[r][i];
      return;
    }
    i--;
  }

  i = c+1;
  while (i < C) {
    if (A[r][i] != '?') {
      A[r][c] = A[r][i];
      return;
    }
    i++;
  }
}

int main() {

  string str;

  cin >> T;

  for (int t=0; t<T; ++t) {
    cin >> R >> C;

    for (int i=0; i<R; ++i) {
      cin >> str;
      A[i] = str;
    }

    for (int i=0; i<C; ++i) {
      for (int j=0; j<R; ++j) {
	expand(j, i);
      }
    }
    
    for (int i=0; i<C; ++i) {
      for (int j=0; j<R; ++j) {
	find(j, i);
      }
    }




    cout << "Case #" << t+1 << ":" << endl;
    for (int i=0; i<R; ++i) {
      cout << A[i] << endl;
    }
  }
  
  return 0;
}
