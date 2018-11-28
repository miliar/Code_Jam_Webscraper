#include <stdio.h>
#include <iostream>

using namespace std;

int num[10];
char col[] = "RYB";

int findMax()
{
	int max = 0;
	for(int i=0; i<3; i++)
		if(num[i] > max)
			max = num[i];
	return max;
}

int count(int x)
{
	int cnt = 0;
	for(int i=0; i<3; i++)
		if(num[i]==x)
			cnt++;
	return cnt;
}

int findSecondMax(int max)
{
	int sMax = 0;
	int idx = -1;
	for(int i=0; i<3; i++)
		if(num[i] < max && num[i] > sMax)
		{
			sMax = num[i];
			idx = i;
		}
	return idx;
}

int checkStr(string ss)
{
	int n = ss.size();
	if(ss[0] == ss[n-1])
		return 0;
	for(int i=0; i<n-2; i++)
		if(ss[i]==ss[i+1])
			return 0;
	return 1;
}

int main()
{
	int t;
	cin >> t;
	for(int tt = 1; tt <= t; tt++)
	{
		int n, r, o, y, g, b, v;
		cin >> n >> r >> o >> y >> g >> b >> v;
		num[0] = r;
		num[1] = y;
		num[2] = b;
		string ss;
		while(ss.size() < n)
		{
			int max = findMax();
			int cntMax = count(max);
			if(cntMax == 3)
			{
				int off = 0;
				if(ss.size()>0)
					off = (ss[0]=='R' ? 0 : (ss[0]=='Y' ? 1 : 2));
				for(int i=off; i<3+off; i++)
				{
					ss += col[i%3];
					num[i%3]--;
				}
			}
			else if(cntMax == 2)
			{
				int off = 0;
				if(ss.size()>0)
					off = (ss[0]=='R' ? 0 : (ss[0]=='Y' ? 1 : 2));
				for(int i=off; i<3+off; i++)
				{
					if(num[i%3]==max)
					{
						ss += col[i%3];
						num[i%3]--;
					}
				}
			}
			else // cntMax == 1
			{
				int sMaxId = findSecondMax(max);
				if(sMaxId != -1)
				{
					for(int i=0; i<3; i++)
					{
						if(num[i]==max)
						{
							ss += col[i];
							num[i]--;
							break;
						}
					}
					// insert second max
					ss += col[sMaxId];
					num[sMaxId]--;
				}
				else
				{
					for(int i=0; i<3; i++)
					{
						if(num[i]==max)
						{
							while(num[i])
							{
								ss += col[i];
								num[i]--;
							}
							break;
						}
					}
				}
			}
		}
		if(checkStr(ss))
			printf("Case #%d: %s\n", tt, ss.c_str());
		else
			printf("Case #%d: IMPOSSIBLE\n", tt);
	}
	return 0;
}