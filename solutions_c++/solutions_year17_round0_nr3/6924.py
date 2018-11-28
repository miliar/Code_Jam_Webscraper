#include <bits/stdc++.h>

using namespace std;

int main(void)
{
	ifstream f("C-small-2-attempt0.in");
	ofstream f2("out2.txt");
	int t, T;	
	f >> t;
	T = t;
	while(t--)
	{
		int n, k, m;
		f >> n >> k;
		int co[n+1] = {0}, pos = n;
		co[n] = 1;
		for(int i = 0; i < k; ++i)
		{			
			while(co[pos] == 0)
			{
				--pos;
			}
			--co[pos];
			if(pos%2 == 1)
			{
				co[pos/2] += 2;
			}
			else
			{
				++co[pos/2];
				++co[pos/2 - 1];
			}
		}
		f2 << "Case #" << T - t << ": ";
		if(pos%2 == 1)
		{
			f2 << pos/2 << ' ' << pos/2 << endl;
		}
		else
		{
			f2 << pos/2 << ' ' << pos/2 - 1 << endl;
		}
	}
}
