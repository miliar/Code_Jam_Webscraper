#include <stdio.h>
#include <string.h>


char grid[25][26];
bool isempty[12];

int copy_below(int i, int R, int C)
{
	if (i + 1 >= R)
		return 1;
		
	if (isempty[i + 1] == true)
		if (copy_below(i + 1, R, C) == 1)
			return 1;

	memcpy(&grid[i][0], &grid[i+1][0], C*sizeof(char));
	isempty[i] = false;
	return 0;
}

int copy_above(int i, int R, int C)
{
	if (i - 1 < 0)
		return 1;
		
	if (isempty[i - 1] == true)
		if (copy_above(i - 1, R, C) == 1)
			return 1;

	memcpy(&grid[i][0], &grid[i-1][0], C*sizeof(char));
	isempty[i] = false;
	return 0;
}

int main(int argc, char** argv)
{
	freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    
    int T;
    scanf("%d", &T);
    
    for (int test = 0; test < T; test++)
    {
    	int R, C;
    	scanf("%d %d\n", &R, &C);
    	
    	memset(isempty, 0, 25*sizeof(bool));
    	
    	for (int i = 0; i < R; i++)
//    		for (int j = 0; j < C; j++)
//    			scanf("%c", &grid[i][j]);
    		gets(grid[i]);
    			
    	for (int i = 0; i < R; i++)
    	{
    		int j = 0;    		
    		while (grid[i][j] == '?') j++;
    		if (j >= C)
    		{
    			isempty[i] = true;
    			continue;
			}
    			
    		int pos = j;
    		char tmp = grid[i][j];
    		for (int k = 0; k < pos; k++)
    			grid[i][k] = tmp;
    		j++;
    		while (j < C)
    		{
    			if (grid[i][j] == '?')
    				grid[i][j] = tmp;
    			else
    				tmp = grid[i][j];
    			j++;
			}
		}
    	
    	for (int r = 0; r < R - 1; r++)
    		if (isempty[r])
    			copy_below(r, R, C);
    			
    	for (int r = 1; r < R; r++)
    		if (isempty[r])
    			copy_above(r, R, C);
    			
    	printf("Case #%d:\n", test +1);
    	for (int r = 0; r < R; r++)
    	{
    		for (int c = 0; c < C; c++)
    			printf("%c", grid[r][c]);
    		printf("\n");
		}
    		
	}
	
	return 0;
}
