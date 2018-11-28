#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <string.h>
#include <math.h>

char S[1001];

int main(int argc, char *argv[]){
  FILE* filein;
  FILE* fileout;
  int T;
  int K, len, res, t, i, j;

  if( argc < 3 ){
    printf("Usage is: TaskA filein fileout\n");
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
    fscanf(filein, "%s %d\n", S, &K);
    printf("%s %d\n", S, K);

    len = strlen(S);
    res = 0;
    for( i = 0; i <= len - K; i ++ ){
      if( S[i] == '-' ){
        for( j = 0; j < K; j ++ ){
          S[i+j] = S[i+j] == '-' ? '+' : '-';
        }
        res ++;
      }
    }
    for( ; i < len; i ++ ){
      if( S[i] == '-' ){
        res = -1;
      }
    }

    // Output
    if( res == -1 ){
      fprintf(fileout, "Case #%d: IMPOSSIBLE\n", t + 1);
    }
    else{
      fprintf(fileout, "Case #%d: %d\n", t + 1, res);
    }
  }

  fclose(fileout);
  fclose(filein);

  return 0;
}
