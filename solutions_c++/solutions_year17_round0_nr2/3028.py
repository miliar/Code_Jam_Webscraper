#include <bits/stdc++.h>
using namespace std;

void solve()
{
	char input[100];
	scanf("%s", input);
	int ind = strlen(input) - 1;
	while(ind > 0)
	{
		if(input[ind-1] > input[ind])
		{
			--input[ind-1];
			for(int j = ind; j < strlen(input); ++j)
				input[j] = '9';
			
		}
		--ind;
	}
	int start = 0;
	if(input[0] == '0')
		start = 1;
	printf("%s\n", &input[start]);
	
}
int main()
{
	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; ++i)
	{
		printf("Case #%d: ", i);
		solve();
	}
	
	
	return 0;
}
