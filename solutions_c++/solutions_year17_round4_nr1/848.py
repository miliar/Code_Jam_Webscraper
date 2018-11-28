#include <cstdio>
#include <cstring>
#include <algorithm>

using std::min;
using std::max;

int T, N, P, G;
int count[4];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	for(int tc=1; tc<=T; tc++) {
		scanf("%d%d", &N, &P);
		memset(count, 0, sizeof(count));
		for(int i=0; i<N; i++) {
			scanf("%d", &G);
			count[G%P]++;
		}
		int ans = N;
		if(P == 2) {
			ans -= count[1]/2;
		}
		if(P == 3) {
			int sum21 = min(count[1], count[2]);
			ans -= sum21;
			count[1] -= sum21;
			count[2] -= sum21;
			if(count[1] != 0) {
				//printf("%d %d\n", count[1], (count[1]+2)/3*2-3+(count[1]%3==0?3:count[1]%3));
				ans -= (count[1]+2)/3*2-3+(count[1]%3==0?3:count[1]%3);
			}
			else if(count[2] != 0){
				ans -= (count[2]+2)/3*2-3+(count[2]%3==0?3:count[2]%3);
			}
		}
		if(P == 4) {
			int sum22 = count[2]/2;
			ans -= sum22;
			count[2] -= sum22*2;
			int sum31 = min(count[1], count[3]);
			ans -= sum31;
			count[1] -= sum31;
			count[3] -= sum31;
			if(count[2] == 0) {
				if(count[1] != 0) {
					ans -= (count[1]+3)/4*3-4+(count[1]%4==0?4:count[1]%4);
				}
				else if(count[3] != 0) {
					ans -= (count[3]+3)/4*3-4+(count[3]%4==0?4:count[3]%4);
				}
			}
			else {
				if(max(count[1],count[3]) < 2) {
					ans -= max(count[1],count[3]);
				}
				else if(count[1] != 0) {
					// a 2-1-1 then rest
					ans -= 2;
					count[1] -= 2;
					ans -= (count[1]+3)/4*3-4+(count[1]%4==0?4:count[1]%4);
				}
				else if(count[3] != 0) {
					// a 2-3-3 then rest
					ans -= 2;
					count[3] -= 2;
					ans -= (count[3]+3)/4*3-4+(count[3]%4==0?4:count[3]%4);
				}
			}
		}
		printf("Case #%d: %d\n", tc, ans);
	}
}
