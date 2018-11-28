
#include<bits/stdc++.h>
#define all(x) x.begin(), x.end()
#define pb(x) push_back(x)
#define cout2(x, y) cout << x << " " << y << endl
#define N 26

using namespace std;

bool vis[N][N];
char T[N][N];

int main(){

	int tc = 0, caso = 1;
	scanf("%d", &tc);
	
	while(tc--){
		
		int r, c;
		scanf("%d%d", &r, &c);
		
		memset(vis, false, sizeof vis);
		for(int i = 0; i < r; i++){
			
			scanf("%s", T[i]);
			for(int j = 0; j < c; j++){
				
				if(T[i][j] != '?')vis[i][j] = true;
			}
		}
			
		
		for(int i = 0; i < r; i++){
			
			for(int j = 0; j < c; j++){
				
				if(!vis[i][j])continue;
				
				int minCol = c + 1, minRow = 0;
				for(int ii = i; ii < r; ii++){
					
					int col = 0;
					for(int jj = j; jj < c; jj++){
						
						if(T[ii][jj] != '?' && T[ii][jj] != T[i][j])break;
						col++;
					}
	
					if(col == 0)break;
					if(ii != i && col < minCol)break;
					minCol = min(minCol, col);
					minRow++;
				}

				int rr = i + minRow - 1, cc = j + minCol - 1;
				minCol = c + 1, minRow = 0;
				
				for(int ii = rr; ii >= 0; ii--){
					
					int col = 0;
					for(int jj = cc; jj >= 0; jj--){
						
						if(T[ii][jj] != '?' && T[ii][jj] != T[i][j])break;
						col++;
						
					}
					if(col == 0)break;
					minCol = min(minCol, col);
					minRow++;
				}
				
				int tor = rr - minRow + 1, toc = cc - minCol + 1;
				for(int ii = rr; ii >= tor; ii--){
					
					for(int jj = cc; jj >= toc; jj--){
						
						T[ii][jj] = T[i][j];
					}
				}

				/*puts("**********************");
				for(int i = 0; i < r; i++)printf("%s\n", T[i]);
				puts("**********************");*/
			}
			
		}
		
		printf("Case #%d:\n", caso++);
		for(int i = 0; i < r; i++)printf("%s\n", T[i]);

		
	}
}

