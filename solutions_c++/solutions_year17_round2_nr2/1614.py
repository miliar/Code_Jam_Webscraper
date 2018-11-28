#include<stdio.h>

// small only

void solve(void)
{
	int n;
	int uni[6];
	char stall[1001];
	int tmp[3];
	char color[6] = {'R', 'O', 'Y', 'G', 'B', 'V'};
	
	scanf("%d", &n);
	for(int i=0; i<6; i++)
	{
		scanf("%d", &uni[i]);
	}
	
	// 원형 
	if(uni[1] == uni[4] && uni[1] != 0)
	{
		for(int i=0; i<6; i++)
		{
			if(!(i == 1 || i == 4))
			{
				if(uni[i] != 0)
				{
					printf("IMPOSSIBLE\n");
					return;
				}
			}
		}
		
		for(int i=0; i<n/2; i++)
		{
			printf("OB");
		}
		puts("");
		return;
	}
	if(uni[0] == uni[3]  && uni[3] != 0)
	{
		for(int i=0; i<6; i++)
		{
			if(!(i == 0 || i == 3))
			{
				if(uni[i] != 0)
				{
					printf("IMPOSSIBLE\n");
					return;
				}
			}
		}
		
		for(int i=0; i<n/2; i++)
		{
			printf("RG");
		}
		puts("");
		return;
	}
	if(uni[2] == uni[5] && uni[5] != 0)
	{
		for(int i=0; i<6; i++)
		{
			if(!(i == 2 || i == 5))
			{
				if(uni[i] != 0)
				{
					printf("IMPOSSIBLE\n");
					return;
				}
			}
		}
		
		for(int i=0; i<n/2; i++)
		{
			printf("VY");
		}
		puts("");
		return;
	}

	if(uni[2] < uni[5] || uni[0] < uni[3] || uni[4] < uni[1])
	{
		printf("IMPOSSIBLE\n");
		return;
	}
	
	uni[2] = uni[2] - uni[5];
	uni[0] = uni[0] - uni[3];
	uni[4] = uni[4] - uni[1];
	
	// 이제 RGB만 처리하면 됨
	
	if(uni[0] >= uni[2] && uni[2] >= uni[4])
	{
		tmp[0] = 0;
		tmp[1] = 2;
		tmp[2] = 4;
	}
	else if(uni[0] >= uni[4] && uni[4] >= uni[2])
	{
		tmp[0] = 0;
		tmp[1] = 4;
		tmp[2] = 2;
	}
	else if(uni[2] >= uni[0] && uni[0] >= uni[4])
	{
		tmp[0] = 2;
		tmp[1] = 0;
		tmp[2] = 4;
	}
	else if(uni[2] >= uni[4] && uni[4] >= uni[0])
	{
		tmp[0] = 2;
		tmp[1] = 4;
		tmp[2] = 0;
	}
	else if(uni[4] >= uni[2] && uni[2] >= uni[0])
	{
		tmp[0] = 4;
		tmp[1] = 2;
		tmp[2] = 0;
	}
	else if(uni[4] >= uni[0] && uni[0] >= uni[2])
	{
		tmp[0] = 4;
		tmp[1] = 0;
		tmp[2] = 2;
	}
	
	if(uni[tmp[0]] > uni[tmp[1]] + uni[tmp[2]])
	{
		printf("IMPOSSIBLE\n");
		return;
	}
	
	while(1)
	{
		if(uni[tmp[0]] == 0) break;

		if(uni[tmp[0]] != 0)
		{
			if(uni[(tmp[0] + 3) % 6] != 0)
			{
				uni[(tmp[0] + 3) % 6]--;
				printf("%c%c%c", color[tmp[0]], color[(tmp[0] + 3) % 6], color[tmp[0]]);
			}
			else
			{
				printf("%c", color[tmp[0]]);
			}
			uni[tmp[0]] --;
		}
		if(uni[tmp[1]] != 0)
		{
			if(uni[(tmp[1] + 3) % 6] != 0)
			{
				uni[(tmp[1] + 3) % 6]--;
				printf("%c%c%c", color[tmp[1]], color[(tmp[1] + 3) % 6], color[tmp[1]]);
			}
			else
			{
				printf("%c", color[tmp[1]]);
			}
			uni[tmp[1]] --;
		}
		if(uni[tmp[2]] == uni[tmp[0]] + 1 && uni[tmp[2]] != 0)
		{
			if(uni[(tmp[2] + 3) % 6] != 0)
			{
				uni[(tmp[2] + 3) % 6]--;
				printf("%c%c%c", color[tmp[2]], color[(tmp[2] + 3) % 6], color[tmp[2]]);
			}
			else
			{
				printf("%c", color[tmp[2]]);
			}
			uni[tmp[2]] --;
		}
	}
	
	puts("");
}

int main()
{
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("output.out", "w", stdout);
	
	int t;
	scanf("%d", &t);
	
	for(int i=1; i<=t; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}
}
