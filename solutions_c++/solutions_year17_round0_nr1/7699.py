#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
#include <algorithm>
#include <map>
#include <queue>
#include <stack>
#include <vector>
#include <fstream>

using namespace std;

bool check(string str)
{
	for(int i = 0; i < str.size(); ++i)
	{
		if(str[i] != '+')
			return false;
	}

	return true;
}

void flip(string& _str, int _i, int _K)
{
	for(int i = _i; i < _K; ++i)
	{
		if(_str[i] == '+')
			_str[i] = '-';
		else
			_str[i] = '+';
	}
}

int main(int argc, char* argv[])
{
	freopen("in.txt", "r+", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	cin >> T;

	for(int t = 0; t < T; ++t)
	{
		string str;
		cin >> str;

		int K;
		cin >> K;
		int i = (int)str.size() - 1;

		int res = 0;
		bool f = false;
		while(i >= 0)
		{
			if(i + K <= str.size())
			{
				if(str[i + K - 1] != '+')
				{
					flip(str, i, i + K);
					res++;
				}
				else
				{
					--i;
				}
			}
			else
			{
				--i;
			}

		}

		if( check(str) )
		{
			cout << "Case #" << (t + 1) << ": " << res << endl;
		}
		else
		{
			cout << "Case #" << (t + 1) << ": " << "IMPOSSIBLE" << endl;
		}
	}

	return 0;
}