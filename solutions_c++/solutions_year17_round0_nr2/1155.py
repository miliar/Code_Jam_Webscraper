#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main(){
	int T,I;
	scanf("%d",&T);
	for(I=1;I<=T;I++){
		char s[30];
		scanf("%s",s);
		printf("Case #%d: ",I);
		int n[30],i,j,l=strlen(s);
		for(i=0;i<l;i++){
			n[i]=(int)(s[i]-'0');
		}
		int t=0;
		while(t==0){
			t=1;
			for(i=0;i<l-1;i++){
				if(n[i]>n[i+1]){
					t=0;
					n[i]--;
					for(j=i+1;j<l;j++){
						n[j]=9;
					}
					break;
				}
			}
		}
		for(i=0;i<l;i++)if(n[i]>0)break;
		for(;i<l;i++)printf("%d",n[i]);
		printf("\n");
	}
	return 0;
}