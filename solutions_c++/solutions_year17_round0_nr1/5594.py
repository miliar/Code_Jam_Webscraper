// A.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <bitset>
#include <unordered_map>
#include <unordered_set>

#include "bigInt.h"
// BigInt::Rossi n1 ("314159265358979323846264338327950288419716939937510", BigInt::DEC_DIGIT);
// int stoi (const string& str, size_t* idx = 0, int base = 10);
// string to_string (val);

using namespace std;

#define FOR(i,n) for (int (i) = 0; (i) < (n); i++)
#define unsigned __int64 ulint
#define __int64 lint

int simple_resolve(int k, std::string &s)
{
	std::vector<bool> flags;
	for (int i = 0; i < 1024; i++)
		flags.push_back(false);

	int flip = (1 << k) -1;

	int code = 0;
	int len = s.length();
	for (int i = 0; i < len; i++)
	{
		if ('-' == s.at(i))
			code = code | (1 << i);
	}

	int step = 0;
	bool success = false;

	std::vector<int> st;
	st.push_back(code);
	flags[code] = true;

	while (!st.empty())
	{
		std::vector<int> tmpSt;

		for (int t : st)
		{
			if (0 == t)
			{
				success = true;
				break;
			}

			for (int i = 0; i < len-k+1; i++)
			{
				int newstatus = t^(flip << i);
				if (!flags[newstatus])
				{
					flags[newstatus] = true;
					tmpSt.push_back(newstatus);
				}
			}
		}

		if (success)
			break;
		else
		{
			st.swap(tmpSt);
			step++;
		}
	}

	if (success)
		return step;
	else
		return -1;
}

int resolve(int k, std::string &s)
{
	int res = 0;

	std::vector<bool> st;
	int len = s.length();
	for (int i = 0; i < len; i++)
	{
		if ('+' == s.at(i))
			st.push_back(true);
		else
			st.push_back(false);
	}

	int i = 0;
	while (i < len)
	{
		if (st[i])
			i++;
		else
		{
			if (i+k > len)
			{
				res = -1;
				break;
			}

			for (int j = 0; j < k; j++)
			{
				st[i+j] = !st[i+j];
			}

			i++;
			res++;
		}
	}

	return res;
}

int main(void)
{
    //freopen("E:\\CodeJam\\A\\x64\\Debug\\in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
	//ios::sync_with_stdio(false);

    int t = 0;
    std::cin >> t;
    
    FOR(i,t)
    {
        std::string s;
		int k;
        cin >> s >> k;

        //int res = simple_resolve(k, s);
		int res = resolve(k, s);

		if (res < 0)
			std::cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << std::endl;
		else
			std::cout << "Case #" << i+1 << ": " << res << std::endl;
    }

	return 0;
}

