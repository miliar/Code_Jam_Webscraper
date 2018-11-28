#include<stdio.h>
#include<string.h>
#include<stdbool.h>
#include<deque>
#include<stdlib.h>
char S[1001];
int main(){
	FILE *fin = fopen("A-large.in","r");
	FILE *fout = fopen("out","w");
	int T;
	fscanf(fin,"%d",&T);
	fprintf(stdout,"%d\n",T);
	for(int xx=1;xx<=T;xx++){
		int k;
		fscanf(fin,"%s%d",S,&k);
		fprintf(stdout,"%s %d\t\t",S,k);
		int count=0,len=strlen(S);
		for(int c=0;c<=len-k;c++)
			if(S[c] == '-'){
				count ++;
				for(int i=0;i<k;i++){
					if(S[i+c] == '-')
						S[i+c] = '+';
					else
						S[i+c] = '-';
				}
			}
		bool ok=true;
		for(int i=len-k;i<len;i++){
			if(S[i]=='-'){
				ok=false;
			}
		}
		if(!ok){
			fprintf(fout,"Case #%d: IMPOSSIBLE\n",xx);
			fprintf(stdout,"Case #%d: IMPOSSIBLE\n",xx);
		}else{
			fprintf(fout,"Case #%d: %d\n",xx,count);
			fprintf(stdout,"Case #%d: %d\n",xx,count);
		}
	}
	return 0;
}

/*

*/
