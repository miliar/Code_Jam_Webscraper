#include <cstdio>
int T;
int N, R, O, Y, G, B, V;
int main (){
	freopen ("B-small-attempt0.in", "r", stdin);
	freopen ("B-small-attempt0.out", "w", stdout);
	scanf("%d", &T);
	for (int i = 1; i <= T; i++){
		scanf("%d %d %d %d %d %d %d", &N, &R, &O, &Y, &G, &B, &V);
		printf("Case #%d: ", i);
		if (O == 0 && G == 0 && V == 0){
			if (R >= Y && R >= B){
				if (R > Y + B)
					printf("IMPOSSIBLE");
				else {
					while (R < Y + B){
						if (R > 0){
							printf("R");
							R--;
						}
						if (Y > 0){
							printf("Y");
							Y--;
						}
						if (B > 0){
							printf("B");
							B--;
						}
					}
					for (int i = 0; i < Y; i++)
						printf("RY");
					for (int i = 0; i < B; i++)
						printf("RB");
				}
			} else if (Y >= R && Y >= B){
				if (Y > R + B)
					printf("IMPOSSIBLE");
				else {
					while (Y < R + B){
						if (Y > 0){
							printf("Y");
							Y--;
						}
						if (R > 0){
							printf("R");
							R--;
						}
						if (B > 0){
							printf("B");
							B--;
						}
					}
					for (int i = 0; i < R; i++)
						printf("YR");
					for (int i = 0; i < B; i++)
						printf("YB");
				}
			} else {
				if (B > R + Y)
					printf("IMPOSSIBLE");
				else {
					while (B < R + Y){
						if (B > 0){
							printf("B");
							B--;
						}
						if (R > 0){
							printf("R");
							R--;
						}
						if (Y > 0){
							printf("Y");
							Y--;
						}
					}
					for (int i = 0; i < R; i++)
						printf("BR");
					for (int i = 0; i < Y; i++)
						printf("BY");
				}
			}
		}
		printf("\n");
	}
	fclose (stdin);
	fclose (stdout);
	return 0;
}
