#include <stdio.h>
int N;
char C;
int i;
int j;
int k;
bool RS[1005];
int L;
int M;
int Ans;
bool pa;
int main(){
	freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
	scanf("%d", &N);
	i = 0;
	while (i < N){
		Ans = 0;
		scanf("\n");
		C = '.';
		L = 0;
		while (C != ' '){
			scanf("%c", &C);
			if (C == '-'){
				RS[L] = 0;
			}
			else{
				RS[L] = 1;
			}
			L++;
		}
		scanf("%d", &M);
		j = 0;
		while (j < (L-M)){
			if (RS[j] == 0){
				k = j;
				while (k < (j+M)){
					if (RS[k] == 0){
						RS[k] = 1;
					}
					else{
						RS[k] = 0;
					}
					k++;
				}
				Ans++;
			}
			j++;
		}
		printf("Case #%d: ", (i+1));
		j = 0;
		pa = true;
		while (j < L-1){
			if (RS[j] == 0){
				printf("IMPOSSIBLE\n");
				pa = false;
				break;
			}
			j++;
		}
		i++;
		if (pa){
			printf("%d\n", Ans);
		}
	}
}
