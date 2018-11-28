#include <algorithm>
#include <cstdio>
using namespace std;

int T, N, P, G, tmp, ans;
int rem[4];

int main (){
	freopen ("A-large.in", "r", stdin);
	freopen ("A-large.out", "w", stdout);
	scanf("%d", &T);
	for (int i = 1; i <= T; i++){
		scanf("%d %d", &N, &P);
		for (int j = 0; j < P; j++)
			rem[j] = 0;
		for (int j = 0; j < N; j++){
			scanf("%d", &G);
			rem[G % P]++;
		}
		if (P == 2){
			ans = rem[0] + (rem[1] + 1) / 2;
		} else if (P == 3){
			tmp = min(rem[1], rem[2]);
			ans = rem[0] + tmp + (rem[1] - tmp + 2) / 3 + (rem[2] - tmp + 2) / 3;
		} else if (P == 4){
			tmp = min(rem[1], rem[3]);
			ans = rem[0] + tmp;
			rem[1] -= tmp;
			rem[3] -= tmp;
			if (rem[1] > 0){
				ans += rem[2] / 2;
				rem[2] %= 2;
				if (rem[2] == 0){
					ans += (rem[1] + 3) / 4;
				} else {
					ans += (rem[1] + 5) / 4;
				}
			} else if (rem[3] > 0){
				ans += rem[2] / 2;
				rem[2] %= 2;
				if (rem[2] == 0){
					ans += (rem[3] + 3) / 4;
				} else {
					ans += (rem[3] + 5) / 4;
				}
			} else {
				ans += (rem[2] + 1) / 2;
			}
		}
		printf("Case #%d: %d\n", i, ans);
	}
	fclose (stdin);
	fclose (stdout);
	return 0;
}
