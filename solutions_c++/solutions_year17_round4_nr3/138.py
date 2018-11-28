#include <stdio.h>

char s[110][110];
int qsx[20100] ,qsy[20100];
int main(void)
{
	int tt ,ii;
	int n ,m ,i ,j ,i2 ,j2 ,iii;
	int ans;
	int z;
	int nq;
	int x ,y;
	int xx ,yy;
	
	scanf("%d" ,&tt);
	for (ii=1 ; ii<=tt ; ii++)
	{
		printf("Case #%d: " ,ii);
		scanf("%d %d" ,&n ,&m);
		for (i=1 ; i<=n ; i++)
		{
			scanf("%s" ,s[i]+1);
		}
		ans=1;
		for (i=1 ; i<=n ; i++)
		{
			for (j=1 ; j<=m ; j++)
			{
				if (s[i][j]=='|')	
				{
					s[i][j]='-';
				}
			}
		}
		for (i=1 ; i<=n ; i++)
		{
			for (j=1 ; j<=m ; j++)	
			{
				if (s[i][j]=='-')
				{
					z=0;
					for (j2=j-1 ; j2 ; j2--)
					{
						if (s[i][j2]=='#')	
						{
							break;
						}
						else if (s[i][j2]=='|'||s[i][j2]=='-')
						{
							z=1;
							break;
						}
					}
					for (j2=j+1 ; j2<=m ; j2++)
					{
						if (s[i][j2]=='#')	
						{
							break;
						}
						else if (s[i][j2]=='|'||s[i][j2]=='-')
						{
							z=1;
							break;
						}
					}		
					if (z)			
					{
						s[i][j]='|';
						z=0;
						for (i2=i-1 ; i2 ; i2--)
						{
							if (s[i2][j]=='#')	
							{
								break;
							}
							else if (s[i2][j]=='|'||s[i2][j]=='-')
							{
								z=1;
								break;
							}
						}
						for (i2=i+1 ; i2<=n ; i2++)
						{
							if (s[i2][j]=='#')	
							{
								break;
							}
							else if (s[i2][j]=='|'||s[i2][j]=='-')
							{
								z=1;
								break;
							}
						}	
						if (z)					
						{
							ans=0;
						}
					}
				}
			}
		}	
		
		if (ans)
		{
			nq=0;
			for (i=1 ; i<=n ; i++)
			{
				for (j=1 ; j<=m ; j++)	
				{
					if (s[i][j]=='.')
					{
						nq++;
						qsx[nq]=i;
						qsy[nq]=j;
					}
				}
			}		
			for (iii=1 ; iii<=nq ; iii++)
			{
				x=qsx[iii];
				y=qsy[iii];
				z=0;
				for (i2=x-1 ; i2 ; i2--)
				{
					if (s[i2][y]=='#')	
					{
						break;
					}
					else if (s[i2][y]=='|')
					{
						z=1;
						break;
					}
				}
				for (i2=x+1 ; i2<=n ; i2++)
				{
					if (s[i2][y]=='#')	
					{
						break;
					}
					else if (s[i2][y]=='|')
					{
						z=1;
						break;
					}
				}	
				if (z)
				{
					s[x][y]='o';
				}
				else
				{
					z=0;
					for (j2=y-1 ; j2 ; j2--)
					{
						if (s[x][j2]=='#')	
						{
							break;
						}
						else if (s[x][j2]=='-')
						{
							z=1;
							break;
						}
					}
					for (j2=y+1 ; j2<=m ; j2++)
					{
						if (s[x][j2]=='#')	
						{
							break;
						}
						else if (s[x][j2]=='-')
						{
							z=1;
							break;
						}
					}		
					if (z)				
					{
						s[x][y]='?';
					}
					else
					{
						z=0;
						for (i2=x-1 ; i2 ; i2--)
						{
							if (s[i2][y]=='#')	
							{
								break;
							}
							else if (s[i2][y]=='-')
							{
								z=1;
								xx=i2;
								yy=y;
								break;
							}
						}
						for (i2=x+1 ; i2<=n ; i2++)
						{
							if (s[i2][y]=='#')	
							{
								break;
							}
							else if (s[i2][y]=='-')
							{
								z=1;
								xx=i2;
								yy=y;								
								break;
							}
						}							
						if (z)
						{
							s[x][y]='o';
							s[xx][yy]='|';
							z=0;
							for (i2=xx-1 ; i2 ; i2--)
							{
								if (s[i2][yy]=='#')	
								{
									break;
								}
								else if (s[i2][yy]=='-'||s[i2][yy]=='|')
								{
									z=1;
									break;
								}
							}
							for (i2=xx+1 ; i2<=n ; i2++)
							{
								if (s[i2][yy]=='#')	
								{
									break;
								}
								else if (s[i2][yy]=='-'||s[i2][yy]=='|')
								{
									z=1;								
									break;
								}
							}	
							if (z)
							{
								ans=0;
								break;	
							}							
							
							for (j2=yy-1 ; j2 ; j2--)
							{
								if (s[xx][j2]=='#')	
								{
									break;
								}
								else if (s[xx][j2]=='?')
								{
									s[xx][j2]='.';
									nq++;
									qsx[nq]=xx;
									qsy[nq]=j2;
								}
							}
							for (j2=yy+1 ; j2<=m ; j2++)
							{
								if (s[xx][j2]=='#')	
								{
									break;
								}
								else if (s[xx][j2]=='?')
								{
									s[xx][j2]='.';
									nq++;
									qsx[nq]=xx;
									qsy[nq]=j2;
								}
							}	

							
						}
						else
						{
							ans=0;
							break;
						}	
					}
				}
			}
		}
		
		if (ans)
		{
			printf("POSSIBLE\n");	
			for (i=1 ; i<=n ; i++)
			{
				for (j=1 ; j<=m ; j++)	
				{
					if (s[i][j]=='o'||s[i][j]=='?')
					{
						s[i][j]='.';
					}
				}
			}	
			for (i=1 ; i<=n ; i++)
			{
				printf("%s\n" ,s[i]+1);
			}
		}
		else
		{
			printf("IMPOSSIBLE\n");
		}	
	}
	
	return 0;
}
