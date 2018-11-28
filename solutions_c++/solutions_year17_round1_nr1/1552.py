#include <iostream>

using namespace std;

#define MAXN 30

char d[MAXN][MAXN];
int check[MAXN][MAXN];
int R, C;

void solve(){
	for(int i = 0; i < R; i++){
		for(int j = 0; j < C; j++){
			if( d[i][j] != '?' && check[i][j] == 0){
				char now = d[i][j]; check[i][j] = 1;
				int k;
				for(k = j-1; k >= 0; k--){
					if(d[i][k] != '?') break;
					else{ d[i][k] = now; check[i][k] = 1;
					}
				}
				int cs = k+1;
				for(k = j+1; k < C; k++){
					if(d[i][k] != '?') break;
					else{
						d[i][k] = now; check[i][k] = 1;
					}
				}
				int ce = k;
				for(k = i-1; k >= 0; k--){
					int l;
					for(l = cs; l < ce; l++){
						if(d[k][l] != '?') break;
					}
					if(l == ce){
						for(l = cs; l < ce; l++){
							d[k][l] = now; check[k][l] = 1;
						}
					}
					else break;
				}
				for(k = i+1; k < R; k++){
					int l;
					for(l = cs; l < ce; l++){
						if(d[k][l] != '?') break;
					}
					if(l == ce){
						for(l = cs; l < ce; l++){
							d[k][l] = now; check[k][l] = 1;
						}
					}
					else break;
				}
			}
		}
	}
}

void init(){
	for(int i = 0; i < R; i++){
		for(int j = 0; j < C; j++){
			check[i][j] = 0;
		}
	}
}

int main(){
	freopen("A-large.in", "rt", stdin);
	freopen("output", "wt", stdout);
	int T;
	scanf("%d", &T);
	for(int i = 0; i < T; i++){
		scanf("%d %d", &R, &C);
		for(int j = 0; j < R; j++){
			scanf("%s", d[j]);
		}
		init();
		solve();
		printf("Case #%d:\n", i+1);
		for(int j = 0; j < R; j++){
			printf("%s\n", d[j]);
		}
		
	}

	return 0;
}