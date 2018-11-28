#include <bits/stdc++.h>
using namespace std;
int main ()
{
	ifstream fin;
	ofstream fout;
	fin.open("input.in");
	fout.open("output.txt");
	int t, k, res, x, y, len, flag, i;
	string s;
	fin >> t;
	for (i=1; i<=t; i++)
	{
		fin >> s >> k;
		res = flag = 0;
		len = s.length();
		for (x=0; x<=(len-k); x++)
		{
			if (s[x]=='-')
			{
				for (y=0; y<k; y++)
				{
					if (s[y+x]=='+')
						s[y+x] = '-';
					else
						s[y+x] = '+';
				}
				res++;
			}
		}
		for (x=len-k+1; x<len; x++)
		{
			if (s[x]=='-')
			{
				flag = 1;
				break;
			}
		}
		if (flag==0)
			fout << "Case #" << i << ": " << res << endl;
		else
			fout << "Case #" << i << ": IMPOSSIBLE" << endl;
	}
	fin.close();
	fout.close();
	return 0;
}
