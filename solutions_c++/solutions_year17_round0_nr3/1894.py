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

struct st
{
	__int64 numbers = 0, size = 0;
}stall[2];

int main()
{
	int z, t;
	s(t);
	forall(z, 1, t + 1)
	{
		__int64 n, k, cur = 1;
		sl(n); sl(k);
		stall[0].size = n;
		stall[0].numbers = 1;
		stall[1].size = stall[1].numbers = 0;
		do
		{
			st a, b;
			forall(i, 0, 2)
			{
				if (stall[i].size <= 0)
					continue;

				k -= stall[i].numbers;
				if (k <= 0)
				{
					printf("Case #%d: %I64d %I64d\n", z, stall[i].size / 2, (stall[i].size - 1) / 2);
					break;
				}
				if (stall[i].size > 1)
				{
					if (stall[i].size % 2 == 0)
					{
						__int64 a1 = stall[i].size / 2;
						if (a1 <= 0)
							continue;

						__int64 a2 = a1 - 1;

						if (i == 0)
						{
							a.size = a1;
							a.numbers = stall[i].numbers;
							if (a2 > 0)
							{
								b.size = a2;
								b.numbers = stall[i].numbers;
							}
						}
						else
						{
							// must be odd
							if (a.size == a1)
							{
								a.numbers += stall[i].numbers;
								if (a2 > 0)
								{
									b.size = a2;
									b.numbers = stall[i].numbers;
								}
							}
							else if (a.size == a2)
							{
								b = a;
								b.numbers += stall[i].numbers;
								a.size = a1;
								a.numbers = stall[i].numbers;
							}
							else //odd is zero
							{
								a.size = a1;
								a.numbers = stall[i].numbers;
								if (a2 > 0)
								{
									b.size = a2;
									b.numbers = stall[i].numbers;
								}
							}
						}

					}
					else
					{
						__int64 a1 = (stall[i].size - 1) / 2;
						if (a1 <= 0)
							continue;

						if (i == 0)
						{
							a.size = a1;
							a.numbers = stall[i].numbers * 2;
						}
						// must be even
						else if (a.size == a1)
						{
							a.numbers += stall[i].numbers * 2;
						}
						else if (b.size == a1)
						{
							b.numbers += stall[i].numbers * 2;
						}
					}
				}
			}

			stall[0] = a;
			stall[1] = b;

			
		} while (k > 0);
	}

}
