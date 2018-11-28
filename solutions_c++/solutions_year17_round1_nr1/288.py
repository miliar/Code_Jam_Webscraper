#include<bits/stdc++.h>
using namespace std;

int TC, TCs;
int R, C;
char cake[30][30];
int i, x, y;

int main(){
	scanf("%d", &TCs);
	for (TC=1; TC<=TCs; TC++){
		printf("Case #%d:\n", TC);
		scanf("%d%d", &R, &C);
		for (y=0; y<R; y++) scanf("%s", cake[y]);
		
		for (y=0; y<R; y++) for (x=0; x<C; x++) if (cake[y][x]!='?'){
			for (i=x+1; i<C; i++){
				if (cake[y][i]!='?') break;
				cake[y][i] = cake[y][x];
			}
			for (i=x-1; i>=0; i--){
				if (cake[y][i]!='?') break;
				cake[y][i] = cake[y][x];
			}
		}
		
		for (x=0; x<C; x++) for (y=0; y<R; y++) if (cake[y][x]!='?'){
			for (i=y+1; i<R; i++){
				if (cake[i][x]!='?') break;
				cake[i][x] = cake[y][x];
			}
			for (i=y-1; i>=0; i--){
				if (cake[i][x]!='?') break;
				cake[i][x] = cake[y][x];
			}
		}
		
		for (y=0; y<R; y++) puts(cake[y]);
	}
	
	
	return 0;
}


