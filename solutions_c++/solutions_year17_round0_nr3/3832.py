#include<stdio.h>
#include<string.h>
#include<stdbool.h>
#include<stdlib.h>
#include<queue>
int main(){
	FILE *fin = fopen("C-small-2-attempt0.in","r");
	FILE *fout = fopen("ou","w");
	int T;
	fscanf(fin,"%d",&T);
	//fprintf(stdout,"%d\n",T);
	for(int xx=1;xx<=T;xx++){
		int k,n;
		fscanf(fin,"%d%d",&n,&k);
		//fprintf(stdout,"%s",S);
		std::priority_queue<int> Q;
		while(!Q.empty())	Q.pop();
		Q.push(n);
		int t;
		for(int i=0;i<k;i++){
			t = Q.top();
		//	printf("Q.pop %d\n",t);
			Q.pop();
			if(t&1){
		//		printf("push %d\n",t/2);
		//		printf("push %d\n",t/2);
				Q.push(t/2);
				Q.push(t/2);
			}else{
		//		printf("push %d\n",t/2);
		//		printf("push %d\n",t/2-1);
				Q.push(t/2);
				Q.push(t/2-1);
			}
		} 
		fprintf(fout,"Case #%d: %d %d\n",xx,t/2,(t&1?t/2:t/2-1));
		fprintf(stdout,"Case #%d: %d %d\n",xx,t/2,(t&1?t/2:t/2-1));
		//system("pause");
	}
	return 0;
}

/*

*/
