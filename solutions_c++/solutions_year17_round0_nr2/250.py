#include <stdio.h>

int s[60];

int main(){
	int t;
	scanf("%d",&t);
	for(int tt=1;tt<=t;tt++){
		char c;
		scanf(" %c",&c);
		int n=0;
		while('0'<=c && c<='9'){
			s[n]=c-'0';
			n++;
			scanf("%c",&c);
		}
		for(int i=n-2;i>=0;i--){
			if(s[i]>s[i+1]){
				s[i]--;
				for(int j=i+1;j<n;j++) s[j]=9;
			}
		}
		printf("Case #%d: ",tt);
		for(int i=0;i<n;i++) if(s[i]!=0) printf("%d",s[i]);
		printf("\n");
	}
	return 0;
}
