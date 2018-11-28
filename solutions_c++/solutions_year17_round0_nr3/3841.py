#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <iostream>
#include <deque>
#include <algorithm>
#include <vector>
#include <ctime>

using namespace std;

int main()
{
	int n;
	freopen("C-small-2.in","r",stdin);
	freopen("C-small-2.out","w",stdout);
	cin>>n;
	int i,j,k;
	for (i=0;i<n;i++)
	{
		long long p,q;
		cin>>p>>q;
		long long div1,div2;
		long long dcount1,dcount2;
		if (p%2 == 1)
		{
			div1 = p/2;
			dcount1 = 2;
			div2 = 0;
			dcount2 = 0;
		}
		else
		{
			div1 = p/2;
			dcount1 = 1;
			div2 = p/2-1;
			if (div2 < 0) div2 = 0;
			dcount2 = 1;
		}
		q--;
		long long cur=2;
		while (q > cur)
		{
			if (div1 % 2 == 1)
			{
				int t1 = dcount1 * 2 + dcount2;
				int t2 = dcount2;
				dcount1 = t1;
				dcount2 = t2;
				div1 = div1/2;
				div2 = div1>1?div1-1:0;
			}
			else
			{
				int t1 = dcount1;
				int t2 = dcount1 + dcount2 * 2;
				dcount1 = t1;
				dcount2 = t2;
				div1 = div1/2;
				div2 = div1>1?div1-1:0;
			}
			q -= cur;
			cur *= 2;
		}
		int ansmax,ansmin;
		if (q == 0)
		{
			ansmax = div1;
			ansmin = dcount2>0?div2:div1;
			ansmin = ansmin<0?0:ansmin;
		}
		else
		if (q <= dcount1)
		{
			ansmax = div1/2;
			ansmin = div1%2==1?ansmax:ansmax-1;
			ansmin = ansmin<0?0:ansmin;
		}
		else
		{
			ansmax = div2/2;
			ansmin = div2%2==1?ansmax:ansmax-1;
			ansmin = ansmin<0?0:ansmin;
		}
		printf("Case #%d: %d %d\n",i+1,ansmax,ansmin);
	}
	return 0;
}
