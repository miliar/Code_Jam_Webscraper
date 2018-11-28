#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;

#define fastio ios_base::sync_with_stdio(false)
#define fi first
#define se second

int T, r, c, x, y, z, vis[50][50];
char mat[50][50], q;
bool yes, can;


void prt(){
	for(int i = 0; i < r; ++i){
		for(int j = 0; j < c; ++j) printf("%c", mat[i][j]);
		printf("\n");
	}
}

int main(){
	scanf("%d", &T);
	
	for(int t = 1; t <= T; ++t){
		scanf("%d%d", &r, &c);
		printf("Case #%d:\n", t);
		yes = false;
		
		for(int i = 0; i < r; ++i){
			for(int j = 0; j < c; ++j){
				scanf(" %c", &mat[i][j]);
				if(mat[i][j] == '?') yes = true;
			}
		}
		
		if(yes){
			for(int i = 0; i < r; ++i){
				for(int j = 0; j < c; ++j){
					if(mat[i][j] != '?' && vis[i][j] != t){
						x = y = j;
						
						for(int k = j - 1; k >= 0; k--){
							if(mat[i][k] == '?') x = k;
							else break;
						}
						for(int k = j + 1; k < c; k++){
							if(mat[i][k] == '?') y = k;
							else break;
						}
						
						for(int k = x; k < y + 1; ++k){
							mat[i][k] = mat[i][j];
							vis[i][k] = t;
						}
						
						can = true;
						
						for(int k = i - 1; k >= 0 && can; --k){
							for(int l = x; l < y + 1 && can; ++l)
								if(mat[k][l] != '?' || vis[k][l] == t) can = false;
							if(can){
								for(int l = x; l < y + 1 && can; ++l){
									mat[k][l] = mat[i][j];
									vis[k][l] = t;
								}
							}
						}
						
						can = true;
						
						for(int k = i + 1; k < r && can; ++k){
							for(int l = x; l < y + 1 && can; ++l)
								if(mat[k][l] != '?' || vis[k][l] == t) can = false;
							if(can){
								for(int l = x; l < y + 1 && can; ++l){
									mat[k][l] = mat[i][j];
									vis[k][l] = t;
								}
							}
						}
					}
				}
			}	
		}
			
		prt();
	}

	return 0;
}
