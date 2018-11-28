#include<stdio.h>
#include<string.h>
#include<stdbool.h>
#include<stdlib.h>
char S[100];
int len;
bool check(int top){
	//printf("check %d\n",top);
	for(int i=top;i<len;i++){
		if(S[i]<S[top])
			return false;
		else if(S[i]>S[top])
			return true;
	}
	return true;
} 
void r(int top,bool QQ){
	//printf("r %d %d\n",top,QQ);
	if(top == len)
		return ;
	if(QQ){
		S[top] = '9';
		r(top+1,QQ);
		return ;
	}
	if(check(top)){
		r(top+1,QQ);
	}else{
		S[top] --;
		r(top+1,true); 
	}
}
int main(){
	FILE *fin = fopen("B-large.in","r");
	FILE *fout = fopen("ou","w");
	int T;
	fscanf(stdin,"%d",&T);
	fprintf(stdout,"%d\n",T);
	for(int xx=1;xx<=T;xx++){
		fscanf(stdin,"%s",S);
		//fprintf(stdout,"%s",S);
		len =strlen(S);
		r(0,false);
		fprintf(fout,"Case #%d: %s\n",xx,S[0]=='0'?S+1:S);
		fprintf(stdout,"Case #%d: %s\n",xx,S[0]=='0'?S+1:S);
		//system("pause");
	}
	return 0;
}

/*

*/
