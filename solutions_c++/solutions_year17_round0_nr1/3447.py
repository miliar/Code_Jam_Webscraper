#include<iostream> 
#include<stdio.h>
#include<string.h>
using namespace std;

int T;

void Gao(){
	scanf("%d",&T);
	for(int k=1;k<=T;k++){
		char a[1100];
		int ans =0;
		int Ok = true;
		int len = 0;
		scanf("%s",a);
		scanf("%d",&len);
		int l = strlen(a);
		for(int i=0;i<l;i++){
			if(a[i]=='+'){
				continue;
			}
			else if(a[i]=='-'){
				if(i+len<=l){
					ans++;
					for(int j=i;j<i+len;j++){
						if(a[j]=='+'){
							a[j]= '-';
						}else if (a[j]=='-'){
							a[j] = '+';
						}
					}
				}	
			}
		}
		for(int i=0;i<l;i++){
			if(a[i]!='+'){
				ans = -1;
			}
		}
		printf("Case #%d: ",k);
		if(ans ==-1){
			printf("IMPOSSIBLE\n");
		}else{
			printf("%d\n",ans);
		}
	}
}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("aoutlarge.txt","w",stdout);
	Gao();
}
