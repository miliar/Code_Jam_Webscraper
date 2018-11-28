
#include <string>
#include <fstream>
//#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
	ifstream in("B-large.in");
	ofstream out("out.txt");
	int n;
	in >> n;
	for (int i = 0; i < n; ++i)
	{
		string s;
		in >> s;

		for (int x = s.size() - 1; x >= 1; --x)
		{
			if (s[x-1] > s[x])
			{
				for (int c = x; c<s.size(); ++c)
				s[c] = '9';
				s[x - 1]--;
			}
		}

		if (s[0] == '0') s.erase(s.begin());

		out << "Case #" << (i + 1) << ": " << s << endl;
	}

	return 0;
}

