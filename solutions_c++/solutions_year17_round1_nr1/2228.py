#include <stdio.h>
#include <iostream>
#include <vector>


using namespace std;

int main(){

   int T;

   scanf("%d", &T);

   for(int t=1; t<=T; t++){

      int C, R;

      scanf("%d %d", &R, &C);

      vector< string > cake(R);

      for(int r = 0; r<R; r++){
         cin >> cake[r];

         for(int j=0; j<C; j++){
            if(cake[r][j] != '?'){
               for(int i=j-1; i>=0 && cake[r][i] == '?'; i--){
                  cake[r][i] = cake[r][j];
               }
               for(int i=j+1; i<C && cake[r][i] == '?'; i++){
                  cake[r][i] = cake[r][j];
               }
            }
         }
      }

      for(int i=0; i<R; i++){
         for(int j=0; j<C; j++){
            // cout << i << " - " << j << endl;
            if(cake[i][j] != '?'){
               for(int k=i-1; k>=0 && cake[k][j] == '?'; k--){
                  cake[k][j] = cake[i][j];
               }
               for(int k=i+1; k<R && cake[k][j] == '?'; k++){
                  cake[k][j] = cake[i][j];
               }
            }
         }
      }

      printf("Case #%d:\n", t);

      for(int i=0; i<R; i++){
         cout << cake[i] << "\n";
      }
   }

   return 0;
}
