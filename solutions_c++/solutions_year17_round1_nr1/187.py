#include <bits/stdc++.h>

using namespace std;

typedef long long lint;
typedef pair<int,int> pii;

int main(){
	freopen("test.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin.sync_with_stdio(0); cin.tie(0);
	int T;
	cin >> T;
	for (int asd = 0; asd<T; ++asd){
		char grid[30][30];
		int R, C;
		cin >> R >> C;
		for (int i=1; i<=R; ++i){
			for (int j=1; j<=C; ++j){
				cin >> grid[i][j];
			}
		}
		for (int i=1; i<=R; ++i){
			for (int j=2; j<=C; ++j){
				if (grid[i][j-1] != '?' && grid[i][j] == '?')
					grid[i][j] = grid[i][j-1];
			}
		}
		for (int i=1; i<=R; ++i){
			for (int j=C-1; j>=1; --j){
				if (grid[i][j+1] != '?' && grid[i][j] == '?')
					grid[i][j] = grid[i][j+1];
			}
		}
		for (int i=2; i<=R; ++i){
			for (int j=1; j<=C; ++j){
				if (grid[i][j] == '?' && grid[i-1][j] != '?')
					grid[i][j] = grid[i-1][j];
			}
		}
		for (int i=R-1; i>=1; --i){
			for (int j=1; j<=C; ++j){
				if (grid[i+1][j] != '?' && grid[i][j] == '?')
					grid[i][j] = grid[i+1][j];
			}
		}
		printf("Case #%d:\n", asd+1);
		for (int i=1; i<=R; ++i){
			for (int j=1; j<=C; ++j){
				printf("%c", grid[i][j]);
			}
			printf("\n");
		}

	}
	return 0;
}