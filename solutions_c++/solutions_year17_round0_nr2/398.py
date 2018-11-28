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
string ans = "";

int main(){
	int T;
	scanf("%d", &T);
	for(int t=1;t<=T;t++){
		scanf("%s", s);
		printf("Case #%d: ", t);

		ans = "";
		for(int i=strlen(s)-1;i>=1;i--){
			if(s[i-1] > s[i]){
				for(int j=i;j<strlen(s);j++) s[j] = '9';
				bool zero = 1;
				s[i-1]--;
			}
		}

		bool ok = 0;
		for(int i=0;i<strlen(s);i++){
			if(s[i] != '0') ok = 1;
			if(ok) ans += s[i];
		}
		cout << ans << endl;
	}
}