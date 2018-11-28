#include <iostream>
#include <vector>
#include <queue>
#include <deque>
#include <utility>
#include <cmath>
#include <list>
#include <string>
#include <fstream>
#define mp make_pair
#define pb push_back

using namespace std;

int main()
{
	ifstream in;
	in.open("A-large.in");
	ofstream out;
	out.open("A-large.out");
	int q;
	in >> q;
	for (int w = 0; w < q; w++)
	{
		out << "Case #" << w + 1 << ": ";
		int q = 0;
		string s;
		in >> s;
		int n;
		in >> n;
		int sz = s.size();
		int cm = 0;
		for (int i = 0; i < sz; i++)
		{
			if (s[i] == '-')
				cm++;
		}
		if (cm == 0)
		{
			out << 0 << endl;
			continue;
		}
		else
		{
			if (cm == 1)
			{
				out << "IMPOSSIBLE" << endl;
				continue;
			}
			if (cm == sz && sz%n == 0)
			{
				out << sz / n << endl;
				continue;
			}
			s = s.substr(s.find('-'));
			int count = 0;
			int min = 1;
			while (s.size() >= n)
			{	
				for (int i = 0; i < n; i++)
				{
					if (s[i] == '-') s[i] = '+';
					else s[i] = '-';
				}
				count++;
				min = s.find('-');
				if (min == -1)
				{
					out << count << endl;
					break;
				}
				else
					s = s.substr(min);
			}
			if (min == -1)
				continue;
			else
			{
				out << "IMPOSSIBLE" << endl;
			}
		}
	}
	return 0;
}