#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>

using namespace std;

int T;

char s[20];



int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	cin >> T;
	int cas = 0;
	while(T--){
		scanf("%s",s + 1);
		int n = strlen(s + 1);
		for(int i = 1;i < n;i++){
			if(s[i] > s[i + 1]){
				if(s[i] != '0'){
					s[i] = s[i] - 1;
				}else s[i] = '9';
				for(int j = i + 1;j <= n;j++){
					s[j] = '9';
				}
				for(int j = i;j > 1;j--){
					if(s[j] < s[j - 1]){
						if(s[j - 1] != '0'){
							s[j - 1] = s[j - 1] - 1;
						}else s[j - 1] = '9';
						for(int k = j;k <= n;k++){
							s[k] = '9';
						}
					}
				}
				break;
			}
		}
		printf("Case #%d: ",++cas);
		bool flag = false;
		for(int i = 1;i <= n;i++){
			if(s[i] == '0'){
				if(flag) putchar(s[i]);
			}else{
				flag = true;
				putchar(s[i]);
			}
		}
		puts("");
	}
	return 0;
}
