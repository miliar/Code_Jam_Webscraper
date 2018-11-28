#include <bits/stdc++.h>

#define ff first
#define ss second
#define mp make_pair

using namespace std;

typedef long long ll;

char mat[30][30];
bool vis[30][30];

int main(){
	int T;

	scanf("%d", &T);

	for(int t = 1; t <= T; t++){
		int r,c;
		scanf("%d%d", &r, &c);

		for(int i = 0; i < r; i++)
			scanf(" %s", mat[i]);

		memset(vis,0,sizeof vis);

		for(int i = 0; i < r; i++){
			for(int j = 0; j < c; j++){
				if(mat[i][j] != '?' && !vis[i][j]){
					// printf("%d,%d\n", i,j);
					vis[i][j] = 1;
					int k1,k2;
					for(k1 = j+1; k1 < c && mat[i][k1] == '?'; k1++)
						mat[i][k1] = mat[i][j], vis[i][k1] = 1;
					for(k2 = j-1; k2 >= 0 && mat[i][k2] == '?'; k2--)
						mat[i][k2] = mat[i][j], vis[i][k2] = 1;
					k2++; k1--;

					for(int l = i+1; l < r; l++){
						bool flag = 1;
						for(int m = k2; m <= k1; m++){
							if(mat[l][m] != '?' && mat[l][m] != mat[i][j]){
								flag = 0;
								break;
							}
						}
						if(!flag) break;
						for(int m = k2; m <= k1; m++){
							mat[l][m] = mat[i][j];
							vis[l][m] = 1;
						}
					}
					for(int l = i-1; l >= 0; l--){
						bool flag = 1;
						for(int m = k2; m <= k1; m++){
							if(mat[l][m] != '?' && mat[l][m] != mat[i][j]){
								flag = 0;
								break;
							}
						}
						if(!flag) break;
						for(int m = k2; m <= k1; m++){
							mat[l][m] = mat[i][j];
							vis[l][m] = 1;
						}
					}

				}
			}
		}



		printf("Case #%d:\n",t);
		for(int i = 0; i < r; i++)
			printf("%s\n", mat[i]);
	}
	
	return 0;
}