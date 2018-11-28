#include<cstdio>
#include <cstdlib>
#include <string.h>
using namespace std;
char in[100],now[100];
void solve(){
	scanf("%s",in);
	int len = strlen(in),i;
	for(i = 0 ;i < len ;i++){
		if(in[i]>in[i+1])break;
	}
	if(i == len-1){
		puts(in);
		return;
	}
	while(1){
		if(i==0){
			if(in[i] != '1')printf("%c",in[i]-1);
			for(int i = 1 ;i <len ;i++)printf("9");
			puts("");
			break;
		}
		if(in[i]-1>=in[i-1]){
			for(int j = 0 ;j < i ;j++)printf("%c",in[j]);
			printf("%c",in[i++]-1);
			for(;i < len ; i++)printf("9");
			puts("");
			break;
		}
		i--;
	}

}
int main(){
	int T;
	scanf("%d",&T);
	for(int i = 1 ; i <= T ;i++){
		printf("Case #%d: ",i);
		solve();
	}
}
