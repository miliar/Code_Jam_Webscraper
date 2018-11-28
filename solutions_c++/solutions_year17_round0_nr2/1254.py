#include <bits/stdc++.h>

using namespace std;

int t,i,j;
char s[105];

int main(){
	
	freopen("B-large (3).in", "r", stdin);
	freopen("judge.out", "w", stdout);
	
	scanf("%d", &t);
	
	for(int tc = 1; tc <= t; tc++){
		scanf("%s", s);
		
		int l = strlen(s);
	
		while(true){
			int before = -1;
			for(i = 0; i < l; i++){
				int num = s[i] - '0';
				if(num < before){
					for(j = i; j < l; j++)
					s[j] = '9';
					s[i - 1]--;
					break;
				}
				before = num;
			}
			if(i == l)
			break;
		}
		
		printf("Case #%d: ", tc);
		
		bool ok = 0;
		for(i = 0; i < l; i++){
			if(s[i] != '0')
			ok = 1;
			if(ok)
			printf("%c", s[i]);
		}
		printf("\n");
	}
}

