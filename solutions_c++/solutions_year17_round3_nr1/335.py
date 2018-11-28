#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <memory.h>
#include <functional>

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
const double PI = 3.14159265359;

#define N 1000

struct aa
{
	__int64 r, h, dd;
};

bool sortaa(aa a, aa b)
{
	return a.dd > b.dd;
}


int main()
{
	int t;
	s(t);
	forall(z, 0, t)
	{
		int n, k;
		__int64 ans = 0;
		s(n); s(k);
		aa inp[N+10];
		forall(i, 0, n)
		{
			int r, h;
			s(r); s(h);
			inp[i].r = r;
			inp[i].h = h;
			inp[i].dd = 2 * inp[i].r * inp[i].h;
		}
		sort(inp, inp+n, sortaa);
		
		forall(i, 0, n)
		{
			int cnt = 1;
			__int64 temp = inp[i].dd + inp[i].r * inp[i].r;
			forall(j, 0, n)
			{
				if (i == j)
					continue;
				if (cnt >= k)
					break;
				cnt++;
				temp += inp[j].dd;
			}
			if (ans < temp)
				ans = temp;
		}
		double p = (double)ans;
		p *= PI;
		printf("Case #%d: %lf\n", z + 1, p);
	}
}