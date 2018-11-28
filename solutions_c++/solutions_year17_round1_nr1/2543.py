#include <bits/stdc++.h>

using namespace std;

const int SIZE = 30;

int tc, R, C;
char grid[SIZE][SIZE];

void fill(int r1, int r2, int c1, int c2, char ch){
   for(int row = min(r1, r2); row <= max(r1, r2); row++)
      for(int col = min(c1, c2); col <= max(c1, c2); col++)
         grid[row][col] = ch;
}

void solve(){
   for(int r1 = 0; r1 < R; r1++)
      for(int c1 = 0; c1 < C; c1++)
         if( grid[r1][c1] != '?' ){
            char ch = grid[r1][c1];
            for(int r2 = 0; r2 < R; r2++)
               for(int c2 = 0; c2 < C; c2++)
                  if( grid[r2][c2] == ch )
                     fill(r1, r2, c1, c2, ch);
         }
   for(int r1 = 0; r1 < R; r1++)
      for(int c1 = 0; c1 < C; c1++)
         if( grid[r1][c1] == '?' ){
            for(int c2 = c1 - 1; c2 >= 0; c2--)
               if( grid[r1][c2] != '?' )
                  fill(r1, r1, c1, c2, grid[r1][c2]), c2 = -1;
            for(int c2 = c1 + 1; c2 < C; c2++)
               if( grid[r1][c2] != '?' )
                  fill(r1, r1, c1, c2, grid[r1][c2]), c2 = C;
         }
   for(int r1 = 0; r1 < R; r1++)
      for(int c1 = 0; c1 < C; c1++)
         if( grid[r1][c1] == '?' ){
            for(int r2 = r1 - 1; r2 >= 0; r2--)
               if( grid[r2][c1] != '?' )
                  fill(r1, r2, c1, c1, grid[r2][c1]), r2 = -1;
            for(int r2 = r1 + 1; r2 < R; r2++)
               if( grid[r2][c1] != '?' )
                  fill(r1, r2, c1, c1, grid[r2][c1]), r2 = R;
         }
}

void read(){
   scanf("%d %d\n", &R, &C);
   for(int r = 0; r < R; r++) scanf("%s", grid[r]);
}

void print(int t){
   printf("Case #%d:\n", t);
   for(int r = 0; r < R; r++) printf("%s\n", grid[r]);
}

int main(){
   scanf("%d", &tc);
   for(int t = 1; t <= tc; t++){
      read();
      solve();
      print(t);
   }
}
