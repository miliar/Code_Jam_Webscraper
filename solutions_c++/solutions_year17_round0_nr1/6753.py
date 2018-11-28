#include <iostream>
#include <queue>
#include <fstream>
#include <vector>
#include <string>
#include <cstring>
#include <map>
using namespace std;

int p1(ifstream& ifs)
{
	string s;
	int k;
	ifs >> s;
	ifs >> k;
	int res = 0;
	for (int i = 0; i <= s.size() - k; i++)
	{
		if (s[i] == '-')
		{
			res++;
			for (int j = 0; j < k; j++)
				if (s[i + j] == '+')
					s[i + j] = '-';
				else s[i + j] = '+';
		}
	}
	for (int i = 0; i < s.size(); i++)
	{
		if (s[i] == '-')
			return -1;
	}
	return res;
}

int main()
{
	ifstream ifs;
	ofstream ofs;
	ifs.open("input4");
	ofs.open("output");

	int T;
	ifs >> T;
	for (int i = 1; i <= T; i++)
	{
		int ret = p1(ifs);
		if (ret == -1)
			ofs << "Case #" << i << ": IMPOSSIBLE" << endl;
		else
			ofs << "Case #" << i << ": " << ret << endl;
	}
	return 0;
}

