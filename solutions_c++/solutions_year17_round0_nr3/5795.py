// C.cpp : Defines the entry point for the console application.
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

typedef unsigned __int64 ulint;

#define FOR(i,n) for (int (i) = 0; (i) < (n); i++)

int getDistance(std::vector<bool> flags, int pos, int& max)
{
	int i = pos-1;
	while (i >= 0 && !flags[i])
		i--;
	int left = pos - i - 1;

	i = pos+1;
	while (i < flags.size() && !flags[i])
		i++;
	int right = i - pos - 1;

	max = std::max(left, right);
	return std::min(left, right);
}

void simple_resolve(ulint n, ulint k, int &r1, int &r2)
{
	std::vector<bool> flags;
	for (int i = 0; i < n; i++)
		flags.push_back(false);

	for (int i = 0; i < k; i++)
	{
		int maxmin = -1;
		int pos = -1;
		int maxmax = -1;
		for (int j = 0; j < flags.size(); j++)
		{
			if (!flags[j])
			{
				int tmpmax = -1;
				int dis = getDistance(flags, j, tmpmax);
				if (dis > maxmin || (dis == maxmin && tmpmax > maxmax))
				{
					maxmin = dis;
					pos = j;
					maxmax = tmpmax;
				}
			}
		}

		flags[pos] = true;

		if (i == k-1)
		{
			r1 = maxmax;
			r2 = maxmin;
		}
	}
}

int main(void)
{
    //freopen("E:\\CodeJam\\C\\x64\\Debug\\in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
	//ios::sync_with_stdio(false);

    int t = 0;
    std::cin >> t;
    
    FOR(i,t)
    {
		ulint n, k;
		std::cin >> n >> k;

		int r1, r2;

		simple_resolve(n, k, r1, r2);

        std::cout << "Case #" << i+1 << ": " << r1 << ' ' << r2 << std::endl;
    }

	return 0;
}

