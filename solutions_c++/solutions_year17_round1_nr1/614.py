#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int m, n;
char A[128][128];

int main() {
  int T;
  scanf("%d", &T);
  for (int t = 0 ; t < T; t++) {     
     scanf("%d %d", &m, &n);
     for (int i = 0 ;i < m; i++) {
       scanf("%s", A[i]);
     }
     for (int i = 0; i < m; i++) {
       for (int j = 0; j < n -1; j ++) 
         if (A[i][j] != '?' && A[i][j+1] == '?') {
            A[i][j+1] = A[i][j];
         } 
       for (int j = n-1 ; j > 0 ; j --) 
         if (A[i][j] != '?' && A[i][j-1] == '?') {
            A[i][j-1] = A[i][j];
         } 
     }
     for (int i = 1; i < m; i++) {
       if (A[i][0]=='?' && A[i-1][0]!= '?') {
         for (int j = 0; j < n; j ++) A[i][j] = A[i-1][j];
       }
     }
     for (int i = m-2; i >= 0; i--) {
       if (A[i][0]=='?' && A[i+1][0] != '?') {
         for (int j = 0; j < n; j ++) A[i][j] = A[i+1][j];
       }
     }
     printf("Case #%d:\n", t + 1);
     for (int i = 0 ; i < m; i++) {
       printf("%s\n", A[i]);
     }
  }
}
