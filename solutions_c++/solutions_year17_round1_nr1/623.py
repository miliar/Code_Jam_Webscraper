#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <string.h>
#include <math.h>

int main(int argc, char *argv[]){
  FILE* filein;
  FILE* fileout;
  int T;
  int t, i, i1, j, R, C;
  char cur;
  bool f;
  char Cake[25][26];

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
    fscanf(filein, "%d %d\n", &R, &C);
    printf("%d %d\n", R, C);
    for( i = 0; i < R; i++ ){
      fscanf(filein, "%s\n", Cake[i]);
      printf("%s\n", Cake[i]);
    }
    // Solve & Output
    for( i = 0; i < R; i++ ){
      f = false;
      for( j = 0; j < C; j ++ ){
        if( Cake[i][j] != '?' ){
          f = true;
          cur = Cake[i][j];
          break;
        }
      }
      if( f ){
        break;
      }
    }
    for( j = 0; j < C; j ++ ){
      if( Cake[i][j] != '?' ){
        cur = Cake[i][j];
      }
      else{
        Cake[i][j] = cur;
      }
    }
    for( i1 = i - 1; i1 >= 0; i1 -- ){
      for( j = 0; j < C; j ++ ){
        Cake[i1][j] = Cake[i1+1][j];
      }
    }
    for( i = i + 1; i < R; i++ ){
      f = false;
      for( j = 0; j < C; j ++ ){
        if( Cake[i][j] != '?' ){
          f = true;
          cur = Cake[i][j];
          break;
        }
      }
      if( f ){
        for( j = 0; j < C; j ++ ){
          if( Cake[i][j] != '?' ){
            cur = Cake[i][j];
          }
          else{
            Cake[i][j] = cur;
          }
        }
      }
      else{
        for( j = 0; j < C; j ++ ){
          Cake[i][j] = Cake[i-1][j];
        }
      }
    }

    fprintf(fileout, "Case #%d:\n", t + 1);
    for( i = 0; i < R; i ++ ){
      fprintf(fileout, "%s\n", Cake[i]);
    }
  }

  fclose(fileout);
  fclose(filein);

  return 0;
}
