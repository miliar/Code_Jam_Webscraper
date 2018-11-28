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

#define N 50
#define TOINT (double)10000000.f
#define ONE 10000000

int main()
{
	int t;
	s(t);
	forall(z, 0, t)
	{
		int n, k, u, inp[N+10];
		double temp;
		s(n); s(k); sf(temp);
		u = temp * TOINT;
		forall(i, 0, n)
		{
			sf(temp);
			inp[i] = temp * TOINT;
		}

		while(u > 0)
		{
			int min = INF, secondMin = INF;
			forall(i, 0, n)
			{
				if (min > inp[i])
				{
					secondMin = min;
					min = inp[i];
				}
				else if (min < inp[i] && secondMin > inp[i])
					secondMin = inp[i];
			}
			if (min >= ONE)
				break;

			int cnt = 0;
			forall(i, 0, n)
			{
				if (min == inp[i])
					cnt++;
			}
			int t = u / cnt;
			if (t == 0)
			{
				forall(i, 0, n)
				{
					if (min == inp[i])
					{
						inp[i] ++;
						u--;
						if (u == 0)
							break;
					}
				}
				break;
			}
			else
			{
				if (min + t > secondMin)
				{
					t = secondMin - min;
				}
				u -= t * cnt;
				forall(i, 0, n)
				{
					if (min == inp[i])
						inp[i] += t;
				}
			}
		};
		double ans = double(inp[0]) / TOINT;
		forall(i, 1, n)
		{
			ans *= double(inp[i]) / TOINT;
		}

		printf("Case #%d: %lf\n", z + 1, ans);
	}
}