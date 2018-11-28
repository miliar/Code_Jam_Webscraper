// g++ AlphabetCake.cpp -o AlphabetCake && ./AlphabetCake < test.txt
#include <iostream>
#include <string>

int main(int argc, char **argv){
	int T,R,C;
	std::string S;
	char *grid;
	
	std::cin >> T;
	for(int i=1; i<T+1; i++){
		std::cin >> R;
		std::cin >> C;
		grid = new char[R*C];
		for (int r=0; r<R; r++){
			std::cin >> S;
			for(int c=0; c<C; c++){
				grid[r*C+c] = S[c];
			}
		}
		for (int r=0; r<R; r++){
			for(int c=0; c<C; c++){
				if(grid[r*C+c] == '?'){
					if(c>0){
						for(int j=c-1; j>=0; j--){
							if(grid[r*C+j] != '?'){
								grid[r*C+c] = grid[r*C+j];
								break;
							}
						}
					}
					else if (c==0){
						for(int j=c+1; j<C; j++){
							if(grid[r*C+j] != '?'){
								grid[r*C+c] = grid[r*C+j];
								break;
							}
						}
					}
				}
			}
		}
		for (int c=0; c<C; c++){
			for(int r=0; r<R; r++){
				if(grid[r*C+c] == '?'){
					if(r>0){
						for(int j=r-1; j>=0; j--){
							if(grid[j*C+c] != '?'){
								grid[r*C+c] = grid[j*C+c];
								break;
							}
						}
					}
					else if (r==0){
						for(int j=r+1; j<R; j++){
							if(grid[j*C+c] != '?'){
								grid[r*C+c] = grid[j*C+c];
								break;
							}
						}
					}
				}
			}
		}
		std::cout << "Case #" << i << ": " << std::endl;
		for (int r=0; r<R; r++){
			for(int c=0; c<C; c++){
				std::cout << grid[r*C+c];
			}
			std::cout << std::endl;
		}
	}

	return 0;
}
