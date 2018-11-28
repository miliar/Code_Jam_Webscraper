#include<iostream>
#include<algorithm>
#include<fstream>
#include<string>
#include<vector>
#include<queue>
using namespace std;

int test;
string s;
bool done;

int main()
{
	ifstream in("B-large.in");
	ofstream out("output.txt");
	in >> test;
	for (int t = 1; t <= test; ++t)
	{
		in >> s;
		int n = (int)s.size();
		int pos = n;
		
		while (1)
		{
			--pos;

			done = true;
			for (int i = 1; i < n; ++i)
			{
				if (s[i] < s[i - 1])
				{
					done = false;
					break;
				}
			}

			if (done)
				break;

			s[pos] = '9';
			for (int i = pos - 1; i >= 0; --i)
			{
				if (s[i] == '0')
					s[i] = '9';
				else
				{
					s[i]--;
					break;
				}
			}
		}

		int nonzero = 0;
		for (int i = 0; i < (int)s.size(); ++i)
		{
			if (s[i] != '0')
			{
				nonzero = i;
				break;
			}
		}

		out << "Case #" << t << ": " << s.substr(nonzero) << endl;
	}

	in.close();
	out.close();
	return 0;
}