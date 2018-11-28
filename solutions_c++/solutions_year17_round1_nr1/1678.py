#include <cstdio>
#include <cstring>

int T, R, C;
char cake[26][26];

void solve(int n){
	char ch;
	int r2, c2;

	scanf("%d %d", &R, &C);
	for(int i = 0; i < R; i++)
		scanf("%s", cake[i]);

	
	for(int r = 0; r < R; r++){
		for(int c = 0; c < C; c++){
			if(cake[r][c] != '?'){
				ch = cake[r][c];
				c2 = c;
				while(cake[r][--c2] == '?')
					cake[r][c2] = ch;
				c2 = c;
				while(cake[r][++c2] == '?')
					cake[r][c2] = ch;
			}
		}
	}

	for(int r = 0; r < R; r++){
		for(int c = 0; c < C; c++){
			if(cake[r][c] != '?'){
				ch = cake[r][c];
				r2 = r;
				while(cake[--r2][c] == '?')
					cake[r2][c] = ch;
				r2 = r;
				while(cake[++r2][c] == '?')
					cake[r2][c] = ch;
			}
		}
	}

	printf("Case #%d: \n", n);
	for(int i = 0; i < R; i++)
		printf("%s\n", cake[i]);
}

int main(){
	scanf("%d", &T);
	for(int i = 1; i <= T; i++)
		solve(i);
}
