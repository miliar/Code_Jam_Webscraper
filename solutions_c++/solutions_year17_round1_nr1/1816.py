#include <iostream>
using namespace std;

int main()
{
	int tt;
	scanf(" %d", &tt);
	
	for(int ii = 1; ii <= tt; ii++)
	{
		int r, c;
		scanf(" %d%d", &r, &c);
		
		char s[r][c];
		for(int i = 0; i < r; i++)
			scanf(" %s", s[i]);
		
		bool chk[26] = {};
		
		for(int i = 0; i < r; i++)
		{
			for(int j = 0; j < c; j++)
			{
				if(s[i][j] != '?')
				{
					char curr = s[i][j];
					int maxI = i;
					int minI = i;
					int maxJ = j;
					int minJ = j;
					
					chk[curr] = 1;
					for(int k = 0; k < r; k++)
					{
						for(int l = 0; l < c; l++)
						{
							if(s[k][l] == curr)
							{
								maxI = max(maxI, k);
								minI = min(minI, k);
								maxJ = max(maxJ, l);
								minJ = min(minJ, l);
								for(int m = minI; m <= maxI; m++)
								{
									for(int n = minJ; n <= maxJ; n++)
									{
										if(s[m][n] == '?')
											s[m][n] = curr;
									}
								}
							}
						}
					}
				}
			}
		}
		
		int cnt = 0;
		for(int i = 0; i < 26; i++)
			if(chk[i])
				cnt++;
			
		if(cnt == 1)
		{
			for(int i = 0; i < r; i++)
			{
				for(int j = 0; j < c; j++)
					printf("%c", s[i][j]);
				
				printf("\n");
			}
		}
		
		else
		{
			char prev = '?';
			for(int i = 0; i < r; i++)
			{
				for(int j = 0; j < c; j++)
				{
					if(s[i][j] == '?')
						s[i][j] = prev;
					
					else
						prev = s[i][j];
				}
				
				prev = '?';
			}
			
			for(int i = 0; i < r; i++)
			{
				for(int j = c -1; j >= 0; j--)
				{
					if(s[i][j] == '?')
						s[i][j] = prev;
					
					else
						prev = s[i][j];
				}
				
				prev = '?';
			}
			
			for(int j = 0; j < c; j++)
			{
				for(int i = 0; i < r; i++)
				{
					if(s[i][j] == '?')
						s[i][j] = prev;
					
					else
						prev = s[i][j];
				}
				
				prev = '?';
			}
			
			for(int j = 0; j < c; j++)
			{
				for(int i = r -1; i >= 0; i--)
				{
					if(s[i][j] == '?')
						s[i][j] = prev;
					
					else
						prev = s[i][j];
				}
				
				prev = '?';
			}
		}
		
		printf("Case #%d:\n", ii);
		
		for(int i = 0; i < r; i++)
		{
			for(int j = 0; j < c; j++)
				printf("%c", s[i][j]);
			printf("\n");
		}
	}
	
	return 0;
}

