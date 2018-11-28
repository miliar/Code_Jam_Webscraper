/**
 * jerry
 * A.cpp
 */

#include <assert.h>
#include <ctype.h>
#include <limits.h>
#include <math.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#include <algorithm>
#include <array>
#include <bitset>
#include <chrono>
#include <complex>
#include <deque>
#include <forward_list>
#include <fstream>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <memory>
#include <numeric>
#include <queue>
#include <random>
#include <regex>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;

typedef long long int lli;
typedef pair<int, int> pii;
typedef pair<int, lli> pil;
typedef pair<lli, int> pli;
typedef pair<lli, lli> pll;

int gInt () {
  int i;
  scanf("%d", &i);
  return i;
}

lli gLong () {
  lli i;
  scanf("%lld", &i);
  return i;
}

double gDouble () {
  double i;
  scanf("%lf", &i);
  return i;
}

void quit () {
  fflush(stdout);
  exit(0);
}

int r, c;
char grid[30][30];
char line[30];

bool hasletter(char* buf) {
  int l = strlen(buf);
  for (int i = 0; i < l; ++i) {
    if (buf[i] != '?') {
      return true;
    }
  }
  return false;
}

void fill(char* buf) {
  int l = strlen(buf);
  char c = '?';
  for (int i = 0; i < l; ++i) {
    if (buf[i] != '?') {
      c = buf[i];
      break;
    }
  }
  for (int i = 0; i < l; ++i) {
    if (buf[i] != '?') {
      c = buf[i];
    }
    buf[i] = c;
  }
}

void solve(int nC) {
  r = gInt();
  c = gInt();
  bool hasfirst = false;
  for (int i = 0; i < r; ++i) {
    scanf("%s", grid[i]);
    if (hasletter(grid[i]) && !hasfirst) {
      strcpy(line, grid[i]);
      fill(line);
      hasfirst = true;
    }
  }
  printf("Case #%d:\n", nC);
  for (int i = 0; i < r; ++i) {
    if (hasletter(grid[i])) {
      strcpy(line, grid[i]);
      fill(line);
    }
    printf("%s\n", line);
  }
}

int main (int argc, char ** argv) {
  int t = gInt();
  for (int i = 0; i < t; ++i) {
    solve(i + 1);
  }
  quit();
}
