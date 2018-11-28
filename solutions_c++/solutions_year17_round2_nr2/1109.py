#include <stdio.h>
#define MAX_N 1005
int cnt[6];
char dmap[6];
char result[MAX_N]; 
int main(){
	dmap[0] = 'R';
	dmap[1] = 'O';
	dmap[2] = 'Y';
	dmap[3] = 'G';
	dmap[4] = 'B';
	dmap[5] = 'V';
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T; scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		int N; scanf("%d", &N);
		for(int i = 0; i < 6; i++){
			scanf("%d", &cnt[i]);
		}
		int prev = -1;
		int most = -1;
		int cUni, cCnt = -1;
		for(int i = 0; i < 6; i++){
			if(cCnt < cnt[i]){
				most = i;
				cCnt = cnt[i];
			}
		}
		result[0] = dmap[most];
		cnt[most]--;
		prev = most;
		bool isPoss = true;
		for(int i = 1; i < N; i++){ 
			cUni = -1;
			cCnt = -1;
			for(int j = 0; j < 6; j++){
				if(j != prev && cCnt < cnt[j]){
					cCnt = cnt[j];
					cUni = j;
				}
				if(j != prev && cnt[j] == cCnt && j == most){	
					cCnt = cnt[j];
					cUni = j;				
				}
			}
			if(cCnt == 0) {
				isPoss = false;
				break;
			}
			result[i] = dmap[cUni];
			cnt[cUni]--;
			prev = cUni;
		}
		result[N] = '\0';
		printf("Case #%d: %s\n", t, (!isPoss || result[0] == result[N - 1] ? "IMPOSSIBLE" : result));
	}
	return 0;
}