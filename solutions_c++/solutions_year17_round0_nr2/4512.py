//
//  b.cpp
//  GCJ
//
//  Created by 방성원 on 2017. 4. 9..
//  Copyright © 2017년 makesource. All rights reserved.
//

#include <stdio.h>
#include <string.h>
#define maxf(a,b) ((a)>(b)?(a):(b))

void output (int test,char *s) {
  int N = (int) strlen(s+1);
  int start = 1;
  for (int i=1;i<=N;i++) {
    if (s[i] != '0') {
      start = i;
      break;
    }
  }
  printf ("Case #%d: %s\n", test, s+start);
}

int main() {
  int T;
  scanf ("%d",&T);
  for (int test = 1; test <= T; test ++ ) {
    char S[99], D[99];
    scanf ("\n%s",S+1);
    int N = (int) strlen(S+1);
    D[1] = S[1];
    for (int i=2;i<=N;i++) D[i] = maxf(D[i-1], S[i]);
    int pos = -1;
    for (int i=2;i<=N;i++) {
      if (D[i] != S[i]) { pos = i; break; }
    }
    if (pos == -1) {
      output(test, S);
      continue;
    }
    for (int i = pos - 1;i >= 1;i --) {
      if (S[i] != '0' && D[i-1] <= S[i] - 1) {
        S[i] = S[i] - 1;
        for (int j = i + 1;j <= N;j ++) S[j] = '9';
        break;
      }
    }
    output(test, S);
  }
  return 0;
}
