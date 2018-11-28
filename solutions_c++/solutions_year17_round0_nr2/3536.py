#include<stdio.h>
#include<string.h>
#include<vector>
#include<queue>
#include<set>
#include<string>
#include<map>

using namespace std;
#define INF 0x3f3f3f3f

typedef long long LL;

char s[1010];

string solve(char* s){
	int n = strlen(s);
	for(int i = 0;i < n - 1;++i){
		if(s[i] <= s[i + 1])
			continue;
		while(i > 0 && s[i - 1] == s[i])
			--i;
		s[i] = s[i] - 1;
		for(int j = i + 1;j < n;++j)
			s[j] = '9';
		break;
	}
	for(int i = 0;i < n;++i)
		if(s[i] != '0')
			return string(s + i);
	return "";
}

int main(){
	int T;
	scanf("%d",&T);
	for(int cas = 1;cas <= T;++cas){
		int k;
		scanf("%s",&s);
		string ans = solve(s);
		printf("Case #%d: %s\n",cas,ans.c_str());
	}
	return 0;
}

