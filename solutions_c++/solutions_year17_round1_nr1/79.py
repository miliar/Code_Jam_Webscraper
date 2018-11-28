/*
  by Nazarbek Altybay
  nazarbek.altybay@gmail.com
*/

#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <cassert>
#include <iomanip>
#include <iostream>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>

#define f first
#define s second

#define pb push_back
#define mp make_pair

using namespace std;

const int N = (int) 30 + 7;
const int MOD = (int) 1e9 + 7;

int n, m;
char a[N][N];
bool row[N];

void solve() {
  cin >> n >> m;
  for (int i = 1; i <= n; i++) {
    row[i] = 0;
    for (int j = 1; j <= m; j++) {
      cin >> a[i][j];
      if (a[i][j] != '?')
        row[i] = 1;
    }
  }
  for (int i = 1; i <= n; i++) {
    int pos = i;
    while (pos > 0 && !row[pos]) pos--;
    if (!pos) {
      pos = i;
      while (pos <= n && !row[pos])
        pos++;
    }
    for (int j = 1; j <= m; j++)
      a[i][j] = a[pos][j];
  }
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= m; j++) {
      if (a[i][j] == '?') {
        int pos = j;
        while (pos > 0 && a[i][pos] == '?') --pos;
        if (!pos) {
          pos = j;
          while (pos <= m && a[i][pos] == '?') ++pos;
        }
        a[i][j] = a[i][pos];
      }
      cout << a[i][j];
    }
    cout << endl;
  }
}

int main() {
  #ifdef LOCAL
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  #endif

  int t;
  scanf("%d", &t);
  for (int cases = 1; cases <= t; cases++) {
    printf("Case #%d:\n", cases);
    //prepare();
    solve();
  }

  return 0;
}