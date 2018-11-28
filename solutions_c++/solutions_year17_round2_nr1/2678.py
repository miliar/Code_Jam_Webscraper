#include<stdio.h>

int main(){
	freopen("A_input.txt","r",stdin);
	freopen("A_output.txt","w",stdout);

	int T;
	scanf("%d",&T);
	for( int i = 0; i < T; ++i ){
		int D, N;
		scanf("%d %d",&D,&N);
		double max = -1;
		for( int j = 0; j < N; ++j ){
			int K, S;
			double result;
			scanf("%d %d",&K,&S);
			result = ((double)(D-K))/((double)S);
			if( result > max ){
				max = result;
			}
		}
		if( max == -1 ){
			printf("Case #%d: %f\n",i+1,D );
		} else {
			printf("Case #%d: %f\n",i+1,D/max );
		}
	}
	return 0;
}
