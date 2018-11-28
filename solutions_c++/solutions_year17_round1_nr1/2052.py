#include <stdio.h>
#include <vector>
#include <iostream>
#include <fstream>
#include <queue>

using namespace std;

int main(){
	FILE *ipf, *opf;

	ipf = fopen("small.in","r");
	opf = fopen("stalls.out", "w");
	int T,r,c;

	fscanf(ipf, "%d", &T);
	int origT = T;
	while(T--){
		fprintf(opf, "Case #%d:\n", origT-T );
		fscanf(ipf, "%d %d\n", &r, &c);
		char grid[r][c];
		for(int i =0;i<r;i++){
			for (int j =0;j<c;j++){
				char alph;
				fscanf(ipf, "%c", &alph);
				grid[i][j] = alph;
			}
			fscanf(ipf, "\n");
		}

		bool rowExtend[r][c] = {true};
		bool colExtend[r][c] = {true};
		bool empty = true;
		int rowsEmpty = 0;
		for (int i = 0; i<r;i++){
			char currExchange = '*';
			bool isZero = true;
			vector<int> cols;
			for (int j = 0;j<c;j++){
					if (grid[i][j]=='?' || grid[i][j]=='*'){
						if (currExchange!='*'){
								// printf("%c", currExchange);
								grid[i][j] = currExchange;
							}
							else{

								cols.push_back(j);
							}
				
					}else{

						empty = false;
						isZero = false;
						currExchange=grid[i][j];
						// printf("%c  %c\n", grid[i][j], currExchange);

						for(vector<int>::iterator it = cols.begin(); it != cols.end(); ++it) {
    						grid[i][*it] = currExchange;
    						/* std::cout << *it; ... */
						}
						cols.clear();
					}
			}
			if (isZero && empty){
				rowsEmpty ++;
			}else if(isZero&&!empty){
				for (int repeat = 0; repeat < c;repeat++){
					grid[i][repeat] = grid[i-1][repeat];
				}
			}

		}
		if (rowsEmpty>0){
			for(int i =0; i<rowsEmpty;i++){
				for (int j = 0;j<c;j++){
					grid[i][j] = grid[rowsEmpty][j];
				}
			}
		}

		for (int i =0;i<r;i++){
			for (int j=0; j<c;j++){
				fprintf(opf, "%c",grid[i][j]);
			}
			
			fprintf(opf, "\n");
		}
	}

}