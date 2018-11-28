#include <bits/stdc++.h>

#define INF 0x3f3f3f3f
#define NINF -0x3f3f3f3f

using namespace std;

typedef pair<int,int> pii;

char str[1005];
char plus_ultra[1005];

void solve ()
{
	int k;
	scanf("%s %d",str,&k);
	
	int len = strlen(str);
	
	for (int i = 0; i < len; i += 1)
	{
		if (str[i] == '+')
			str[i] = 0;
		else
			str[i] = 1;
			
		plus_ultra[i] = 0;
	}
	
	int ans = 0;
	for (int i = 0; i <= len-k; i += 1)
	{
		if (plus_ultra[i] != str[i])
		{
			for (int j = 0; j < k; j += 1)
			{
				plus_ultra[i+j] = 1-plus_ultra[i+j];
			}
			
			++ans;
		}
	}
	
	bool valid = true;
	for (int i = 0; i < len; i += 1)
	{
		if (plus_ultra[i] != str[i])
		{
			valid =false;
			break;
		}
	}
	
	if (!valid)
		printf("IMPOSSIBLE\n");
	else
		printf("%d\n",ans);
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
