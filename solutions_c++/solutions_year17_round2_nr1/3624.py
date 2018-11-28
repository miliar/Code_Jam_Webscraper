#include<cstdio>
#include<iostream>
#include<cstring>

int main(){
	long K_i, S_i, D, N, T;
        float maxT ,t;
	scanf("%d",&T);
	for(int i=0;i<T;i++){
		maxT=0;
		scanf("%d %d", &D, &N);
		for(int j=0;j<N;j++){
		  scanf("%d %d", &K_i, &S_i);
                  t=1.0*(D-K_i)/S_i;
                  if(maxT < t)maxT=t;
		}
                printf("Case #%d: %.7f\n", i+1, D/maxT);
	}
	return(0);
}

