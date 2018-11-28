#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int T;
    scanf("%d",&T);
    for(int t=1; t<=T; t++)
    {
        printf("Case #%d:\n",t);
        int r, c;
        scanf("%d %d", &r, &c);
        char mat[30][30];
        for(int i=1; i<=r; i++)
        	for(int j=1; j<=c; j++)
        		scanf(" %c", &mat[i][j]);

        for(int j=1; j<=c; j++)
        {
        	char f = '\0';
        	for(int i=1; i<=r; i++)
        	{
        		if(mat[i][j] != '?')
        		{
        			f = mat[i][j];
        			break;
        		}
        	}
        	if(f)
        	for(int i=1; i<=r; i++)
        	{
        		if(mat[i][j] == '?' || mat[i][j] == f)
        			mat[i][j] = f;
        		else
        			f = mat[i][j];
        	}
        }
        for(int i=1; i<=r; i++)
        {
        	char f = '\0';
        	for(int j=1; j<=c; j++)
        	{
        		if(mat[i][j] != '?')
        		{
        			f = mat[i][j];
        			break;
        		}
        	}
        	if(f)
        	for(int j=1; j<=c; j++)
        	{
        		if(mat[i][j] == '?' || mat[i][j] == f)
        			mat[i][j] = f;
        		else
        			f = mat[i][j];
        	}
        }
        for(int i=1; i<=r; i++)
        {
        	for(int j=1; j<=c; j++)
        		printf("%c", mat[i][j]);
        	printf("\n");
        }
    }
    return 0;
}
