#include <stdio.h>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstdlib>
#include <cmath>
#include <string.h>
#include <memory.h>
#include <algorithm>
#include <iomanip>
#include <string>
#include <bitset>

#define F first
#define S second;
#define MP make_pair

typedef long long ll;

using namespace std;

int const PI = acos(-1);
int dx[] = { 0, 1, 1, 1, 0, -1, -1, -1 };
int dy[] = { 1, 1, 0, -1, -1, -1, 0, 1 };

long long gcd(long long a, long long b) {
	return b == 0 ? a : gcd(b, a % b);
}

long long lcm(long long a, long long b) {
	return a * (b / gcd(a, b));
}

char grid[26][26];

int main() {
  freopen("in.in", "r", stdin);
  freopen("out.out", "w", stdout);

  int t;
  scanf("%d", &t);

  int n, m;
  for(int c = 1; t--; c++) {
    scanf("%d%d", &n, &m);

    for(int i = 0; i < n; i++)
      scanf("%s", grid[i]);

    for(int i = 0; i < n; i++)
      for(int j = 0; j < m; j++)
        if(i < n - 1 && grid[i][j] != '?') {
          int k = i + 1;
          while(k < n && grid[k][j] == '?') {
            grid[k][j] = grid[i][j];
            k++;
          }
        }

    for(int i = n - 1; i >= 0; i--)
      for(int j = 0; j < m; j++)
        if(i && grid[i][j] != '?') {
          int k = i - 1;
          while(k >= 0 && grid[k][j] == '?') {
            grid[k][j] = grid[i][j];
            k--;
          }
        }

    for(int i = 0; i < n; i++)
      for(int j = 0; j < m; j++)
        if(j < m - 1 && grid[i][j] != '?') {
          int k = j + 1;
          while(k < m && grid[i][k] == '?') {
            grid[i][k] = grid[i][j];
            k++;
          }
        }

    for(int i = 0; i < n; i++)
      for(int j = m - 1; j >= 0; j--)
        if(j && grid[i][j] != '?') {
          int k = j - 1;
          while(k >= 0 && grid[i][k] == '?') {
            grid[i][k] = grid[i][j];
            k--;
          }
        }

    printf("Case #%d:\n", c);
    for(int i = 0; i < n; i++)
      printf("%s\n", grid[i]);
  }

  return 0;
}
