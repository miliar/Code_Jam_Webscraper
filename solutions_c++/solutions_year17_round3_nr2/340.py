#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <memory.h>

using namespace std;

// Input macros
#define s(n)                        scanf("%d",&n)
#define sl(n)						scanf("%I64d", &n)
#define sc(n)                       scanf("%c",&n)
#define sf(n)                       scanf("%lf",&n)
#define ss(n)                       scanf("%s",n)

// Useful container manipulation / traversal macros
#define forall(i,a,b)               for(int i=a;i<b;i++)
#define foreach(v, c)               for( typeof( (c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define all(a)                      a.begin(), a.end()
#define in(a,b)                     ( (b).find(a) != (b).end())
#define pb                          push_back
#define fill(a,v)                    memset(a, v, sizeof a)
#define sz(a)                       ((int)(a.size()))
#define mp                          make_pair

typedef vector<int> vi;
typedef vector<string> vs;

#define INF 2147483647
#define UINF 0xffffffff

#define DAY 1440
#define HALFDAY 720
int dyn[HALFDAY + 10][HALFDAY + 10][2];

int main()
{
	int t;
	s(t);
	forall(z, 0, t)
	{
		bool Act[2][DAY+10] = { false, };
		fill(dyn, 10000);
		int inp[2];
		s(inp[0]); s(inp[1]);
		forall(l, 0, 2)
		{
			forall(i, 0, inp[l])
			{
				int st, ed;
				s(st); s(ed);
				forall(k, st, ed)
				{
					Act[l][k] = true; // l == 0(c), l == 1(j)
				}
			}
		}
		if(!Act[0][0])
			dyn[0][0][0] = 0;
		if(!Act[1][0])
			dyn[0][0][1] = 0;
		forall(i, 0, HALFDAY + 1)
		{
			if (i == 540)
			{
				int ff;ff = 10;
			}
			forall(j, 0, HALFDAY + 1)
			{
				if (i == j && i == 0)
					continue;
				
				if (!Act[0][i + j - 1] && i > 0 && dyn[i][j][0] > dyn[i - 1][j][0])
					dyn[i][j][0] = dyn[i - 1][j][0];
				if (!Act[1][i + j - 1] && j > 0 && dyn[i][j][0] > dyn[i][j - 1][1] + 1)
					dyn[i][j][0] = dyn[i][j - 1][1] + 1;

				if (!Act[0][i + j - 1] && i > 0 && dyn[i][j][1] > dyn[i - 1][j][0] + 1)
					dyn[i][j][1] = dyn[i - 1][j][0] + 1;
				if (!Act[1][i + j - 1] && j > 0 && dyn[i][j][1] > dyn[i][j - 1][1])
					dyn[i][j][1] = dyn[i][j - 1][1];
			}
		}

		int ans = min(dyn[HALFDAY][HALFDAY][0], dyn[HALFDAY][HALFDAY][1]);
		if (ans % 2 == 1)
			ans++;

		printf("Case #%d: %d\n", z + 1, ans);
		
	}
}