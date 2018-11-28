#include <bits/stdc++.h>

#define INF 0x3f3f3f3f
#define NINF -0x3f3f3f3f

using namespace std;

typedef pair<int,int> pii;

char num[25];

void solve ()
{
	scanf("%s",num);
	
	int len = strlen(num);
	
	int nn = 0;
	for (int i = 0; i < len; i += 1)
	{
		nn = 10*nn + (num[i]-'0');
	}
	
	for (int i = 0; i < len-1; i += 1)
	{
		if (num[i] <= num[i+1])
			continue;
			
		bool change = false;
		for (int j = i+1; j < len; j += 1)
		{
			if (num[j] < num[i])
			{
				change = true;
				break;
			}
		}
		
		if (change)
		{
			bool reset = false;
			for (int j = i; j >= 0; j--)
			{
				num[j]--;
				
				if (num[j] >= '0')
					break;
				
				reset = true;
				num[j] = '9';
			}
			
			for (int j = i+1; j < len; j += 1)
			{
				num[j] = '9';
			}
			
			i = -1;
		}
	}
	
	bool leadingZ = true;
	for (int i = 0; i < len; i += 1)
	{
		if (num[i] == '0' && leadingZ)
			continue;
			
		leadingZ = false;
		printf("%c",num[i]);
	}
	printf("\n");
}

int main (int argc, char const* argv[])
{
	int T;
	scanf("%d",&T);
	
	for (int t = 1; t <= T; t += 1)
	{
		printf("Case #%d: ",t);
		
		solve();	
	}	
	
	return 0;
}
