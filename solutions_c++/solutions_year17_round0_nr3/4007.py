#include<stdio.h>
#include<string.h>
#include<stdbool.h>
#include<stdlib.h>
#include<queue>
#define ULL unsigned long long
ULL ary[100000];
int num[100000],top;
int find(){
	ULL max=ary[0];
	int ch=0;
	int i;
	for(i=1;i<top;i++){
		if(ary[i]>max){
			max = ary[i];
			ch = i;
		}
	}
	return ch;
}
int insert(ULL n,int k){
	//printf("insert %llu,%d\n",n,k); 
	for(int i=0;i<top;i++){
		if(ary[i]==n){
			num[i]+=k;
			return 0;
		}
	}
	ary[top]=n;
	num[top++]=k;
}
void print(){
	for(int i=0;i<top;i++){
		printf("print %d : %llu %d\n",i,ary[i],num[i]);
	}
}
int main(){
	FILE *fin = fopen("C-small-2-attempt0.in","r");
	FILE *fout = fopen("ou2","w");
	ULL T;
	fscanf(fin,"%d",&T);
	//fprintf(stdout,"%d\n",T);
	for(int xx=1;xx<=T;xx++){
		ULL k;
		ULL n;
		fscanf(fin,"%llu%llu",&n,&k);
		//fprintf(stdout,"%s",S);
		ULL t;
		top=1;
		ary[0]=n,num[0]=1;
		while(k){
			int m= find();
			ULL a=ary[m];
			int b=num[m];
		//	printf("find %d %llu %d\n",m,a,b);
			if(k>b){
				k-=b;
			}else{
				t=a;
				break;
			}	
			ary[m] = a/2;
			if(a&1){
				num[m] = b*2;
			}else{
				
				insert((a/2)-1,b);
			}
		//	print();
		//	system("pause");
		}		
		fprintf(fout,"Case #%d: %llu %llu\n",xx,t/2,(t&1?t/2:t/2-1));
		fprintf(stdout,"Case #%d: %llu %llu\n",xx,t/2,(t&1?t/2:t/2-1));
		//system("pause");
	}
	return 0;
}

/*

*/
