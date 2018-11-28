#include <stdio.h>
#include <string.h>

char s[1050];
int t;
int ans = 0;
int len = 0;
int k;


int main(){
	freopen("input.txt","r",stdin);
	freopen("output1.txt", "w", stdout);
	scanf("%d",&t);
	int c = 0;
	while(c++<t){
		scanf("%s",s);
		scanf("%d",&k);
		len = strlen(s);
		bool flag = true;
		for(int i = 0; i < len; i++){
			if(s[i]=='+') continue;
			ans++;
			for(int j = 0; j < k; j++){
				if(i+j >= len){
					flag = false;
					break;
				}
				if(s[i+j] == '+') s[i+j] = '-';
				else s[i+j] = '+';
			}
		}
		if(flag) printf("Case #%d: %d\n",c, ans);
		else printf("Case #%d: IMPOSSIBLE\n", c);
		ans = len = 0;
	}
}