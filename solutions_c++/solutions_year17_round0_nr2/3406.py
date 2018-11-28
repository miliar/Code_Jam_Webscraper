#include<iostream>
#include<string.h>
#include<stdio.h>

using namespace std;
int T;
void Gao(){
	scanf("%d",&T);
	for(int k= 1;k<=T;k++){
		char tem[30];
		int before[30];
		scanf("%s",tem);
		int l = strlen(tem);
		for(int i=0;i<l;i++){
			before[i] = tem[i]-'0';
		}
		if(l!=1){
			bool hasReverse = false;
			int stReverse = -1;
			for(int i=1;i<l;i++){
				if(before[i]<before[i-1]){
					hasReverse = true;
					stReverse = i;
					break;
				}
			}
			if(hasReverse){
				for(int i=l-1;i>=0;i--){
					if(before[i]>before[i+1]){
						before[i]-=1;
						for(int j=i+1;j<l;j++){
							before[j]=9;
						}
					}
				}
			}
			printf("Case #%d: ",k);
			for(int i =0;i<l;i++){
				if(before[i]!=0){
					printf("%d",before[i]);
				}
			}
			printf("\n");
		}else{
			printf("Case #%d: ",k);
			for(int i =0;i<l;i++){
				printf("%d",before[i]);
			}
			printf("\n");
		}
	}
}
int main(){
	freopen("B-large.in","r",stdin);
	freopen("b-large.out","w",stdout);
	Gao();	
}

