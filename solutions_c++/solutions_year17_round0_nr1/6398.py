/************************************************************************
    > File Name: A.cpp
    > Author: milaso
    > Mail: 562058113@qq.com 
    > Created Time: 六  4/ 8 12:40:16 2017
 ************************************************************************/

#include<iostream>
#include<math.h>
#include<algorithm>
#include<string.h>
#include<string>
#include<stdio.h>
#include<fstream>
using namespace std;

char S[2000];
int flat[2000];
int ck[2000];

int main(){
	int T;
	scanf("%d",&T);
	for(int i=0;i<T;i++){
		int K;
		memset(flat,0,sizeof(flat));
		scanf("%s %d",S,&K);
		int l = strlen(S);
		int r = l - K;
		int f = 0;
		int ans = 0;
		for(int j=0;j<l;j++){
			if(S[j] == '+')
				ck[j] = 1;
			else
				ck[j] = 0;
		}
		for(int j=0;j<=r;j++){
			if(j >= K){
				f -= flat[j-K];
			}
			if((ck[j]+f)%2 == 0){
				flat[j] = 1;
				f += 1;
				ans += 1;
			}
		}
		int flag = 0;
		for(int j=1;j<K;j++){
			if(r + j >= K){
				f -= flat[r+j-K];
			}
			if((ck[r+j]+f)%2 == 0)
				flag = 1;
		}
		printf("Case #%d: ",i + 1);
		if(flag){
			printf("IMPOSSIBLE\n");
		}
		else
			printf("%d\n",ans);
	}
	return 0;
}
