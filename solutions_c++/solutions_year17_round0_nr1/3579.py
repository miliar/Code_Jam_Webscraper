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

int solve(char* s,int k){
	int n = strlen(s);
	int cnt = 0;
	for(int i = 0;i < n;++i){
		if(s[i] == '+')
			continue;
		if(i + k > n)
			return -1;
		for(int j = 0;j < k;++j)
			s[i + j] = '+' + '-' - s[i + j];
		++cnt;
	}
	return cnt;
}

int main(){
	int T;
	scanf("%d",&T);
	for(int cas = 1;cas <= T;++cas){
		int k;
		scanf("%s%d",&s,&k);
		int ans = solve(s,k);
		if(ans == -1)
			printf("Case #%d: IMPOSSIBLE\n",cas);
		else
			printf("Case #%d: %d\n",cas,ans);
	}
	return 0;
}

