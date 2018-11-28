#include <algorithm>
#include <cstdio>
using namespace std;
bool checker;
int T, N, P, ans;
int R[50], Q[50][50], lower[50][50], upper[50][50], point[50], large;
bool compare(int x, int y){
	return x > y;
}
int main (){
	freopen ("B-small-attempt0.in", "r", stdin);
	freopen ("B-small-attempt0.out", "w", stdout);
	scanf("%d", &T);
	for (int i = 1; i <= T; i++){
		scanf("%d %d", &N, &P);
		for (int j = 0; j < N; j++)
			scanf("%d", &R[j]);
		for (int j = 0; j < N; j++){
			for (int k = 0; k < P; k++)
				scanf("%d", &Q[j][k]);
			sort(Q[j], Q[j] + P, compare);
		}
		large = 0;
		for (int j = 0; j < N; j++){
			for (int k = 0; k < P; k++){
				upper[j][k] = (int) (Q[j][k] / (0.9 * R[j]));
				lower[j][k] = (int) ((Q[j][k] - 0.00000001) / (1.1 * R[j])) + 1;
				if (large < upper[j][k])
					large = upper[j][k];
			}
		}
		ans = 0;
		for (int j = 0; j < N; j++)
			point[j] = 0;
		for (int j = large; j >= 1; j--){
			checker = true;
			for (int k = 0; k < N; k++){
				if (point[k] >= P)
					checker = false;
			}
			if (checker){
				for (int k = 0; k < N; k++){
					if (j > upper[k][point[k]]){
						checker = false;
						k = N;
					} else if (j < lower[k][point[k]]){
						checker = false;
						point[k]++;
						k = N;
						j++;
					}
				}
				if (checker){
					ans++;
					for (int k = 0; k < N; k++)
						point[k]++;
					j++;
				}
			}
		}
		printf("Case #%d: %d\n", i, ans);
	}
	fclose (stdin);
	fclose (stdout);
	return 0;
}
