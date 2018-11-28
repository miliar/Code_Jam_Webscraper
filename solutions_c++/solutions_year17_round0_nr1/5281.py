#include <stdio.h>
#include <queue>

using namespace std;

const int MAXN = 1005;

char str[MAXN];
int N, K, T, test = 1, res, A[MAXN];

int main(){
#ifdef DEBUG
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif
  scanf("%d", &T);
  while(T--){
    scanf("%s %d", str, &K);
    N = strlen(str), res = 0;
    for(int i=0; i<N; ++i) A[i] = (str[i] == '+');
    queue<int> moves;
    for(int i=0; i<N; ++i){
      if(!moves.empty() && moves.front() <= i - K) moves.pop();
      if(!((moves.size() & 1) ^ A[i])){
        if(i > N - K){ res = -1; break; }
        res++;
        moves.push(i);
      }
    }
    printf("Case #%d: ", test++);
    if(res != -1) printf("%d\n", res);
    else puts("IMPOSSIBLE");
  }
  return 0;
}