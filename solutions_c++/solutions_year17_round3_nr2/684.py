#include <bits/stdc++.h>
using namespace std;

#define MAX 100000;

const int N = 102;
int t, ac, aj;
int c1[N], d1[N], c2[N], d2[N];
int dp[3][730][730];
int tempo[1500];
int beg;

int go(int quem, int t1, int t2){
	if(t1 > 720 or t2 > 720) return MAX;
	if(tempo[t1+t2] == 1 and quem == 1) return MAX;
	if(tempo[t1+t2] == 2 and quem == 2) return MAX;
	if(t1 == 720 and t2 == 720){
		if(quem != beg) return 1;
		else return 0;
		//return 0;
	}
	if(dp[quem][t1][t2] != -1) return dp[quem][t1][t2];
	
	int tt1 = t1, tt2 = t2;
	if(quem == 1) tt1++;
	if(quem == 2) tt2++;
	
	int r1 = go(1, tt1, tt2);
	if(quem == 2) r1++;
	
	int r2 = go(2, tt1, tt2);
	if(quem == 1) r2++;
	
	return dp[quem][t1][t2] = min(r1, r2);
}

int main(void){
	scanf("%d", &t);
	
	for(int caso = 1; caso <= t; caso++){
		memset(tempo, 0, sizeof tempo);
		scanf("%d%d", &ac, &aj);
		
		for(int i = 0; i < ac; i++){
			scanf("%d%d", &c1[i], &d1[i]);
			for(int j = c1[i]; j < d1[i]; j++){
				tempo[j] = 1;
			}
		}
		for(int i = 0; i < aj; i++){
			scanf("%d%d", &c2[i], &d2[i]);
			for(int j = c2[i]; j < d2[i]; j++){
				tempo[j] = 2;
			}
		}
		
		/*for(int i = 0; i < 3; i++){
			for(int j = 0; j < 730; j++){
				for(int k = 0; k < 730; k++){
					dp[i][j][k] = -1;
				}
			}
		}*/
		
		memset(dp, -1, sizeof dp);
		
		beg = 1;
		int res1 = go(1,0,0);
		
		/*for(int i = 0; i < 3; i++){
			for(int j = 0; j < 730; j++){
				for(int k = 0; k < 730; k++){
					dp[i][j][k] = -1;
				}
			}
		}*/
		
		memset(dp, -1, sizeof dp);
		
		beg = 2;
		int res2 = go(2,0,0);
		
		//if(res1 == 1) res1++;
		//if(res2 == 1) res2++;
		
		printf("Case #%d: %d\n", caso, min(res1, res2));
	}
	
	return 0;
}
