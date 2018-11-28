#define _CRT_SECURE_NO_WARNINGS
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <string>
#include <set>
#include <vector>
#include <stack>
#include <deque>
#include <math.h>
#include <map>
#include <fstream>
#include <iomanip>
#include <queue>
#include <bitset>

using namespace std;

typedef long long ll;
#define mp make_pair
#define N 100001
#define INF 1000000000000000000

const int c = 1E9 + 7;

bool comp(pair<int, int> a, pair<int, int> b)
{
	return a.second < b.second;
}

vector<int> digits[101];

void digitize(ll k, int tc)
{
	ll z = k;
	while (z)
	{
		int b = z % 10;
		z /= 10;
		digits[tc].push_back(b);
	}
	reverse(digits[tc].begin(), digits[tc].end());
}

int main()
{
	ofstream out;
	out.open("output.txt");
	int t;
	cin >> t;
	ll k;
	for (int i = 1; i <= t; ++i)
	{
		cin >> k;
		out << "CASE #" << i << ": ";
		bool flag = false;
		int j = 0, pos = 0;
		string s;
		digitize(k, i);
		for (j = 1; j < digits[i].size(); ++j)
		{
			if (digits[i][j] >= digits[i][j - 1])
			{
				s += digits[i][j - 1] + 48;
				if (digits[i][j] > digits[i][j - 1])
					pos = j;
			}
			else
			{
				flag = true;
				break;
			}
		}
		if (flag)
		{
			for (int l = 0; l < pos; ++l)
				out << digits[i][l];
			if (digits[i][pos] - 1)
				out << digits[i][pos] - 1;
			for (int l = pos + 1; l < digits[i].size(); ++l)
				out << 9;
			out << endl;
		}
		else
			out << s << digits[i][digits[i].size() - 1] << endl;
	}
	return 0;
}