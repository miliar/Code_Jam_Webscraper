#include<bits/stdc++.h>
using namespace std;
int main() {
	int T;
	cin >> T;
	for (int test = 1 ; test <= T; test++) {
		int x, y, unknow = 0;
		scanf("%d %d\n", &x, &y);
		int grid[x + 2][y + 2] = {0};
		memset(grid,0,sizeof(grid));
		for (int i = 1 ; i <= x; i++) {
			char tmp[30];
			scanf("%s", &tmp);
			for (int k = 1 ; k <= y; k++) {
				if (tmp[k - 1] == '?') {
					unknow++;
				}
				grid[i][k] = tmp[k - 1];
			}
		}
		for (int i = 1 ; i <= x && unknow; i++) {
			for (int k = 1 ; k <= y; k++) {
				if (grid[i][k] != '?') {
					int now = i + 1;
					while (now <= x) {
						if (grid[now][k] == '?') {
							grid[now][k] = grid[i][k];
							unknow--;
						} else {
							break;
						}
						now++;
					}
					now = i - 1;
					while (now >= 1) {
						if (grid[now][k] == '?') {
							grid[now][k] = grid[i][k];
							unknow--;
						} else {
							break;
						}
						now--;
					}
				}
			}
		}

		for (int i = 1 ; i <= x && unknow; i++) {
			for (int k = 1 ; k <= y; k++) {
				if (grid[i][k] != '?') {
					int t = i + 1, counter = 1;
					while (grid[t][k] == grid[i][k] && t <= x) {
						t++;
						counter++;
					}

					int now = k;
					int times = -1;
					bool tag = true;
					
					while (tag && now <= y) {
						now++;
						times++;
						for (int s = 0 ; s < counter ; s++) {
							//printf("%d %d %d %c %c\n",counter,now,times,grid[i+s][now],grid[i][k]);
							if (grid[i+s][now] != '?') {
								tag = false;
								break;
							}
						}
						
					}
					//printf("out : %d %d %d %d %c %c\n",times,counter,now,times,grid[i][k]);
					for (int s = 1; s <= times; s++) {
						for (int kt = 0; kt < counter; kt++) {
							grid[i+kt][k+s] = grid[i][k];
						}
					}

					now = k;
					times = -1;
					tag = true;
					
					while (tag && now >= 1) {
						now--;
						times++;
						for (int s = 0 ; s < counter ; s++) {
							//printf("%d %d %d %c %c\n",counter,now,times,grid[i+s][now],grid[i][k]);
							if (grid[i+s][now] != '?') {
								tag = false;
								break;
							}
						}
						
					}
					//printf("out : %d %d %d %d %c %c\n",times,counter,now,times,grid[i][k]);
					for (int s = 1; s <= times; s++) {
						for (int kt = 0; kt < counter; kt++) {
							grid[i+kt][k-s] = grid[i][k];
						}
					}
				}
			}
		}

		printf("Case #%d:\n", test);
		for (int i = 1 ; i <= x; i++) {
			for (int k = 1 ; k <= y; k++) {
				printf("%c", grid[i][k]);
			}
			puts("");
		}
	}
}