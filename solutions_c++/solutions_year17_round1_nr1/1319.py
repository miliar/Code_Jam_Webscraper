#include <iostream>
#include <cstdlib>
using namespace std;
char grid[100][100];

int main(){
  int T; 
  cin >> T;
  for(int t=1;t<=T;t++){
   int R, C; 
   cin >> R >> C;
   for(int i=0;i<R;i++)
      for(int j=0;j<C;j++)
         cin >> grid[i][j];
   // <----
   for(int i=0;i<R;i++){
   	  char state='?';
      for(int j=0;j<C;j++){
	     if(grid[i][j]!='?')
	        state=grid[i][j];
	     else if(state!='?')
	        grid[i][j] = state;
	  }
   }
   // ---->
   for(int i=0;i<R;i++){
      char state='?';
      for(int j=C-1;j>=0;j--){
	     if(grid[i][j]!='?')
	        state=grid[i][j];
	     else if(state!='?')
	        grid[i][j] = state;
	  }
   }
   // up
   for(int j=0;j<C;j++){
      char state='?';
      for(int i=0;i<R;i++){
	     if(grid[i][j]!='?')
	        state=grid[i][j];
	     else if(state!='?')
	        grid[i][j] = state;
	  }
   }
   // down
   for(int j=0;j<C;j++){
      char state='?';
      for(int i=R-1;i>=0;i--){
	     if(grid[i][j]!='?')
	        state=grid[i][j];
	     else if(state!='?')
	        grid[i][j] = state;
	  }
   }
   cout << "Case #" << t << ":\n";
   for(int i=0;i<R;i++){
      for(int j=0;j<C;j++) cout << grid[i][j];
      cout << "\n";
   }
  }
   
} 
