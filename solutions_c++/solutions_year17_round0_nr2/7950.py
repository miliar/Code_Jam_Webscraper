#include <bits/stdc++.h>

using namespace std;

const int N = 25;

int n;
char s[N];
int memo[N][10][2];

bool solve(int i, int d, bool ok) { 
  if (i == n) {
    return ok;
  } else {
    int& res = memo[i][d][ok];
    if (res == -1) {
      res = 0;
      if (ok) {
        res |= solve(i + 1, 9, ok);
      } else {
        for (int j = d; j <= s[i] - '0'; j++) {
          res |= solve(i + 1, j, j < s[i] - '0');
        }
      }
    }
    return res;
  }
}

void print(int i, int d, bool ok) {
  if (i < n) {
    if (ok) {
      printf("9");
      print(i + 1, d, ok);
    } else {
      for (int j = s[i] - '0'; j >= d; j--) {
        if (solve(i + 1, j, j < s[i] - '0')) {
          printf("%d", j);
          print(i + 1, j, j < s[i] - '0');
          break;
        }  
      }
    }
  } 
}

int main() {
  int t;
  scanf("%d", &t);
  for (int tc = 1; tc <= t; tc++) {
    scanf("%s", s);
    n = strlen(s);
    memset(memo, -1, sizeof memo);
    printf("Case #%d: ", tc);
    if (is_sorted(s, s + n)) {
      printf("%s\n", s);
    } else {
      for (int i = s[0] - '0'; i >= 0; i--) {
        if (solve(1, i, i < s[0] - '0')) {
          if (i) {
            printf("%d", i);
          } 
          print(1, i, i < s[0] - '0');
          printf("\n");
          break;
        }
      }
    }
  }
  return 0; 
}