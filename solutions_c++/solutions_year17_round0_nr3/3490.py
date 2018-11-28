#include <stdio.h>
#include <math.h>

int main(){
	int T;
	scanf("%d",&T);
	for(int t=0; t<T; t++){
		int N,K;
		scanf("%d%d",&N,&K);
        int aa = 1;
        while((1<<aa)-1 <= K){
            aa++;
        }
        int sep = (1<<(aa-1))-1;  // sep<=K
        int bb = (N-sep)/(sep+1);
        int mind,maxd;
        if(K-sep == 0){
            bb = (N-sep/2)/(sep/2+1);
            mind = floor(((double)bb-1)/2);
            maxd = ceil(((double)bb-1)/2);
        }else if(K-sep <= (N-sep)-bb*(sep+1)){
            mind = floor((double)bb/2);
            maxd = ceil((double)bb/2);
        }else{
            mind = floor(((double)bb-1)/2);
            maxd = ceil(((double)bb-1)/2);
            
        }
		printf("Case #%d: %d %d\n",t+1,maxd,mind);
	}
	return 0;
}
