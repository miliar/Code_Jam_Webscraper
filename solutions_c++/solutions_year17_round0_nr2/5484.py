#include <stdio.h>
#include <cstring>
#include <algorithm>

using namespace std;


int main()
{
	//freopen("input.txt", "r", stdin);

	int t;
	int id = 1;
	scanf("%d", &t);
	while(t--){
		char s[50];
		memset(s, 0, sizeof(s));
		scanf("%s", &s);
		//printf("%s\n", s);
		int ans = 1;
		int len = 0;
		int anslen = 1;
		for(int i=0; s[i]; i++){
			len = i+1;
		}
		for(int i=1; s[i]; i++){
			if(s[i] < s[i-1]){
				int now = i-1;
				while(now>0 && s[now] == s[now-1]){
					now--;
				}
				//printf("%d\n", now);
				ans = now;
				break;
			}
			else{
				ans = i;
				anslen = i;
			}
		}
		printf("Case #%d: ", id++);
		if(ans==0 && s[0]=='1'){
			for(int i=1; s[i]; i++){
				printf("%d", 9);
			}
			printf("\n");
		}
		else{
			for(int i=0; s[i]; i++){
				if(i<ans){
					printf("%d", s[i]-'0');
				}
				else{
					if(ans+1 == len){
						printf("%d", s[i]-'0');
					}
					else{
						if(i==ans){
							printf("%d", s[i]-1-'0');
						}
						else{
							printf("%d", 9);
						}
					}
				}
			}
			printf("\n");
		}
	}

    return 0;
}
