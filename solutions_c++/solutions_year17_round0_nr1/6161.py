#include<iostream>
#include<stdio.h>
#include<math.h>
#include<string.h>
#include<cstring>
#include<map>
#include<algorithm>
#include<vector>
#include<stdlib.h>
#include<stack>
 
using namespace std;
 
#define MEM(v,i) memset(v,i,sizeof(v))

int main(){
	int test = 0;
	int N = 0, i = 0, j  = 0, K = 0,count = 0, flag = true;
	string s;
	scanf("%d",&test);
	for(int xtest = 1; xtest<=test; xtest++){
		printf("Case #%d: ",xtest);
		cin>>s;
		scanf(" %d",&K);
		N = s.length();
		flag = true;
		count = 0;
		for(i = 0; i<N&&flag==true; i++){
			for(;i<N && s[i]=='+';i++);
			if(i<N && s[i]=='-'){
				if(i+K-1<N){
					count++;
					for(j = i; j-i<K;j++){
						if(s[j]=='-') s[j]='+';
						else if(s[j]=='+') s[j] = '-';
					}
				}
				else flag = false;
			}
			if(i==N){break;}
		}
		if(flag==true)printf("%d\n",count);
		else printf("IMPOSSIBLE\n");
	}
	return(0);
}