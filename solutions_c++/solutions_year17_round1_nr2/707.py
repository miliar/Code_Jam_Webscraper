#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<map>
using namespace std;

int arr[55];
int table[55][55];
int ans[55][55];
int dp[55][55][2];
int start[55];

map<int, int> m[55];
map<int, int> cur, tmpCur;
map<int, int> :: iterator it;

bool inRange(int cur, int x) {
	//printf("\t%d %d\n", x, cur);
	if(x == cur) return true;
	if(x < cur && 10 * x >= cur * 9) return true;
	if(x > cur && 10 * x <= cur * 11) return true;
	return false;
}

bool overlap(int x1, int y1, int x2, int y2) {
	if(x1 == -1 || y1 == -1 || x2 == -1 || y2 == -1) return false;
	if((y1 >= x2 && y1 <= y2) || (x1 >= x2 && x1 <= y2)) return true;
	return false;
}

main() {
	freopen("B-large.in", "r", stdin);
	freopen("outLargeB.txt", "w", stdout);
	
	int t, tc = 1;
	int n, p;
	scanf("%d", &t);
	while(t--) {
		
		
		for(int i = 0; i < 55; i++) {
			start[i] = 0;
			for(int j = 0; j < 55; j++) {
			//m[i].clear();
				ans[i][j] = 0;			
			}
		}
		//cur.clear();
		
		scanf("%d %d", &n, &p);
		for(int i = 0; i < n; i++) {
			scanf("%d", &arr[i]);
		}
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < p; j++) {
				scanf("%d", &table[i][j]);
			}
			sort(&table[i][0], &table[i][p]);
		}
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < p; j++) {
				int div = table[i][j] / arr[i];
				//printf("%d\n", div);
				bool left = true;
				bool right = true;
				
				dp[i][j][0] = dp[i][j][1] = -1;
				if(inRange(div * arr[i], table[i][j])) {
					//m[i][div]++;
					dp[i][j][0] = div;
				}
				for(int shift = 1;; shift++) {
					if(!left && !right) break;
					
					if(left) {
						int L = div - shift;
						if(inRange(L * arr[i], table[i][j])) {
							//printf("..\n");
							//m[i][L]++;
							dp[i][j][0] = L;
						} else {
							left = false;
						}
					}
					if(right) {
						int R = div + shift;
						if(inRange(R * arr[i], table[i][j])) {
							//printf("...\n");
							//m[i][R]++;
							dp[i][j][1] = R;
						} else {
							right = false;
						}
					}
				}
				if(dp[i][j][0] == -1) dp[i][j][0] = dp[i][j][1];
				else if(dp[i][j][1] == -1) dp[i][j][1] = dp[i][j][0];
				//printf("%d %d : %d %d\n", i, j, dp[i][j][0], dp[i][j][1]);
			}
			/*if(i == 0) {
				for(int j = 0; j < p; j++) {
					if(dp[i][j][0] != -1 && dp[i][j][1] != -1) ans[i][j] = 1;
				}
			} else {
				for(int j = 0; j < p; j++) {
					for(int k = 0; k < p; k++) {
						if(overlap(dp[i][j][0], dp[i][j][1], dp[i - 1][k][0], dp[i - 1][k][1])) {
							ans[i][j] += ans[i - 1][k];
							
							dp[i][j][0] = max(dp[i][j][0], dp[i - 1][k][0]);
							dp[i][j][1] = min(dp[i][j][1], dp[i - 1][k][1]);
							
							if(dp[i][j][1] < dp[i][j][0]) {
								dp[i][j][0] = dp[i][j][1] = -1;
								ans[i][j] = 0;
							}
						}
					}
				}
			}*/
			
			/*tmpCur.clear();
			for(it = m[i].begin(); it != m[i].end(); it++) {
				int key = it -> first;
				int value = it -> second;
				
				printf("%d : %d\n", key, value);
				
				if(i == 0) {
					tmpCur[key] = value;
				} else {
					if(cur.find(key) != cur.end()) {
						tmpCur[key] = cur[key] * value;
					}
				}
			}
			cur.clear();
			cur.insert(tmpCur.begin(), tmpCur.end());
			
			printf("\n");*/
		}
		
		int total = 0;
		while(true) {
			
			bool endLoop = false;
			for(int i = 0; i < n; i++) {
				if(start[i] >= p) {
					endLoop = true; 
					break; 
				}
			}
			if(endLoop) break;
			
			bool overlapAll = true;
			for(int i = 0; i < n; i++) {
				for(int j = i + 1; j < n; j++) {
					if(!overlap(dp[i][start[i]][0], dp[i][start[i]][1], dp[j][start[j]][0], dp[j][start[j]][1]))  {
						overlapAll = false;
						break;
					}
				}
				if(!overlapAll) break;
			}
			
			//printf("%d : %d %d\n", table[0][start[0]], dp[0][start[0]][0], dp[0][start[0]][1]);
			if(n == 1) {
				if(dp[0][start[0]][0] == -1 || dp[0][start[0]][1] == -1) overlapAll = false;
			}
			
			if(overlapAll) {
				total++;
				for(int i = 0; i < n; i++) {
					start[i]++;
				}
				continue;
			}
			
			int min = 10000000;
			int jum;
			for(int i = 0; i < n; i++) {
				if(dp[i][start[i]][1] < min) {
					min = dp[i][start[i]][1];
					jum = i;
				}
			}
			start[jum]++;
		}
		/*for(int i = 0; i < n; i++) {
			for(int j = 0; j < p; j++) {
				
				
				
				printf("%d ", ans[i][j]);
			}
			printf("\n");
		}*/
		
		/*int total = 0;
		for(int j = 0; j < p; j++) {
			total += ans[n - 1][j];
		}*/
		printf("Case #%d: %d\n", tc++, total);
	}
}

