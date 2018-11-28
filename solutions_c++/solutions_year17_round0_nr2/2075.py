#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

char S[20];

int main(int argc, char *argv[]){
  FILE* filein;
  FILE* fileout;
  int T;
  int t, i, j, len, res;

  if( argc < 3 ){
    printf("Usage is: TaskB filein fileout\n");
    return 0;
  }

  // Input 

  filein = fopen(argv[1], "r");
  if( filein == NULL ){
    printf("Error open(); filein\n");
    return 0;
  }
  fileout = fopen(argv[2], "w");
  if( fileout == NULL ){
    printf("Error open(); fileout\n");
    return 0;
  }

  fscanf(filein, "%d\n", &T);
  printf("%d\n", T);
  for( t = 0; t < T; t ++ ){
    printf("-------------\t=%d\n", t);
    fscanf(filein, "%s\n", S);
    len = strlen(S);
    printf("%d %s\n", len, S);

    for( i = 0; i < len - 1; i ++ ){
      if( S[i] > S[i+1] ){
        for( j = i + 1; j < len; j ++ ){
          S[j] = '9';
        }
        S[i] = S[i] - 1;
        for( j = i - 1; j >= 0; j -- ){
          if( S[j] > S[j+1] ){
            S[j+1] = '9';
            S[j] = S[j] - 1;
          }
        }
      }
    }
    for( i = 0; i < len; i ++ ){
      if( S[i] != '0' ){
        break;
      }
    }

    // Solve & Output
    fprintf(fileout, "Case #%d: %s\n", t + 1, S + i);
  }

  fclose(fileout);
  fclose(filein);

  return 0;
}
