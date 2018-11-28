#include <iostream>
#include <math.h>
using namespace std;

int main(){
	int t;
	int r,c,pin;
	char spare;
	scanf("%d\n", &t);
	for (int _=1; _<=t; _++){
		scanf("%d %d\n", &r, &c);
		char grid[r][c];
		for (int i=0; i<r; i++){
			for(int j=0; j<c; j++)
				scanf("%c", &grid[i][j]);
			scanf("%c", &spare);
		}
		for (int i=0; i<r; i++){
			for(int j=0; j<c; j++){
				while(grid[i][j]=='?' && j<c) j++;
				if (j<c){
					spare = grid[i][j];
					pin = j-1;
					while(pin>=0&&grid[i][pin]=='?') {
						grid[i][pin] = spare;
						pin--;
					}
					pin = j+1;
					while(pin<c&&grid[i][pin]=='?') {
						grid[i][pin] = spare;
						pin++;
					}
					j = pin-1;
				}
			}
		}
		if (grid[0][0]=='?'){
			pin = 1;
			while(grid[pin][0]=='?') pin++;
			for (int j=0; j<c; j++) grid[0][j]=grid[pin][j];
		}
		for(int i=1; i<r; i++)
			if (grid[i][0]=='?')
				for (int j=0; j<c; j++) grid[i][j]=grid[i-1][j];


		printf("Case #%d:\n", _); 
		for (int i=0; i<r; i++){
			for(int j=0; j<c; j++)
				printf("%c",grid[i][j] );
			printf("\n");
		}
	}
}