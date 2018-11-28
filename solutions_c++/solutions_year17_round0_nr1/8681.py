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

ll dp[2][5001][5001];
int n, m, k;

int main()
{
	ofstream out;
	out.open("output.txt");
	int t;
	cin >> t;
	int k;
	string s;
	for (int i = 1; i <= t; ++i)
	{
		cin >> s >> k;
		int len = s.length(), cnt = 0;
		for (int j = 0; j < len - k + 1; ++j)
		{
			if (s[j] == '-')
			{
				for (int l = 0; l < k; ++l)
				{
					if (s[j + l] == '-')
						s[j + l] = '+';
					else
						s[j + l] = '-';
				}
				cnt++;
			}
		}
		bool flag = false;
		for (int j = len - k; j < len; ++j)
		{
			if (s[j] == '-')
			{
				out << "CASE #" << i << ": IMPOSSIBLE" << endl;
				flag = true;
				break;
			}
		}
		if (!flag)
			out << "CASE #" << i << ": " << cnt << endl;
	}
	cin >> t;
	return 0;
}