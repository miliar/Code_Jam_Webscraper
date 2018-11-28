/*************************************************************************
    > File Name: B.cpp
    > Author: milaso
    > Mail: 562058113@qq.com 
    > Created Time: 六  4/ 8 16:18:58 2017
 ************************************************************************/

#include<iostream>
#include<math.h>
#include<algorithm>
#include<string.h>
#include<string>
#include<stdio.h>
#include<fstream>
using namespace std;


char Num[20];

int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		printf("Case #%d: ",t);
		scanf("%s",Num);
		int l = strlen(Num);
		int now = Num[0];
		int i;
		for(i = 1;i < l;i++){
			if(Num[i] < now)
				break;
			now = Num[i];
		}
		if(i == l){
			printf("%s",Num);
		}
		else{
			if(now == '1'){
				l--;
				for(int j=0;j<l;j++)
					printf("9");
			}
			else{
				int m = i-1;
				Num[m] --;
				while(m--){
					if(Num[m]>Num[m+1]){
						Num[m] -- ;
						i = m+1;
					}
				}
				for(;i<l;i++)
					Num[i] = '9';
				printf("%s",Num);
			}
		}
		printf("\n");
	}
	return 0;
}
