#include <cstdio>
#include <cmath>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

char s[105][105];
char add[105][105];

char inp[105];

bool colx[105];

int main(){
	int T;
	scanf("%d", &T);
	for(int t=1;t<=T;t++){

		memset(colx, 0, sizeof(colx));

		int N, M, R, C;
		scanf("%d%d", &N, &M);

		for(int i=1;i<=N;i++) for(int j=1;j<=N;j++) s[i][j] = '.', add[i][j] = '.';

		int xpos = 0;
		int opos = 0;
		for(int i=0;i<M;i++){
			scanf("%s", inp);
			scanf("%d%d", &R, &C);
			s[R][C] = inp[0];
			add[R][C] = inp[0];
			if(inp[0] == 'x'){
				colx[C] = 1;
				xpos = C;
			}
			else if(inp[0] == 'o'){
				colx[C] = 1;
				opos = 1;
			}
		}
		if(N == 1){
			add[1][1] = 'o';
		}
		else{
			if(xpos == 0 && opos == 0){
				for(int j=1;j<=N;j++){
					if(add[1][j] == '.' && !colx[j]){
						colx[j] = 1;
						add[1][j] = 'x';
						xpos = j;
						break;
					}
				}
			}
			for(int i=2;i<=N-1;i++){
				bool succ = 0;
				for(int j=2;j<=N-1;j++){
					if(colx[j]) continue;
					colx[j] = 1;
					add[i][j] = 'x';
					succ = 1;
					break;
				}
				if(!succ){
					add[i][N] = 'x';
					colx[N] = 1;
				}
			}

			if(colx[1]){
				add[N][N] = 'x';
				colx[N] = 1;
			}
			else{
				add[N][1] = 'x';
				colx[1] = 1;
			}


			for(int i=1;i<=N;i++){
				if(add[1][i] == '.') add[1][i] = '+';
			}
			for(int i=2;i<=N-1;i++){
				if(add[N][i] == '.') add[N][i] = '+';
			}

			if(opos == 0){
				if(xpos != 0){
					add[1][xpos] = 'o';
				}
				else{
					add[1][N] = 'o';
				}
			}
		}
		int ans1=0, ans2=0;
		printf("Case #%d: ", t);

		for(int i=1;i<=N;i++){
			for(int j=1;j<=N;j++){
				if(add[i][j] == '.') continue;
				if(add[i][j] == 'o') ans1+=2;
				else ans1++;

				if(s[i][j] != add[i][j]){
					ans2++;
				}
			}
		}
		printf("%d %d\n", ans1, ans2);
		for(int i=1;i<=N;i++){
			for(int j=1;j<=N;j++){
				if(add[i][j] == '.') continue;
				if(s[i][j] != add[i][j]) printf("%c %d %d\n", add[i][j], i, j);
			}
		}
	}
}