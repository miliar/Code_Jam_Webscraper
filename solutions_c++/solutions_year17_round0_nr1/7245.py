#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;

int N, K;
char inp[1000 + 10];

int calc() {
   int rs = 0;
   for(int i = 0; i < N; i++) {
      if(inp[i] == '-') {
         if(i+K > N) return INF;
         for(int j = i; j < i+K; j++) {
            if(inp[j] == '-') inp[j] = '+';
            else inp[j] = '-';
         }
         rs++;
      }
   }
   return rs;
}

int main() {
   int T; scanf("%d", &T);
   for(int cs = 1; cs <= T; cs++) {
      scanf("%s%d", inp, &K); N = strlen(inp);
      printf("Case #%d: ", cs);
      int rs = calc();
      if(rs == INF) printf("IMPOSSIBLE\n");
      else printf("%d\n", rs);
   }
}
