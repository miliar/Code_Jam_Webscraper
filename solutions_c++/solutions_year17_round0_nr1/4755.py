#include <stdio.h>
#include <iostream>
#include <string>
#include <bitset>
#include <algorithm>
#define FOR(i,n) for(int (i)=0; (i)<(n); (i)++)
#define SD(x) scanf("%d", &x); 
using namespace std;
int k;
void toStr(int x){
	if(x == 0) return;
	printf("%c", x%2==0 ? '+' : '-');
	toStr(x/2);
}
int solve(string str){
	int ans = 0;
	FOR(i, str.size()-k+1){
		if(str[i] != '+'){ 
			FOR(j, k){
				str[i+j] = str[i+j]=='+' ? '-' : '+'; 
			}
			ans++;
		}
	}
	FOR(i, str.size()){
		if(str[i] != '+') return -1;
	}
	return ans;
}
int  main(){
	int t; SD(t);
	FOR(c, t){
		string str;
		cin >> str;
		SD(k);
		int ans = solve(str);
		if(ans == -1){
			printf("Case #%d: IMPOSSIBLE\n", c+1);
		}
		else printf("Case #%d: %d\n", c+1, ans);
	}
}