//
//  main.cpp
//  GCJ
//
//  Created by 방성원 on 2017. 4. 9..
//  Copyright © 2017년 makesource. All rights reserved.
//

#include <stdio.h>
#include <string.h>
int main() {
  int T;
  scanf ("%d",&T);
  for (int test = 1; test <= T; test ++ ) {
    int K; char S[1010];
    scanf ("\n%s %d",S+1, &K);
    int N = (int) strlen(S+1);
    bool cake[1010];
    for (int i=1;i<=N;i++) cake[i] = S[i] == '+';
    int ans = 0;
    for (int i=1;i<=N-K+1;i++) {
      if (!cake[i]) {
        for (int j=i;j<=i+K-1;j++) cake[j] = !cake[j];
        ans ++;
      }
    }
    bool impossible = false;
    for (int i=N-K+2;i<=N;i++) {
      if (!cake[i]) impossible = 1;
    }
    if (impossible) {
      printf ("Case #%d: IMPOSSIBLE\n",test);
    } else {
      printf ("Case #%d: %d\n",test,ans);
    }
  }
  return 0;
}
