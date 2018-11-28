#include<iostream>
//#include<bits/stdc++.h>
#include<stdio.h>
#include<vector>

using namespace std;

int T, R, C;
char M[30][30];


int main() {
  //FILE *in = fopen("input.txt", "r");
  FILE *in = fopen("A-large.in", "r");
  //scanf("%d", &T);
  fscanf(in, "%d", &T);

  FILE *out = fopen("A-small.out", "w");

  for(int i = 0; i < T; i++) {
    //scanf("%d %d", &R, &C);
    fscanf(in, "%d %d", &R, &C);

    int blank = 0;

    for(int j = 0; j < R; j++) {
      //scanf("%s", M[j]);
      fscanf(in, "%s", M[j]);

      for(int k = 0; k < C; k++) {
        if(M[j][k] == '?') {
          blank += 1;
        }
      }
    }

    while(blank > 0) {
    for(int r = 0; r < R; r++) {
      for(int c = 0; c < C; c++) {
        char m = M[r][c];

        int before;
        if(m != '?') {
          before = c;
          for(int j = c + 1; j < C; j++) {
            if(j - before > 1) break;
            if(M[r][j] == '?') {
              M[r][j] = m;
              before = j;
              blank -= 1;
            }
          }
          before = c;
          for(int j = c - 1; j >= 0; j--) {
            if(before - j > 1) break;
            if(M[r][j] == '?') {
              M[r][j] = m;
              before = j;
              blank -= 1;
            }
          }
        }
      }
    }

    for(int c = 0; c < C; c++) {
      for(int r = 0; r < R; r++) {
        char m = M[r][c];

        int before;
        if(m != '?') {
          before = r;
          for(int j = 0; j < R; j++) {
            if(j - before > 1) break;
            if(M[j][c] == '?') {
              M[j][c] = m;
              before = j;
              blank -= 1;
            }
          }
          before = r;
          for(int j = r - 1; j >= 0; j--) {
            if(before - j > 1) break;
            if(M[j][c] == '?') {
              M[j][c] = m;
              before = j;
              blank -= 1;
            }
          }
        }
      }
    }
    }


    //while(blank.size() > 0) {
    //  for(int j = 0; j < blank.size(); j++) {
    //    int r = blank[j].first;
    //    int c = blank[j].second;
//
 //       fill(r, c);
  //    }
   // }

    //printf("Case #%d:\n", i + 1);
    fprintf(out, "Case #%d:\n", i + 1);
    for(int j = 0; j < R; j++) {
      //printf("%s\n", M[j]);
      fprintf(out, "%s\n", M[j]);
    }
  }

  return 0;
}