#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <vector>
#include <cstring>

using namespace std;

#define MAX 1000100
char S[MAX];
int LS[MAX], RS[MAX];

int main() {
  int T;

  scanf("%d", &T);
  for(int caso = 1; caso <= T; caso++) {
    int N, K;
    scanf("%d %d", &N, &K);

    memset(S, 0, sizeof(S));
    S[0] = S[N+1] = 1;

    for(int i = 1; i <= N; i++){
      LS[i] = i-1;
      RS[i] = N-i;
    }

    int best;
    for(int i = 0; i < K; i++){
      best = -1;
      for(int j = 1; j <= N; j++){
        if (!S[j]){
          if (best < 0) best = j;
          else if (min(LS[j], RS[j]) > min(LS[best], RS[best])) best = j;
          else if (min(LS[j], RS[j]) == min(LS[best], RS[best]) && max(LS[j], RS[j]) >  max(LS[best], RS[best])) best = j;
        }
      }
      S[best] = 1;
      for(int j = best+1; j <= N; j++){
        if (S[j]) break;
        LS[j] = j-(best+1);
      }
      for(int j = best-1; j >= 0; j--){
        if (S[j]) break;
        RS[j] = best-1-j;
      }
    }

    printf("Case #%d: %d %d\n", caso, max(LS[best], RS[best]), min(LS[best], RS[best]));
  }
  return 0;
}

