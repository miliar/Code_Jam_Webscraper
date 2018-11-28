#include <stdio.h>
#include <string.h>

char s[100];
int t;
int c;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output2.txt","w",stdout);
	scanf("%d",&t);
	while(c++<t){
		scanf("%s",s);
		int len = strlen(s);
		int j = 0;
		while(j++<20){
			bool flag = false;
			for(int i = 1; i < len; i++){
				if(flag){
					s[i] = '9';
					continue;
				}
				if(s[i] >= s[i-1]) continue;
				else{
					s[i-1]--;
					s[i] = '9';
					flag = true;
				}
			}
		}
		if(s[0]=='0') printf("Case #%d: %s\n", c, s+1);
		else printf("Case #%d: %s\n", c, s);
	}
}