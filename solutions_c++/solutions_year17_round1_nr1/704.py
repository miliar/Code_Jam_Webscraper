#include <iostream>
#include <vector>  
using namespace std; 
 
void main()  
{  
   int T;
   cin >> T;
   for (int i = 1; i <= T; i++){
	   int R, C;
	   cin >> R >> C;
	   vector<vector<char> > cake(R, vector<char>(C, 0));
	   getchar();
	   for (int r = 0; r < R; r++){
			for (int c = 0; c < C; c++){
				cake[r][c] = getchar();
			}
			getchar();
	   }
	   for (int r = 0; r < R; r++){
		   char previous = '?';
		   for (int c = 0; c < C; c++){
			   if (cake[r][c] != '?'){
					if (previous == '?') {
						for (int cc = 0; cc < c; cc++){
							cake[r][cc] = cake[r][c];
						}
					}
					previous = cake[r][c];
			   }
			   else{
				   cake[r][c] = previous;
			   }
		   }
	   }
	   int previous_line = -1;
	   for (int r = 0 ; r < R; r++){
		   if (cake[r][0] != '?'){
			   for (int line = previous_line + 1; line <= r; line++){
					for (int c = 0; c < C; c++){
						cake[line][c] = cake[r][c];
					}
			   }
			   previous_line = r;
		   }
		   if ((r == R-1)&&(cake[r][0] == '?')){
			   for (int line = previous_line + 1; line <= r; line++){
					for (int c = 0; c < C; c++){
						cake[line][c] = cake[previous_line][c];
					}
			   }
		   }
	   }
	   
	   
	   cout << "Case #" << i << ":" << endl;
	   for ( int r = 0; r < R; r++){
			for (int c = 0; c < C; c++){
				cout << cake[r][c];
			}
			cout << endl;
	   }
   }
}  
