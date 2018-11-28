#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <string.h>
#include <math.h>

int min2(int A, int B){
  if( A < B )
    return A;
  return B;
}

int min3(int A, int B, int C){
  if( (A < B) && (A < C) )
    return A;
  if( B < C )
    return B;
  return C;
}

int main(int argc, char *argv[]){
  FILE* filein;
  FILE* fileout;
  int T, t;
  int i;
  int N, P, PP[4], tmp, min, res;


  if( argc < 3 ){
    printf("Usage is: task1 filein fileout\n");
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
    for( i = 0; i < 4; i ++ ){
      PP[i] = 0;
    }
    printf("-------------\t=%d\n", t);
    fscanf(filein, "%d %d\n", &N, &P);
    printf("%d %d\n", N, P);
    for( i = 0; i < N; i ++ ){
      fscanf(filein, "%d", &tmp);
      printf("%d ", tmp);
      PP[tmp%P] ++;
    }
    fscanf(filein, "\n");
    printf("\n");

    // Solve & Output
    res = 0;
    if( P == 2 ){
      res += PP[0];
      if( PP[1] % 2 != 0 ){
        res += PP[1] / 2 + 1;
      }
      else{
        res += PP[1] / 2;
      }
    }
    if( P == 3 ){
      res += PP[0];
      min = min2(PP[1], PP[2]);
      res += min;
      PP[1] -= min;
      PP[2] -= min;
      res += PP[1] / 3;
      res += PP[2] / 3;
      if( (PP[1] % 3 != 0) || (PP[2] % 3 != 0 ) ){
        res ++;
      }
    }
    if( P == 4 ){
      res += PP[0];
      res += PP[2] / 2;
      PP[2] = PP[2] % 2;
      min = min2(PP[1], PP[3]);
      res += min;
      PP[1] -= min;
      PP[3] -= min;
      if( (PP[1] >= 2) && (PP[2] == 1) ){
        res ++;
        PP[1] -= 2;
        PP[2] -= 1;
      }
      if( (PP[3] >= 2) && (PP[2] == 1) ){
        res ++;
        PP[3] -= 2;
        PP[2] -= 1;
      }
      res += PP[1] / 4;
      res += PP[3] / 4;
      if( (PP[1] % 4 != 0) || (PP[3] % 4 != 0 ) || (PP[2] > 0)){
        res ++;
      }
    }

    fprintf(fileout, "Case #%d: %I64d\n", t + 1, res);
  }

  fclose(fileout);
  fclose(filein);

  return 0;
}
