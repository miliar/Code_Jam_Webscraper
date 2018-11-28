#include<iostream>
#include<cstdio>
using namespace std;

int main(){
	int t, k;
	char s[1005];
	scanf("%d", &t);
	for(int tcase=1;tcase<=t;tcase++){
		printf("Case #%d: ", tcase);
		scanf("%s %d", s, &k);
		int l=strlen(s);
		int check=1;
		int cnt=0;
		for(int i=0;i<=l-1;i++){
			if(s[i]=='-'){
				if(i>=l-k+1){
					printf("IMPOSSIBLE\n");
					check=0;
					break;
				}
				else{
					for(int j=0;j<=k-1;j++){
						s[i+j]='+'+'-'-s[i+j];
					}
					cnt++;
				}
			}
		}
		if(check==1){
			printf("%d\n", cnt);
		}
	}
	return 0;
}
					
			
