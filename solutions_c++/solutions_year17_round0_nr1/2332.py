#include <stdio.h> 
#include <string.h>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long ll;
int w, h;
int t;
int n, k, L;

int min(int a, int b)
{
	if (a > b)return b;
	return a;
}
int max(int a, int b)
{
	if (a > b)return a;
	return b;
}
int abs(int a)
{
	if(a>0)return a;
	return -a;
}

const int MAXN = 1005;

char c[MAXN];
int a[MAXN];




int main()
{ 
	int tc, i;
	freopen("alarge.txt","r",stdin);
	freopen("alargeoutput.txt","w",stdout);

	scanf("%d",&tc);

	for(int t=1;t<=tc;t++)
	{
		scanf("%s",c);
		scanf("%d",&k);

		L = strlen(c);
		
		int state=0;

		for(int i=0;c[i];i++)
		{
			if(c[i]=='+')
				a[i] = 1;
			else
				a[i] = 0;
		}

		int ret = 0;
		for(int i=0;i+k<=L;i++)
		{
			if(a[i]==0)
			{
				ret++;
				for(int j=i;j<i+k;j++)
					a[j] ^= 1;
			}
		}

		int wrong=0;
		for(int i=0;i<L;i++)
		{
			if(a[i]==0)
			{
				wrong=1;
			}
		}

		if(wrong == 0)
		{
			printf("Case #%d: %d\n",t, ret);
		}
		else
			printf("Case #%d: IMPOSSIBLE\n", t);
		
	}

	return 0;
}


