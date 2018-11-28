#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <vector>
#include <cstring>

using namespace std;

#define LEN 1024
char S[LEN];
int K, len;

int solve(int i){
  if (i == len) return 0;
  if (S[i] == '+') return solve(i+1);
  if (i+K > len) return -1;

  for(int k = 0; k < K; k++)
    S[i+k] = (S[i+k] == '+') ? '-' : '+';

  int r = solve(i+1);
  return (r < 0) ? r : r+1;
}

int main() {
  int T;

  scanf("%d", &T);
  for(int caso = 1; caso <= T; caso++) {
    scanf("%s %d", S, &K);

    len = strlen(S);
    int r = solve(0);

    printf("Case #%d: ", caso);
    if (r < 0) printf("IMPOSSIBLE\n");
    else printf("%d\n", r);

  }
  return 0;
}

