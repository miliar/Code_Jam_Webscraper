#include <stdio.h>
#include <algorithm>

using namespace std;

const int MAXN = 1005;

int Lpos[MAXN], Rpos[MAXN], A[MAXN], N, K, T, test = 1;

int main(){
#ifdef DEBUG
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif
  scanf("%d", &T);
  while(T--){
    scanf("%d %d", &N, &K);
    for(int i=1; i<=N; ++i) A[i] = 0, Lpos[i] = 0, Rpos[i] = N + 1;
    A[0] = A[N + 1] = 1;
    int lm = -1, rm = -1, pos = -1;
    for(int r=1; r<=K; ++r){
      lm = -1, rm = -1, pos = -1;
      for(int i=1; i<=N; ++i){
        if(!A[i]){
          int ll = i - Lpos[i] - 1, rr = Rpos[i] - i - 1;
          if(min(ll, rr) > min(lm, rm) || (min(ll, rr) == min(lm, rm) && max(ll, rr) > max(lm, rm)))
            lm = ll, rm = rr, pos = i;
        }
      }
      A[pos] = 1;
      for(int i=pos+1; i<=N; ++i){
        if(A[i]) break;
        Lpos[i] = pos;
      }
      for(int i=pos-1; i>=1; --i){
        if(A[i]) break;
        Rpos[i] = pos;
      }
    }
    printf("Case #%d: %d %d\n", test++, max(lm, rm), min(lm, rm));
  }
  return 0;
}