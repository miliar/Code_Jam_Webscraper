#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <string.h>
#include <math.h>

long long Sizes[200], Counts[200];

int main(int argc, char *argv[]){
  FILE* filein;
  FILE* fileout;
  int T;
  long long N, K;
  long long max, min;
  int t, i, cur, last;

  if( argc < 3 ){
    printf("Usage is: TaskC filein fileout\n");
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
    fscanf(filein, "%lld %lld\n", &N, &K);
    printf("%lld %lld\n", N, K);

    // Solve
    for( i = 0; i < 200; i ++ ){
      Sizes[i] = 0;
      Counts[i] = 0;
    }
    Sizes[0] = N;
    Counts[0] = 1;
    cur = 0;
    last = 0;
    while( K > 0 ){
      K = K - Counts[cur];
      max = Sizes[cur] / 2;
      min = (Sizes[cur] - 1) / 2;
      if( Sizes[last] > max ){
        last ++;
      }
      Sizes[last] = max;
      Counts[last] += Counts[cur];
      if( max > min ){
        last ++;
      }
      Sizes[last] = min;
      Counts[last] += Counts[cur];
      cur++;
    }
    cur --;
    max = Sizes[cur] / 2;
    min = (Sizes[cur] - 1) / 2;
    //printf("cur=%d, last=%d\n", cur, last);

    // Output
    fprintf(fileout, "Case #%d: %lld %lld\n", t + 1, max, min);
  }

  fclose(fileout);
  fclose(filein);

  return 0;
}
