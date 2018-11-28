#include <stdio.h>
#include <string.h>

int main(){
	int T,min;
	scanf("%d",&T);
	char N[40];
	for(int c1=0;c1<T;++c1){
		min=10;
		scanf("%s",N);
		for(int c2=strlen(N)-1;c2>=0;--c2){
			if(min>=N[c2]-48)min=N[c2]-48;
			else{
				for(int c3=c2+1;c3<strlen(N) && N[c3]-48<9;c3++)N[c3]=57;
				--N[c2];
				min=N[c2]-48;
			}
		}
		printf("Case #%d: ",c1+1);
		int c2;
		for(c2=0;c2<strlen(N) && (N[c2]-48)==0;++c2);
		for(;c2<strlen(N);c2++)printf("%c",N[c2]);
		printf("\n");		
	}
	return 0;
}
