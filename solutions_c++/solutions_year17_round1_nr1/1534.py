#include<cstdio>
#include<vector>
#include<algorithm>

using namespace std;
char cake[26][26];
char change;

void solve(void)
{
	int r, c;
	scanf("%d %d", &c, &r);
	
	for(int i=0; i<c; i++)
	{
		scanf("%s", cake[i]);
	}
	
	for(int i=0; i<c; i++) //오른쪽으로 채우기 
	{
		change = 0;
		for(int j=0; j<r; j++)
		{
			if(cake[i][j] == '?' && change != 0)
			{
				cake[i][j] = change;
			}
			if(cake[i][j] != '?')
			{
				change = cake[i][j];
			}
		}
	}

	for(int i=0; i<c; i++) //왼쪽으로 채우기 
	{
		change = 0;
		for(int j=r-1; j>=0; j--)
		{
			if(cake[i][j] == '?' && change != 0)
			{
				cake[i][j] = change;
			}
			if(cake[i][j] != '?')
			{
				change = cake[i][j];
			}
		}
	}

	for(int i=0; i<c; i++) //빈줄 채우기 
	{
		change = 0;

		if(cake[i][0] == '?')
		{
			for(int j = 0; j<r; j++)
			{
				for(int x = i+1; x<c; x++)
				{
					if(cake[x][j] != '?')
					{
						cake[i][j] = cake[x][j];
						break;
					}
				}
				if(cake[i][j] == '?')
				{
					for(int x = i-1; x>=0; x--)
					{
						if(cake[x][j] != '?')
						{
							cake[i][j] = cake[x][j];
							break;
						}
					}
				}
			}
		}
	}
	
	for(int i=0; i<c; i++)
	{
		for(int j=0; j<r; j++)
		{
			printf("%c", cake[i][j]);
		}
		puts("");
	}
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int t;
	scanf("%d", &t);
	
	for(int i=1; i<=t; i++)
	{
		printf("Case #%d:\n", i);
		solve();
	}
}
