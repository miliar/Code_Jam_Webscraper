
#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

void rev(string& s, int l, int k)
{
	for (int i = l; i < l + k; ++i)
		s[i] = s[i] == '+' ? '-' : '+';
}

int main()
{
	int T;
	ifstream in("A-large.in", ios_base::in);
	ofstream out("a.out", ios_base::out);
	in >> T;
	for(int t = 1; t <= T; ++t)
	{
		string s;
		int k;
		int res = 0;
		int curN = 0, curP = 0;
		int lastI = 0;

		in >> s >> k;
		for (int i = 0; i < s.length(); ++i)
		{
			if (s[i] == '-')
				++curN;
			else
			{
				if (curN > 0)
					++curP;
				else
				    lastI = i - 1;
			}
			if (curN == k)
			{
				lastI = i - 1;
				++res;
				rev(s, i - k + 1, k);
				curN = curP = 0;
			}
			else if (curN + curP == k)
			{
				++res;
				rev(s, i - k + 1, k);
				i = lastI;
				curN = curP = 0;
			}
		}
		for (int i = 0; i < s.length(); ++i)
		{
			if (s[i] == '-')
			{
				res = -1;
				break;
			}
		}
		out << "Case #" << t << ": ";
		if (res < 0)
			out << "IMPOSSIBLE\n";
		else
			out << res << endl;
	}
	system("pause");
	return 0;
}
