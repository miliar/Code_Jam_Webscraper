#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>

using namespace std;

char data[2000];
int k;

int main(){
	int t;
	scanf("%d",&t);
	for(int co=1;co<=t;co++){
		scanf("%s %d",data,&k);
		int len = strlen(data);
		int ans = 0;
		for(int g=0;g<len-k+1;g++){
			if(data[g]=='-'){
				for(int h=g;h<g+k;h++){
					data[h] = (data[h] == '-') ? '+' : '-';
				}
				ans++;
			}
		}
		for(int g=0;g<len;g++){
			if(data[g] == '-'){
				printf("Case #%d: IMPOSSIBLE\n", co);
				break;
			}
			if(g==len-1){
				printf("Case #%d: %d\n", co,ans);
			}
		}
	}

}