#include<bits/stdc++.h>
using namespace std;

int main(){
	int T; scanf("%d",&T);
	for(int cs=0; cs<T; cs++){
		char s[100];
		scanf("%s", &s);
		
		int len = strlen(s);
		
		int idx = 0;
		for(int i = 1; i < len; i++){
			if (s[i] < s[i-1]){
				s[idx]--;
				for(int j = idx + 1; j < len; j++){
					s[j] = '9';
				}
				break;
			}
			if (s[i] > s[i-1]) idx = i;
		}
		
		printf("Case #%d: ", cs + 1);
		int print = 0;
		for(int i = 0; i < len; i++){
			if (!print && s[i] == '0') continue;
			print = 1;
			putchar(s[i]);
		}
		puts("");
	}
}