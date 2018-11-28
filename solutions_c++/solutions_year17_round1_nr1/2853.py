#include <iostream>
#include <cstdio>

using namespace std;

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, i, j, r, c, cases = 1, minX, minY, maxX, maxY, k, l, tmp;
	char grid[25][25];
	cin>>t;
	while(t--) {
		bool filled[25][25] = {false};
		cin>>r>>c;
		for(i = 0; i < r; i++) {
			scanf("%s", grid[i]);
		}
		for(i = 0; i < r; i++) {
			for(j = 0; j < c; j++) {
				if(grid[i][j] != '?' && !filled[i][j]) {
					for(minX = i; minX >= 0 && (grid[minX][j] == grid[i][j] || grid[minX][j] == '?'); minX--);
					minX++;
					for(maxX = i; maxX < r && (grid[maxX][j] == grid[i][j] || grid[maxX][j] == '?'); maxX++);
					maxX--;
					for(maxY = j; maxY < c && (grid[i][maxY] == grid[i][j] || grid[i][maxY] == '?'); maxY++);
					maxY--;
					for(minY = j; minY >= 0 && (grid[i][minY] == grid[i][j] || grid[i][minY] == '?'); minY--);
					minY++;
					// cout<<grid[i][j]<<" "<<minY<<" "<<maxY<<"\n";
					tmp = i;
					for(k = i - 1; k >= minX; k--) {
						for(l = minY; l <= maxY && grid[k][l] == '?'; l++);
						if(l != maxY + 1) break;
						tmp = k;
					}
					minX = tmp;
					tmp = i;
					for(k = i + 1; k <= maxX; k++) {
						for(l = minY; l <= maxY && (grid[k][l] == '?' || grid[k][l] == grid[i][j]); l++);
						if(l != maxY + 1) break;
						tmp = k;
						// cout<<k<<" "<<tmp<<"\n";
					}
					maxX = tmp;

					// for(k = minX; k <= maxX; k++) {
					// 	tmp = j;
					// 	for(l = j - 1; l >= minY && grid[k][l] == '?'; l--) {
					// 		tmp = l;
					// 	}
					// 	if(tmp != minY) {
					// 		if(k <= i) minX = 
					// 		break;
					// 	}
					// 	minY = tmp;
					// 	tmp = j;
					// 	for(l = j + 1; l <= maxY && grid[k][l] == '?'; l++) {
					// 		tmp = l;
					// 	}
					// 	if(tmp != maxY) break;
					// 	maxY = tmp;
					// 	// cout<<k<<" "<<j+1<<" "<<grid[k][j+1]<<" "<<maxY<<"\n";
					// }

					// cout<<"=========";
					for(k = minX; k <= maxX; k++) {
						for(l = minY; l <= maxY; l++) {
							grid[k][l] = grid[i][j];
							filled[k][l] = true;
						}
					}
				}
			}
		}
		cout<<"Case #"<<cases<<":\n";
		for(i = 0; i < r; i++) cout<<grid[i]<<"\n";
		cases++;
	}
	return 0;
}