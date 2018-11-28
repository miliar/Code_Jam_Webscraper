#include <iostream>
#include <stdio.h>
#include <string>
#include <math.h>
#include <vector>
#include <stdlib.h>

using namespace std;

int compare (const void * a, const void * b)
{
	return ( *(int*)a - *(int*)b );
}

void * solve(){
	void * ans;
	int row, col, i, j, fr, fc;
	char cake[26][26], temp;
	
	cin >> row >> col;
	//read stuf
	for (i = 0; i < row; i++) {
		for (j = 0; j < col; j++) {
			scanf(" %c", &temp);
			cake[i][j] = temp;
		}
		scanf("\n");
	}
	
	//program
	
	for (i = 0; i < row; i++) {
		//find
		j = 0;
		while (j < col && cake[i][j] == '?') {
			j++;
		}
		
		if (j == col) {
			fr = -1;
		}
		else {
			fr = j; //found it!
			for (j = 0; j < fr; j++) {
				cake[i][j] = cake[i][fr];
			}
		}
		
		//extend right
		if (fr != -1) {
			temp = cake[i][fr];
			j = fr + 1;
			while (j < col) {
				if (cake[i][j] == '?') {
					cake[i][j] = temp;
				}
				else {
					temp = cake[i][j];
				}
				j++;
			}
		}		
		
	}
		
	//find again
	i = 0;
	while (cake[i][0] =='?') {
		i++;
	}
	
	//up
	fc = i;
	for (i = 0; i < fc; i++) {
		for (j = 0; j < col ; j++) {
			cake[i][j] = cake[fc][j];
		}
	}
	
	//down
	i = fc + 1;
	while (i < row) {
		if (cake[i][0] != '?') {
			fc = i;
		}
		else {
			for (j = 0; j < col; j++) {
				cake[i][j] = cake[fc][j];
			}
		}
		i++;
	}
	
	//done , write the answer
	
	for (i = 0; i < row; i++) {
		for (j = 0; j < col; j++) {
			printf("%c", cake[i][j]);
		}
		printf("\n");
	}
	
	
	return ans;
}



int main (int argc, char * const argv[]) {
    int ncases, cases;
	scanf("%d\n", &ncases);
	for (cases = 0; cases < ncases; cases++) {
		cout << "Case #" << cases + 1 << ": " << endl;
		solve();
		//cout << endl;
	}
    return 0;
}
