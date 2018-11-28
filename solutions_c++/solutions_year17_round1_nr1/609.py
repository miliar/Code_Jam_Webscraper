#include <bits/stdc++.h>

#define icin(x) scanf("%d",&x)
#define lcin(x) scanf("%lld",&x)
#define pb push_back
#define LL long long
#define F first
#define S second
#define VPI vector< pair<int,int> >
#define VVI vector< vector<int> > 
#define BC(x) __builtin_popcount(x)

using namespace std;

int main()
{
	int t;
	icin(t);
	for(int tc=1; tc<=t; tc++)
	{
		int r,c;
		icin(r);
		icin(c);
		string data[r];
		vector<int> emp(r,0);
		for(int i=0; i<r; i++)
		{
			cin >> data[i];
			for(int j=0; j<c; j++)
			{
				if(data[i][j] != '?')
					emp[i] = 1;
			}
		}
		int cur = -1,done = -1;
		for(int i=0; i<r; i++)
		{
			if(emp[i] == 0)
			{
				if(cur != -1)
				{
					data[i] = data[cur];
					done = i;
				}
			}
			else
			{
				cur = i;
				for(int j=0; j<c; j++)
				{
					if(data[i][j] != '?')
					{
						if( (j+1) < c && data[i][j+1] == '?')
							data[i][j+1] = data[i][j];
					}
				}
				for(int j=c; j>=0; j--)
				{
					if(data[i][j] != '?')
					{
						if( (j-1) >= 0 && data[i][j-1] == '?')
							data[i][j-1] = data[i][j];
					}	
				}
				for(int j=done+1; j<i; j++)
					data[j] = data[cur];
				done = i;
			}
		}
		printf("Case #%d:\n",tc);
		for(int i=0; i<r; i++)
		{
			for(int j=0; j<c; j++)
				printf("%c",data[i][j]);
			printf("\n");
		}
	}
	return 0;
}