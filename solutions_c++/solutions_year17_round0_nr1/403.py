#include <cstdio>
#include <cmath>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

char s[1005];

int main(){
	int T, K;
	scanf("%d", &T);
	for(int t=1;t<=T;t++){
		scanf("%s", s);
		scanf("%d", &K);

		int ans = 0;
		for(int i=0;i<=strlen(s)-K;i++){
			if(s[i] == '-'){
				ans++;
				for(int j=i;j<i+K;j++){
					if(s[j] == '-') s[j] = '+';
					else if(s[j] == '+') s[j] = '-';
				}
			}
		}

		bool ok = 1;
		for(int i=0;i<strlen(s);i++){
			if(s[i] == '-'){
				ok = 0;
				break;
			}
		}

		printf("Case #%d: ", t);
		if(ok) printf("%d", ans);
		else printf("IMPOSSIBLE");
		printf("\n");
	}
}