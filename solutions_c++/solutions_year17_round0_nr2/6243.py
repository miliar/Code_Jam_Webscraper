#include <cstdio>
#include <cstring>

using namespace std;

int main() {

	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for (int t = 0; t < T; ++t)
	{
		char S[1001];
		scanf("%s",S);
		int n = strlen(S);
		if(n == 1) {
		printf("Case #%d: %s\n",t+1,S );
		continue;				
		}
	int idx = 0;
	while(idx < n - 1) {
		if(S[idx] > S[idx + 1]) break;
		++idx;
	}
	if(idx == n - 1) {
		printf("Case #%d: %s\n",t+1,S );
		continue;	
	}
	while(1) {
		for (int i = idx + 1; i < n; ++i)
		{
			S[i] = '9';
		}
		S[idx] = S[idx] - 1;
		if(idx == 0) break;
		if(S[idx] >= S[idx - 1]) break;
		--idx;
	}
	if (S[0] == '0')
	{
		for (int i = 0; i < n - 1; ++i)
		{
			S[i] = S[i + 1];
		}
		S[n - 1] = '\0';
	}
	printf("Case #%d: %s\n",t+1,S );
	}
	return 0;
}