#include <bits/stdc++.h>
#define time fucktime
int a, b, d[2222][2222][3][3], time[2222];
void Main(){
	scanf("%d%d", &a, &b);
	memset(time, 0, sizeof time);
	for (; a -- ; ){
		int t1, t2;
		scanf("%d%d", &t1, &t2);
		for (int i = t1; i < t2; i ++ )
			time[i] = 1;
	}
	for (; b -- ; ){
		int t1, t2;
		scanf("%d%d", &t1, &t2);
		for (int i = t1; i < t2; i ++ )
			time[i] = 2;
	}
	memset(d, 63, sizeof d);
	d[0][0][2][2] = d[0][0][1][1] = 0;
	for (int i = 0; i < 24 * 60; i ++ )
		for (int j = 0; j <= 12 * 60; j ++ )
			for (int k = 1; k <= 2; k ++ )
				for (int l = 1; l <= 2; l ++ ){
					int D = d[i][j][k][l];
					//if (D < 99999) printf("%d %d %d %d %d\n", i,j,k,l,D);
					if (k == 1){
						if (j != 12 * 60 && time[i] != 2){
							if (d[i + 1][j + 1][1][l] > D)
								d[i + 1][j + 1][1][l] = D;
						}
						if (i - j < 12 * 60 && time[i] != 1){
							if (d[i + 1][j][2][l] > D + 1)
								d[i + 1][j][2][l] = D + 1;
						}
					}
					else{
						if (j != 12 * 60 && time[i] != 2){
							if (d[i + 1][j + 1][1][l] > D + 1)
								d[i + 1][j + 1][1][l] = D + 1;
						}
						if (i - j < 12 * 60 && time[i] != 1){
							if (d[i + 1][j][2][l] > D)
								d[i + 1][j][2][l] = D;
						}
					}
				}
	int res = 111111;
	for (int k = 1; k <= 2; k ++ )
		for (int l = 1; l <= 2; l ++ ){
			if (k != l) d[24 * 60][12 * 60][k][l] ++ ;
			if (res > d[24 * 60][12 * 60][k][l])
				res = d[24 * 60][12 * 60][k][l];
			//printf("%d %d %d\n", k, l, d[24 * 60][12 * 60][k][l]);
		}
	printf("%d\n", res);
}
int main(){
	freopen("t.out","w",stdout);
	int _;
	scanf("%d", &_);
	for (int i = 1; i <= _; i ++ ){
		printf("Case #%d: ", i);
		Main();
	}
}
