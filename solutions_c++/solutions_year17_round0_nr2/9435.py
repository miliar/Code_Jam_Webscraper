#include<cstdio>
#include<memory.h>
#include<cstring>

using namespace std;

int main(void){
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T,i,temp;
	scanf("%d",&T);
	char input[21];
	for(int loop=0;loop<T;loop++){
		printf("Case #%d: ",loop+1);
		memset(input,0,sizeof(input));
		scanf("%s",&input);
		for(i=1;i<strlen(input);i++){
			if(input[i]<input[i-1]) break;
		}//for
		temp=i;
		for(;i<strlen(input);i++) input[i]='9';
		for(i=temp-1;i>=0;i--){
			if(strlen(input)==1) continue;
			if(i==strlen(input)-1) break;
			input[i]--;
			if(input[i]>=input[i-1] || i==0) break;
			input[i]='9';
		}//for
		if(input[0]=='0') input[0]='0'-1;
		for(i=0;i<strlen(input);i++){
			if(input[i]=='0'-1) continue;
			printf("%c",input[i]);
		}//for
		printf("\n");
	}//for
	return 0;
}//main
