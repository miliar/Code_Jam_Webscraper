#include <cstdlib>
#include <cstdio>
#include <cstring>

using namespace std;

int main()
{
	int T;
	scanf("%d", &T);
	
	for(int t = 1; t<= T; t++)
	{
		printf("Case #%d: ", t);
		char s[1005];
		scanf("%s", s);
		int k;
		scanf("%d", &k);
		
		int len=strlen(s);
		
		bool ok=true;
		int nb=0;
		for(int i= 0; i < len; i++)
		{
			if(s[i]=='-')
			{
				if(i+k-1 >= len)
				{
					ok=false;
					break;
				}
				nb++;
				for(int j = 0; j < k; j++)
					s[i+j]=(s[i+j]=='-')?'+':'-';
			}
		}
		if(ok)
			printf("%d\n", nb);
		else
			printf("IMPOSSIBLE\n");
	}
	
	return 0;
}

