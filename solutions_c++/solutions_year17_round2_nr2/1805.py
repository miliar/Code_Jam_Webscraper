#include<bits/stdc++.h>

using namespace std;

char ans[1500];

sama(char a, char b)
{
	if(a == b) return true;
	else return false;
}

typedef struct{
	char color;
	int byk;
} pony;

pony li[10];

bool cmp(pony a, pony b)
{
	return (a.byk >= b.byk);
}

int main()
{
	int T;
	cin>>T;
	int N, R, O, Y, G, B, V;
	for(int tc=1;tc<=T;tc++)
	{
		cin>>N>>R>>O>>Y>>G>>B>>V;
		
		for(int i=0;i<=N;i++)
		{
			ans[i] = 'X';
		}
		int ii=1;
		
		li[0].color = 'R'; li[0].byk = R;
		li[1].color = 'Y'; li[1].byk = Y;
		li[2].color = 'B'; li[2].byk = B;
		sort(li, li+3, cmp);
		
		while(li[0].byk || O || li[1].byk || G || li[2].byk || V)
		{	
			if(li[0].byk>0 && li[0].byk>=li[1].byk && li[0].byk>=li[2].byk)
			{
				ans[ii]=li[0].color; li[0].byk--; ii++;
				if(li[1].byk>0 && li[1].byk>=li[2].byk)
				{
					ans[ii] = li[1].color; li[1].byk--; ii++;
				}
				else if(li[2].byk>0) 
				{
					ans[ii] = li[2].color; li[2].byk--; ii++;
				}
			}
			else if(li[1].byk>0 && li[1].byk>=li[0].byk && li[1].byk>=li[2].byk)
			{
				ans[ii]=li[1].color; li[1].byk--; ii++;
				if(li[0].byk>0 && li[0].byk>=li[2].byk)
				{				
					ans[ii] = li[0].color; li[0].byk--; ii++;
				}
				else if(li[2].byk>0) 
				{
					ans[ii] = li[2].color; li[2].byk--; ii++;
				}
			}
			else if(li[2].byk>0 && li[2].byk>=li[0].byk && li[2].byk>=li[1].byk)
			{
				ans[ii]=li[2].color; li[2].byk--; ii++;
				if(li[0].byk>0 && li[0].byk>=li[1].byk)
				{
					ans[ii] = li[0].color; li[0].byk--; ii++;
				}	
				else if(li[1].byk>0)
				{
					ans[ii] = li[1].color; li[1].byk--; ii++;
				}
			}
			else break;
		}
		
		if(ii<N || sama(ans[1],ans[N]))
		{
			printf("Case #%d: IMPOSSIBLE\n", tc);
		}
		else
		{
			printf("Case #%d: ", tc);
			for(int i=1;i<=N;i++)
			{
				printf("%c", ans[i]);
			}
			printf("\n");
		}
	}

	return 0;
}
