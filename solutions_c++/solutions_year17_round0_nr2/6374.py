
#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

void allNine(string& s, int l)
{
	for (int i = l; i < s.length(); ++i)
		s[i] = '9';
}

void decI(string& s, int i)
{
	if (s[i] == '0')
	{
		allNine(s, i);
		decI(s, i - 1);
	}
	else if (s[i] == '1')
	{
		if (!i)
		{
			s = s.substr(1, s.size() - 1);
			allNine(s, 0);
		}
		else
		{
			--s[i];
			allNine(s, i + 1);
		}
	}
	else
	{
		--s[i];
		allNine(s, i + 1);
	}
}

int main()
{
	int T;
	ifstream in("B-large.in", ios_base::in);
	ofstream out("b.out", ios_base::out);
	in >> T;
	for (int t = 1; t <= T; ++t)
	{
		string n;
		in >> n;
		for (int i = 1; i < n.length(); ++i)
		{
			if (n[i] < n[i - 1])
			{
				decI(n, i - 1);
				i = max(0, i - 2);
			}
		}
		out << "Case #" << t << ": " << n << endl;
	}
	system("pause");
	return 0;
}
