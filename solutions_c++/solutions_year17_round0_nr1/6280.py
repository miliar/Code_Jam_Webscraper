#include <cstdio>
#include <cstring>

using namespace std;

int main() {

	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for (int t = 0; t < T; ++t)
	{
		char S[1001];
		scanf("%s",S);
		int n = strlen(S);
		int K;
		scanf("%d",&K);	
		int ans = 0;
		for (int i = 0; i <= n - K; ++i)
			{
				if(S[i] == '+') continue;
				++ans;
				for (int j = i; j < i + K; ++j)
				{
					if(S[j] == '+') 
						S[j] = '-';
					else
						S[j] = '+';
				}

			}
			bool clr = 1;
		for (int i = 0; i < n; ++i)
				{
					if(S[i] == '-') {
						clr = 0;
						break;
					}
				}
		(clr)?printf("Case #%d: %d\n",t+1,ans ):printf("Case #%d: IMPOSSIBLE\n",t+1 );				
	}
	return 0;
}