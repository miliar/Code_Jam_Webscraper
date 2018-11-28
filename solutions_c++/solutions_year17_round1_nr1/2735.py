#include <bits/stdc++.h>

#define INF 0x3f3f3f3f
#define NINF -0x3f3f3f3f

using namespace std;

typedef pair<int,int> pii;

char cake[30][30];
int visited[30][30];
vector<pii> lts;

void fillC (int mnR, int mxR, int mnC, int mxC, char lt)
{
	for (int i = mnR; i <= mxR; i += 1)
	{
		for (int j = mnC; j <= mxC; j += 1)
		{
			cake[i][j] = lt;
		}
	}
}

bool bt (int pos, int r, int c)
{
	if (pos == lts.size())
	{
		for (int i = 0; i < r; i += 1)
		{
			for (int j = 0; j < c; j += 1)
			{
				if (cake[i][j] == '?')
					return false;
			}
		}
		
		return true;
	}
	
	const int x = lts[pos].first;
	const int y = lts[pos].second;
	const char lt = cake[x][y];
	
	for (int i = 0; i <= y; i += 1)
	{
		for (int j = y; j <= c-1; j += 1)
		{
			bool valid = true;
			for (int k = i; k <= j ; k += 1)
			{
				if (cake[x][k] != lt && cake[x][k] != '?')
				{
					valid = false;
					break;
				}
			}
			
			if (!valid)
				break;
				
			int mnR = x;
			int mxR = x;
			
			for (int k = x-1; k >= 0; k--)
			{
				bool ivalid = true;
				for (int l = i; l <= j; l += 1)
				{
					if (cake[k][l] != '?')
					{
						ivalid = false;
						break;
					}
				}
				
				if (!ivalid)
					break;
					
				--mnR;
			}
			
			for (int k = x+1; k < r; k += 1)
			{
				bool ivalid = true;
				for (int l = i; l <= j; l += 1)
				{
					if (cake[k][l] != '?')
					{
						ivalid = false;
						break;
					}
				}
				
				if (!ivalid)
					break;
					
				++mxR;
			}
			
			fillC(mnR,mxR,i,j,lt);
			
			if (bt(pos+1,r,c))
				return true;

			fillC(mnR,mxR,i,j,'?');
			cake[x][y] = lt;
		}
	}
	
	return false;
}

void solve ()
{
	int r,c;
	scanf("%d %d",&r,&c);
	
	lts.clear();
	for (int i = 0; i < r; i += 1)
	{
		scanf("%s",cake[i]);
		
		for (int j = 0; j < c; j += 1)
		{
			if (cake[i][j] != '?')
			{
				lts.push_back(pii(i,j));
			}
		}
	}
	
	bt(0,r,c);
	
	for (int i = 0; i < r; i += 1)
	{
		printf("%s\n",cake[i]);
	}
}

int main (int argc, char const* argv[])
{
	int T;
	scanf("%d",&T);
	
	for (int t = 1; t <= T; t += 1)
	{
		printf("Case #%d:\n",t);
		solve();
	}
	
	return 0;
}
