#include <cstdio>
#include <cstring>
int T;
char str[50];
int num[50];
void output(int num[], int len){
	int nonzero=0;
		
	for(int i=0;i<len;i++){
		if(num[i]!=0)nonzero=1;
		if(nonzero)printf("%d", num[i]);
	}
	puts("");
}
int main(){
	int ca=0;
	scanf("%d ", &T);
	while(T--){
		scanf("%s", str);
		int len=strlen(str), i, j;
		// if(len==1){printf("Case #%d: %s\n", ++ca, str); continue;}
		// puts(str);
		for(i=0;i<len;i++){
			num[i]=str[i]-'0';
		}

		int big=-1;
		int pre=num[0];
		for(i=1;i<len;i++){
			if(num[i]<pre){
				big=i;
				break;
			}
			pre=num[i];
			
		}
		// printf("i = %d\n", i);
		for(j=big;j<len;j++)num[j]=9;

		num[big-1]-=1; // nonzero
		// printf("%d ? %d\n", num[i-1], num[i]);
		// output(num, len);
		for(j=big-1; j>0 && num[j-1]>num[j]; j--){
			// num[j]=num[j]?(num[j]-1):9;
			// printf("num[%d] = %d, num[%d]= %d\n", j, num[j], j+1, num[j+1]);
			num[j]=9;
			num[j-1]-=1;
		}
		// if(j!=i-1)
		// 	num[j]-=1;
		// printf("j = %d\n", j);
		// num[j+1]-=1;
		
		printf("Case #%d: ", ++ca);
		if(big<0 || len ==1 )puts(str);
		else output(num, len);

	}
	return 0;
}