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

#define N 100

int main()
{
	int t;
	s(t);
	forall(z, 0, t)
	{
		int n, p;
		s(n); s(p);
		int inp[N + 10];
		forall(i, 0, n)
		{
			s(inp[i]);
			inp[i] %= p;
		}

		int ans = 0;
		if (p == 2)
		{
			int m = 0;
			forall(i, 0, n)
			{
				if (inp[i] == 0)
					ans++;
				else
				{
					m += inp[i];
					if (m > 0 && m % 2 == 0)
					{
						ans++;
						m = 0;
					}
				}
			}
			if (m > 0)
				ans++;
		}
		else if (p == 3)
		{
			int cnt[3] = { 0, };
			forall(i, 0, n)
			{
				if (inp[i] == 0)
					ans++;
				cnt[inp[i]] ++;
			}
			
			int m = min(cnt[1], cnt[2]);
			ans += m;
			cnt[1] -= m;
			cnt[2] -= m;

			ans += cnt[1] / 3;
			cnt[1] %= 3;
			ans += cnt[2] / 3;
			cnt[2] %= 3;
			if (cnt[1] + cnt[2] > 0)
				ans++;

		}
		else // p == 4
		{
			int cnt[4] = { 0, };
			forall(i, 0, n)
			{
				cnt[inp[i]] ++;
			}
			ans = cnt[0];

			int m = min(cnt[1], cnt[3]);
			ans += m;
			cnt[1] -= m;
			cnt[3] -= m;

			ans += cnt[2] / 2;
			cnt[2] %= 2;


			if (cnt[2] > 0) // == 1
			{
				if (cnt[3] % 4 >= 2)
				{
					ans++;
					cnt[2]--;
					cnt[3] -= 2;
				}
				else if (cnt[1] % 4 >= 2)
				{
					ans++;
					cnt[2] --;
					cnt[3] -= 2;
				}
			}

			ans += cnt[3] / p;
			cnt[3] %= p;

			ans += cnt[1] / p;
			cnt[1] %= p;

			if (cnt[3] + cnt[1] > p)
			{
				ans++;
				cnt[1] += cnt[3];
				cnt[3] = 0;
				cnt[1] %= p;
			}
			if (cnt[1] + cnt[2] + cnt[3] > 0)
				ans++;

		}
		printf("Case #%d: %d\n", z + 1, ans);
	}
}