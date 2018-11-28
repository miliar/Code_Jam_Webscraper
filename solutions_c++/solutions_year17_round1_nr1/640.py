#include<bits/stdc++.h>
using namespace std;
char grid[30][30];
bool blank[30];

int main()
{
	int R,C,i,j,k,l;
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int T,it;
	scanf("%d", &T);

	for(it=1; it<=T; it++){
	scanf("%d%d", &R, &C);

	for(i=0; i<R; i++){
		scanf("%s", grid[i]);
	}

	//cout<<grid[0]<<endl;

	for(i=0; i<R; i++){

		blank[i] = 1;

		for(j=0; j<C; j++){
			if(grid[i][j] != '?')  blank[i] = 0;
		}

		if(!blank[i]){

			int lastpos = 0;
			char lastchar = 0;

			for(j=0; j<C; j++){
				if(grid[i][j] != '?'){
					lastchar = grid[i][j];
					for(k=lastpos; k<j; k++)  grid[i][k] = lastchar;
					lastpos = j+1;
				}
			}

			for(k=lastpos; k<C; k++)
				grid[i][k] = lastchar;
		}
	}

	for(i=0; i<R; i++){

		if(!blank[i])  continue;

		j = i+1;
		while(j<R && blank[j]) j++;

		if(i-1>=0){

			for(k=i; k<j; k++){
				for(l=0; l<C; l++)
					grid[k][l] = grid[i-1][l];
			}
		}

		else{
			for(k=i; k<j; k++){
				for(l=0; l<C; l++)
					grid[k][l] = grid[j][l];
			}
		}
		i = j-1;
	}

	printf("Case #%d:\n", it);
	for(i=0; i<R; i++){
		for(j=0; j<C; j++)  printf("%c", grid[i][j]);
		puts("");
	}
	}
	return 0;
}