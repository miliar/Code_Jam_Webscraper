#include <iostream>
#include <string>
#include <fstream>
//#include <bits/stdc++.h>
using namespace std;


int main(){

	int T;
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	fin >> T;

	for(int t = 0; t < T ; t++){
		int R, C;
		fin >> R >> C;

		char grid[R][C];
		for(int r =0; r < R; r++){

			for(int c = 0; c < C; c++){

				fin >> grid[r][c];

			}

		}

		for(int r =0; r < R; r++){

			for(int c = 0; c < C; c++){

				 if(grid[r][c] != '?'){

					int c1 = c-1;
					while(c1 >= 0 ){
						if(grid[r][c1] != '?') break;
						grid[r][c1] = grid[r][c];
						c1--;
					}

					c1 = c+1;
					while(c1 < C ){
						if(grid[r][c1] != '?') break;
						grid[r][c1] = grid[r][c];
						c1++;
					}
				  

				}

			}

		}


		for(int r = 0; r < R; r++){

			if(grid[r][0] != '?'){

				int r1 = r-1;
				while(r1 >= 0 ){
					if(grid[r1][0] != '?') break;
					for(int c1 = 0; c1 < C; c1++) grid[r1][c1] = grid[r][c1];
					r1--;
				}

				r1 = r+1;
				while(r1 < R ){
					if(grid[r1][0] != '?') break;
					for(int c1 = 0; c1 < C; c1++) grid[r1][c1] = grid[r][c1];
					r1++;
				}

			}

		}

		



		fout << "Case #" << t+1 << ": " <<endl;
		for(int r =0; r < R; r++){

			for(int c = 0; c < C; c++){

				fout << grid[r][c];

			}
			fout << endl;

		}



		
	}

	fin.close();
	fout.close();

	return 0;
}
