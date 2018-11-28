#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <cmath>

using namespace std;

struct Rect
{
	int minY, minX, maxY, maxX;
	
	Rect()
	{
	}
	
	Rect(int a, int b, int c, int d) : minY(a), minX(b), maxY(c), maxX(d)
	{
	}
	
	void add(int nY, int nX)
	{
		minY=min(minY, nY);
		minX=min(minX, nX);
		maxY=max(maxY, nY);
		maxX=max(maxX, nX);
	}
};

Rect rect[30];

bool inter(Rect a, Rect b)
{
	int bidule = max(a.minX, b.minX);
	int truc = min(a.maxX, b.maxX);
	
	int chose = max(a.minY, b.minY);
	int chouette = min(a.maxY, b.maxY);
	
	return bidule <= truc && chose <= chouette;
}

int main()
{
	int T;
	scanf("%d", &T);
	
	for(int t = 1; t<=T; t++)
	{
		int nbL, nbC;
		scanf("%d%d", &nbL, &nbC);
		
		char grid[30][30];
		char seen[30];
		for(int i= 0; i < nbL; i++)
		{
			scanf("%s", grid[i]);
		}
		
		for(int i = 0; i < 26; i++)
			seen[i]=0;
		
		for(int i= 0; i < nbL; i++)
		{
			for(int j = 0; j < nbC; j++)
			{
				if(grid[i][j]=='?')continue;
				int c = grid[i][j]-'A';
				if(seen[c])
					continue;
				seen[c]=1;
				int minX=j, minY=i, maxX=j, maxY=i;
				for(int autreY = 0; autreY < nbL; autreY++)
				{
					for(int autreX = 0; autreX < nbC; autreX++)
					{
						int autreC=grid[autreY][autreX]-'A';
						if(autreC==c)
						{
							minX = min(minX, autreX);
							minY = min(minY, autreY);
							maxX = max(maxX, autreX);
							maxY = max(maxY, autreY);
						}
					}
				}
				rect[c]=Rect(minY, minX, maxY, maxX);
			}
		}
		
		printf("Case #%d:\n", t);
		
		/*int bd='C'-'A';
		printf("(%d;%d) et (%d;%d) \n", rect[bd].minY, rect[bd].minX, rect[bd].maxY, rect[bd].maxX);
		printf("%d \n", seen[bd]);*/
		
		for(int i = 0; i < nbL; i++)
		{
			for(int j = 0; j < nbC; j++)
			{
				if(grid[i][j]=='?')
				{
					for(int c = 0; c < 26; c++)
					{
						if(!seen[c])continue;
						Rect newRect = rect[c];
						newRect.add(i,j);
						bool ok=true;
						for(int autreC = 0; autreC < 26; autreC++)
						{
							if(!seen[autreC] || autreC==c)continue;
							if(inter(newRect, rect[autreC]))
								ok=false;
						}
						if(ok)
						{
							grid[i][j]=c+'A';
							rect[c]=newRect;
							/*if(i==1 && j==0)
							{
								printf("debug : \n");
								bd='C'-'A';
								printf("(%d;%d) et (%d;%d) \n", rect[bd].minY, rect[bd].minX, rect[bd].maxY, rect[bd].maxX);
							}*/
							break;
						}
					}
				}
				
				putchar(grid[i][j]);
			}
			putchar('\n');
		}
		
		/*bd='C'-'A';
		printf("(%d;%d) et (%d;%d) \n", rect[bd].minY, rect[bd].minX, rect[bd].maxY, rect[bd].maxX);
		
		printf("debug : inter entre G et C = %d\n", inter(rect[bd], rect['G'-'A']));*/
	}
	
	return 0;
}

