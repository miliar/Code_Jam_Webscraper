#include <stdio.h>
int N;
long long X;
long long Ans;
long long Mul;
int i;
int dgts[25];
int dgln;
int j;
int prev;
int k;
int main(){
	freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
	scanf("%d", &N);
	i = 0;
	while (i < N){
		scanf("%lld", &X);
		dgln = 0;
		while (X > 0){
			dgts[dgln] = X % 10;
			X = X / 10;
			dgln++;
		}
		prev = dgts[dgln-1];
		j = dgln-2;
		while (j > -1){
			if (dgts[j] < prev){
				k = j+1;
				while (k!= dgln && dgts[k] == dgts[j+1]){
					k++;
				}
				k = k-1;
				dgts[k] -= 1;
				while (k!= -1){
					k--;
					dgts[k] = 9;
				}
				break;
			}
			prev = dgts[j];
			j--;
		}
		if (dgln == 1){
			printf("Case #%d: %d\n", i+1, dgts[0]);
		}
		else{
			Ans = 0;
			Mul = 1;
			k = 0;
			while (k < dgln){
				Ans += dgts[k]*Mul;
				Mul = Mul * 10;
				k++;
			}
			printf("Case #%d: %lld\n", i+1, Ans);
		}
		i++;
	}
}
