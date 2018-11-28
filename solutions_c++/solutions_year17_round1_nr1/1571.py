#include <cstdio>



int main()
{
	int T;
	scanf("%d", &T);
	int cnt = 1;
	while(T--)
	{
		int r, c;
		scanf("%d%d", &r, &c);
		char map[32][32];
		int appear[26];
		for(int i = 0; i < r; i++)
		{
			scanf("%s", map[i]);
			for(int j = 0; j < c; j++)
			{
				appear[map[i][j] - 'A'] = 1;
			}
		}
		int edge[26][4];	//0:up,	1:down,	2:left,	3:right
		for(int i = 0; i < 26; i++)
		{
			edge[i][0] = edge[i][2] = 2147483647;
			edge[i][1] = edge[i][3] = -1;
			for(int j = 0; j < r; j++)
			{
				for(int k = 0; k < c; k++)
				{
					if(map[j][k] == ('A' + i))
					{
						if(j <= edge[i][0])
						{
							edge[i][0] = j;
						}
						if(j >= edge[i][1])
						{
							edge[i][1] = j;
						}
						if(k <= edge[i][2])
						{
							edge[i][0] = k;
						}
						if(k >= edge[i][3])
						{
							edge[i][1] = k;
						}
					}
				}
			}
		}
		for(int i = 0; i < 26; i++)
		{
			if(appear[i] == 1)
			{
				for(int j = edge[i][0]; j <= edge[i][1]; j++)
				{
					for(int k = edge[i][2]; k <= edge[i][3]; k++)
					{
						map[j][k] = ('A' + i);
					}
				}
			}
		}



		for(int i = 0; i < r; i++)
		{
			for(int j = 0; j < c; j++)
			{
				if(j != c-1)
				{
					if(map[i][j] == '?')
					{
						for(int k = j+1; k < c; k++)
						{
							if(map[i][k] != '?')
							{
								map[i][j] = map[i][k];
								break;
							}
						}
					}
				}
				else
				{
					if(map[i][j] == '?')
					{
						for(int k = j-1; k >= 0; k--)
						{
							if(map[i][k] != '?')
							{
								map[i][j] = map[i][k];
								break;
							}
						}
					}
				}
				
			}
		}

		for(int i = 0; i < r; i++)
		{
			for(int j = 0; j < c; j++)
			{
				if(j == 0)
				{
					if(map[i][j] == '?')
					{
						for(int k = j+1; k < c; k++)
						{
							if(map[i][k] != '?')
							{
								map[i][j] = map[i][k];
								break;
							}
						}
					}
				}
				if(j != 0)
				{
					if(map[i][j] == '?')
					{
						for(int k = j-1; k >= 0; k--)
						{
							if(map[i][k] != '?')
							{
								map[i][j] = map[i][k];
								break;
							}
						}
					}
				}
				
			}
		}


		for(int i = 0; i < c; i++)
		{
			for(int j = 0; j < r; j++)
			{
				if(j != r-1)
				{
					if(map[j][i] == '?')
					{
						for(int k = j+1; k < r; k++)
						{
							if(map[k][i] != '?')
							{
								map[j][i] = map[k][i];
								break;
							}
						}
					}
				}
				else
				{
					if(map[j][i] == '?')
					{
						for(int k = j-1; k >= 0; k--)
						{
							if(map[k][i] != '?')
							{
								map[j][i] = map[k][i];
								break;
							}
						}
					}
				}
			}
		}

		for(int i = 0; i < c; i++)
		{
			for(int j = 0; j < r; j++)
			{
				if(j == 0)
				{
					if(map[j][i] == '?')
					{
						for(int k = j+1; k < r; k++)
						{
							if(map[k][i] != '?')
							{
								map[j][i] = map[k][i];
								break;
							}
						}
					}
				}
				else if(j != 0)
				{
					if(map[j][i] == '?')
					{
						for(int k = j-1; k >= 0; k--)
						{
							if(map[k][i] != '?')
							{
								map[j][i] = map[k][i];
								break;
							}
						}
					}
				}
			}
		}


		printf("Case #%d:\n", cnt++);
		for(int i = 0; i < r; i++)
		{
			printf("%s\n", map[i]);
		}


	}





	return 0;
}