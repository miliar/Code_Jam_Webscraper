#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int compare( const void *arg1, const void *arg2 )
{
  if( *(int*)arg1 < *(int*)arg2 )
    return -1;
  if( *(int*)arg1 > *(int*)arg2 )
    return 1;
  return 0;
}

int N, P, R[50], Q[50][50];
int maxmax[50][50], minmin[50][50];
int ii[50];

int main(int argc, char *argv[]){
  FILE* filein;
  FILE* fileout;
  int T;
  int t, i, j;
  int res, minmax, mmindex, curmin, curmax, nummin, nummax;
  bool flag;

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
    fscanf(filein, "%d %d\n", &N, &P);
    printf("%d %d\n", N, P);
	  for( i = 0; i < N - 1; i ++ ){
      fscanf(filein, "%d ", R+i);
      printf("%d ", R[i]);
	  }
    fscanf(filein, "%d\n", R+i);
    printf("%d\n", R[i]);
	  for( i = 0; i < N; i ++ ){
      for( j = 0; j < P - 1; j ++ ){
        fscanf(filein, "%d ", &(Q[i][j]));
        printf("%d ", Q[i][j]);
      }
      fscanf(filein, "%d\n", &(Q[i][j]));
      printf("%d\n", Q[i][j]);
	  }

    // Solve & Output
    for( i = 0; i < N; i++ ){
      qsort(Q[i], P, sizeof(int), compare);
      for( j = 0; j < P; j ++ ){
        printf("%d ", Q[i][j]);
      }
      printf("\n");
    }

    for( i = 0; i < N; i ++ ){
      for( j = 0; j < P; j ++ ){
        minmin[i][j] = 10 * Q[i][j] / (11 * R[i]);
        if ( minmin[i][j] * 11 * R[i] < 10 * Q[i][j] ){
          minmin[i][j] ++;
        }
        maxmax[i][j] = 10 * Q[i][j] / (9 * R[i]);
      }
    }
    for( i = 0; i < N; i ++ ){
      for( j = 0; j < P; j ++ ){
        printf("%d-%d ", minmin[i][j], maxmax[i][j]);
      }
      printf("\n");
    }

    for( i = 0; i < N; i++ ){
      ii[i] = 0;
    }
    res = 0;
    flag = true;
    while( flag ){
      minmax = maxmax[0][ii[0]];
      mmindex = 0;
      for( i = 1; i < N; i ++ ){
        if( maxmax[i][ii[i]] < minmax ){
          minmax = maxmax[i][ii[i]];
          mmindex = i;
        }
      }
      for( i = 0; i < N; i ++ ){
        if( minmin[i][ii[i]] > minmax ){
          break;
        }
      }
      if( i == N ){
        res ++;
        for( j = 0; j < N; j ++ ){
          ii[j] ++;
          if( ii[j] == P ){
            flag = false;
          }
        }
      }
      else{
        ii[mmindex] ++;
        if( ii[mmindex] == P ){
          flag = false;
        }
      }
    }
    
    fprintf(fileout, "Case #%d: %d\n", t + 1, res);
  }

  fclose(fileout);
  fclose(filein);

  return 0;
}
