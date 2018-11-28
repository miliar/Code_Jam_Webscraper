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

#define N 1000
bool deleted[N + 10];
struct dddd
{
	int k, speed;
}inp[N + 10];

int d, n;
double tim[N + 10];

bool sorti(dddd a, dddd b)
{
	return a.k < b.k;
}

int main()
{
	int t;
	s(t);
	forall(z, 0, t)
	{
		s(d); s(n);
		forall(i, 0, n)
		{
			s(inp[i].k); s(inp[i].speed);
		}
		sort(inp, inp + n, sorti);
		fill(deleted, false);
		fill(tim, 0.f);
		int rem = n;
		bool flag = false;
		double min = 0.f, ans = 0.f;
		if (z == 98)
		{
			int ddd;
			ddd = 10;
		}
		do
		{
			flag = false;
			min = 0.f;
			int p;
			forall(i, 0, n-1)
			{
				if (deleted[i])
					continue;
				int j = i + 1;
				while (j < n && deleted[j])
					j++;
				if (j >= n)
					continue;
				if (inp[i].speed > inp[j].speed)
				{
					tim[i] = double(inp[j].k - inp[i].k) / double(inp[i].speed - inp[j].speed);
					if (tim[i] * inp[i].speed + inp[i].k > d)
						continue;

					if (!flag || min > tim[i])
					{
						flag = true;
						min = tim[i];
						p = i;
					}
				}
			}
			if (flag)
			{
				deleted[p] = true;
				ans = min;
				rem--;
			}
		} while (rem >= 2 && flag);
		if (rem > 0)
		{
			forall(i, 0, n)
			{
				if (!deleted[i])
				{
					double temp = double(d - inp[i].k) / inp[i].speed;
					if (ans < temp || !(ans > 0))
					{
						ans = temp;
						flag = false;
					}
				}
			}
		}
		printf("Case #%d: %lf\n", z+1, double(d)/ans);
	}
}