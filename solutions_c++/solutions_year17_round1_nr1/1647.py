#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>

int main() {
  int n_cases;
  scanf("%d\n", &n_cases);
  for (int i = 0; i < n_cases; i++) {
    int row, col;
    scanf("%d %d\n", &row, &col);
    char cake[25][25];
    for (int j = 0; j < row; j++) {
      for (int k = 0; k < col; k++) {
        scanf("%c", &cake[j][k]);
      }
      scanf("\n");
    }
    // Solve
    for (int j = 0; j < row; j++) {
      for (int k = 0; k < col; k++) {
        // for every position
        if (cake[j][k] == '?') continue;
        // upward
        for (int u = j - 1; u >= 0; u--) {
          if (cake[u][k] != '?') break;
          cake[u][k] = cake[j][k];
        }
        // downward
        for (int u = j + 1; u < row; u++) {
          if (cake[u][k] != '?') break;
          cake[u][k] = cake[j][k];
        }        
      }
    }
    for (int j = 0; j < row; j++) {
      for (int k = 0; k < col; k++) {      
        // upward
        for (int u = k - 1; u >= 0; u--) {
          if (cake[j][u] != '?') break;
          cake[j][u] = cake[j][k];
        }
        // downward
        for (int u = k + 1; u < col; u++) {
          if (cake[j][u] != '?') break;
          cake[j][u] = cake[j][k];
        }
      }
    }
    printf("Case #%d:\n", i + 1);
    for (int j = 0; j < row; j++) {
      for (int k = 0; k < col; k++) {
        printf("%c", cake[j][k]);
      }
      printf("\n");
    }
  }    
  return 0;
} 