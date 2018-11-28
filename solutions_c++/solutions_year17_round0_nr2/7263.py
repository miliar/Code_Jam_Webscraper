#include <cstdio>
#include <cstring>
using namespace std;

#define UNSET -999

char number[20];
long long dp[20][16][2];
int digitCount;

int max(int a, int b) {
  return a > b ? a : b;
}

long long solveRecursive(int pos, int minDigit, bool droppedDecimal) {
  if (dp[pos][minDigit][droppedDecimal] != UNSET) {
    // Memoization.
    return dp[pos][minDigit][droppedDecimal];
  }

  int current = (int) number[pos] - (int) '0';
  int limit = droppedDecimal ? 9 : current;
  if (limit < minDigit) {
    // No can't do.
    dp[pos][minDigit][droppedDecimal] = -1;
    //printf("can't do - dp[%d][%d] = -1\n", pos, minDigit);
    return -1;
  }

  long long sol = -1;
  if (pos == digitCount - 1) {
    sol = limit;
  } else {
    while (sol == -1 && limit >= minDigit) {
      //printf("Trying to sove for limit %d at pos %d\n", limit, pos);
      sol = solveRecursive(pos + 1, limit, droppedDecimal);
      if (sol == -1) {
        droppedDecimal = true;
        limit--;
      }
    }
    if (sol != -1) {
      long long factor = 1;
      long long copy = sol;
      while (copy) {
        factor *= 10;
        copy /= 10;
      }
      //printf("Got %lld as solution, prepending %lld\n", sol, limit);
      sol = limit * factor + sol;
    }
  } 
  dp[pos][minDigit][droppedDecimal] = sol;
  //printf("dp[%d][%d] = %lld\n", pos, minDigit, sol);
  return sol;
}

long long solve() {
  return solveRecursive(0, 0, false);
}

void clean() {
  for (int i = 0; i < 20; i++) {
    for (int j = 0; j < 10; j++) {
      dp[i][j][0] = UNSET;
      dp[i][j][1] = UNSET;
    }
  }
}

int main() {
  int tests;
  scanf("%d", &tests);
  for (int i = 1; i <= tests; i++) {
    scanf("%s", number);
    digitCount = strlen(number);
    clean();
    printf("Case #%d: %lld\n", i, solve());
  }
}