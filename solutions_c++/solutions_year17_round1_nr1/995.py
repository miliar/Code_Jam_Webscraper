#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(void)
{
	int a;
	FILE* fp = fopen("Output.txt", "w+");
	scanf("%d", &a);
	for(int x=0;x<a;x++)
	{
		int r, c;
		char d[25][25] = {0};
		bool comp[26] = {0};
		scanf("%d%d", &r, &c);
		for(int i=0;i<r;i++)
			scanf("%s", d[i]);
		//for(int i=0;i<r;i++)
		//	printf("%s\n", d[i]);
		for(int i=0;i<r;i++)
			for(int j=0;j<c;j++)
			{
				if(d[i][j]!='?'&&!comp[d[i][j]-'A'])
				{
					bool tr1 = 1, tr2 = 1;
					int x1 = 0, y1 = 0, x2 = 0, y2 = 0;
					while(tr2)
					{
						tr2 = 0;
						tr1 = 1;
						//printf("%d%d%d%d%d%d\n", x1, x2, y1, y2, i, j);
						if(i+x1-1>=0)
						{
							for(int k=y1;k<=y2;k++)
								if(d[i+x1-1][j+k] != '?')
									tr1 = 0;
							if(tr1)
							{
								for(int k=y1;k<=y2;k++)
									d[i+x1-1][j+k] = d[i][j];
								tr2 = 1;
								x1--;
								//printf("%d%d\n", i+x1-1, j);
							}
							tr1 = 1;
						}
						if(i+x2+1<r)
						{
							for(int k=y1;k<=y2;k++)
								if(d[i+x2+1][j+k] != '?')
									tr1 = 0;
							if(tr1)
							{
								for(int k=y1;k<=y2;k++)
									d[i+x2+1][j+k] = d[i][j];
								tr2 = 1;
								x2++;
								//printf("%d%d\n", i+x2+1, j);
							}
							tr1 = 1;
						}
						if(j+y1-1>=0)
						{
							for(int k=x1;k<=x2;k++)
								if(d[i+k][j+y1-1] != '?')
									tr1 = 0;
							if(tr1)
							{
								for(int k=x1;k<=x2;k++)
									d[i+k][j+y1-1] = d[i][j];
								tr2 = 1;
								y1--;
								//printf("%d%d\n", i, j+y1-1);
							}
							tr1 = 1;
						}
						if(j+y2+1<c)
						{
							for(int k=x1;k<=x2;k++)
								if(d[i+k][j+y2+1] != '?')
									tr1 = 0;
							if(tr1)
							{
								for(int k=x1;k<=x2;k++)
									d[i+k][j+y2+1] = d[i][j];
								tr2 = 1;
								y2++;
								//printf("%d%d\n", i, j+y2+1);
							}
							tr1 = 1;
						}
						/*for(int i=0;i<r;i++)
						{
							for(int j=0;j<c;j++)
								printf("%c", d[i][j]);
							printf("\n");
						}
						printf("%d %d\n\n", i+1, j+1);*/
					}
					comp[d[i][j]-'A'] = 1;
				}
			}
		fprintf(fp, "Case #%d:\n", x+1);
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
				fprintf(fp, "%c", d[i][j]);
			fprintf(fp, "\n");
		}
	}
	return 0;
}
