#include <bits/stdc++.h>

#define INF 0x3f3f3f3f
#define NINF -0x3f3f3f3f

using namespace std;

typedef pair<int,int> pii;

enum
{
	RR,
	OO,
	YY,
	GG,
	BB,
	VV
};

int cx[6];
int vv[6][6];
string lts = "ROYGBV";

void solve ()
{
	int n;
	scanf("%d",&n);
	
	int total = 0;
	for (int i = 0; i < 6; i += 1)
	{
		scanf("%d",&cx[i]);
		total += cx[i];
	}
	
	for (int i = 0; i < 6; i += 1)
	{
		if (cx[i] > n/2)
		{
			printf("IMPOSSIBLE\n");
			return;
		}
	}
	
	//ELIMINAR LOS O,G, V!!!
	
	assert(cx[VV] == 0 && cx[GG] == 0 && cx[OO] == 0);
	int pos = max_element(cx,cx+6)-cx;

	string ans;
	
	if (pos == RR)
	{	
		int leftY = cx[RR]-cx[BB];
		for (int i = 0; i < cx[RR]; i += 1)
		{
			ans += 'R';
			
			if (cx[BB])
			{
				ans += 'B';
				cx[BB]--;
				
				if (cx[YY] > leftY)
				{
					ans += 'Y';
					--cx[YY];
				}
			}
			else if (cx[YY])
			{
				ans += 'Y';
				cx[YY]--;
			}
		}
	}
	else if (pos == BB)
	{
		int leftY = cx[BB]-cx[RR];
		for (int i = 0; i < cx[BB]; i += 1)
		{
			ans += 'B';
			
			if (cx[RR])
			{
				ans += 'R';
				--cx[RR];
				
				if (cx[YY] > leftY)
				{
					ans += 'Y';
					--cx[YY];
				}
			}
			else if (cx[YY])
			{
				ans += 'Y';
				--cx[YY];
			}
			else
			{
				printf("IMPOSSIBLE\n");
				return ;
			}
		}
	}
	else if (pos == YY)
	{
		int leftB = cx[YY]-cx[RR];
		for (int i = 0; i < cx[YY]; i += 1)
		{
			ans += 'Y';
			
			if (cx[RR])
			{
				ans += 'R';
				cx[RR]--;
				
				if (cx[BB] > leftB)
				{
					ans += 'B';
					cx[BB]--;
				}
			}
			else if (cx[BB])
			{
				ans += 'B';
				cx[BB]--;
			}
			else
			{
				printf("IMPOSSIBLE\n");
				return ;
			}
		}
	}

	printf("%s\n",ans.c_str());
}

int main (int argc, char const* argv[])
{
	vv[RR][BB] = vv[RR][YY] = vv[RR][GG] = true;
	vv[BB][RR] = vv[BB][YY] = vv[BB][OO] = true;
	vv[YY][BB] = vv[YY][RR] = vv[YY][VV] = true;
	vv[OO][BB] = true;
	vv[GG][RR] = true;
	vv[VV][YY] = true;
	
	int T;
	scanf("%d",&T);
	
	for (int t = 1; t <= T; t += 1)
	{
		printf("Case #%d: ",t);
		solve();
	}
	
	return 0;
}
