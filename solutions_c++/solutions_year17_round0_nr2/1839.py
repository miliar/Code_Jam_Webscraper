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

int n;
char ans[30];
char inp[30];

bool dfs(int m, bool less, int digit)
{
	if (digit >= n)
		return true;

	int st = less ? 9 : inp[digit];
	bool nLess = less;
	for (int i = st; i >= m; i--)
	{
		if (i < inp[digit])
			nLess = true;

		ans[digit] = i + '0';
		if (dfs(max(i, m), nLess, digit + 1))
			return true;
	}
	return false;
}

int main()
{
	int z, t;
	s(t);
	forall(z, 1, t + 1)
	{
		ss(inp);
		n = strlen(inp);
		forall(i, 0, n)
			inp[i] -= '0';
		fill(ans, 0);
		for (int i = inp[0]; i >= 0; i--)
		{
			ans[0] = i+'0';
			if (dfs(i, (i == inp[0]) ? false : true, 1))
			{
				ans[n] = NULL;
				if(i > 0)
					printf("Case #%d: %s\n", z, ans);
				else
					printf("Case #%d: %s\n", z, ans+1);
				break;
			}
		}

	}
}