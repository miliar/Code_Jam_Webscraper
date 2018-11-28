#include <iostream>
#include <queue>
#include <fstream>
#include <vector>
#include <string>
#include <cstring>
#include <map>
using namespace std;

bool isTidy(int64_t in)
{
	int old = 10;
	while (in)
	{
		if (in % 10 > old)
			return false;
		old = in % 10;
		in /= 10;
	}
	return true;
}

int64_t maxTidy(int64_t in)
{
	vector<int> rem;
	while (in)
	{
		rem.insert(rem.begin(), in % 10);
		in /= 10;
	}
	int old = 0;
	for (int i = 0; i < rem.size(); i++)
	{
		if (rem[i] < rem[old])
		{
			break;
		}
		old = i;
	}

	for (int i = old + 1; i < rem.size(); i++)
		rem[i] = 9;

	while (old > 0 && rem[old]-- == rem[old - 1])
	{
		rem[old] = 9;
		old--;
	}
	if (old == 0)
	{
		rem[0]--;
	}
	int64_t ret = 0;

	for (auto i : rem)
	{
		ret *= 10;
		ret += i;
	}
	return ret;
}

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

int64_t p2(ifstream& ifs, ofstream& ofs)
{
	int64_t N;
	ifs >> N;
	if (isTidy(N))
		return N;
	else 
		return maxTidy(N);
	
}

int main()
{
	ifstream ifs;
	ofstream ofs;
	ifs.open("input1");
	ofs.open("output");

	int T;
	ifs >> T;
	for (int i = 1; i <= T; i++)
	{
		ofs << "Case #" << i << ": " << p2(ifs, ofs) << endl;

	}
	return 0;
}

