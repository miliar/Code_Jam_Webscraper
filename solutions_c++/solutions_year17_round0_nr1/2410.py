
#include<bits/stdc++.h>
using namespace std;
#define MAX		1000

char str[MAX+5];

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout); 
	
	int i, j, k, t, cs, n, cnt;
	
	scanf("%d", &t);
	for(cs = 1; cs <= t; cs++)
	{
		scanf("%s %d", str + 1, &k); 
		n = strlen(str + 1);
		cnt = 0;
		
		for(i = 1; i <= n; i++)
		{
			if(str[i] == '-' && i + k - 1 <= n)
			{
				for(j = i; j <= i + k - 1; j++)
					if(str[j] == '-') str[j] = '+';
					else str[j] = '-';
					cnt++; 
			}
		}
		
		printf("Case #%d: ", cs);
		for(i = 1; i <= n; i++) 
			if(str[i] == '-') 
			{
				puts("IMPOSSIBLE");
				break;
			}
		if(i == n + 1) printf("%d\n", cnt);
	}
	return 0;
}
