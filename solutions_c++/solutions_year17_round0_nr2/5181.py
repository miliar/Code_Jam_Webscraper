// GCJ.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <fstream>
#include <cmath>

using namespace std;

int query;

vector<int> check(long long a)
{
	vector<int> ra;
	while (a != 0)
	{
		ra.push_back(a % 10);
		a /= 10;
	}
	reverse(ra.begin(), ra.end());
	return ra;
}

long long get10(int a)
{
	long long res = 1;
	for (int i = 0; i < a; ++i)
	{
		res *= 10;
	}
	return res;
}

int main()
{
	ofstream cout("small_output.txt");
	ifstream cin("inp.in");

	cin >> query;
	for (int asd = 0; asd < query; ++asd)
	{
		long long n;
		cin >> n;

		vector<int> r = check(n);

		for (int i = 0; i < r.size() - 1; ++i)
		{
			if (r[i] > r[i + 1])
			{
				for (int j = i + 1; j < r.size(); ++j)
				{
					r[j] = 9;
				}
				int j = i;
				while (j > 0 && r[j] == r[j - 1])
				{
					--j;
				}
				++j;
				for (int k = j; k <= i; ++k)
				{
					r[k] = 9;
				}
				--r[j - 1];
				break;
			}
		}

		long long res = 0;
		for (int i = 0; i < r.size(); ++i)
		{
			res += r[i] * get10(r.size() - i - 1);
		}

		cout << "Case #" << (asd + 1) << ": ";
		cout << res;
		cout << endl;
	}
    return 0;
}

