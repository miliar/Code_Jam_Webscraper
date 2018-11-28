#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<sstream>
#include<vector>
#include<algorithm>
#include<set>
#include<fstream>
#include<map>
#include<string>
#include <stdio.h>
#include<bitset>
#include<queue>
#include<iomanip>
#include<cmath>

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<ll>vl;
typedef vector<int>vi;
typedef vector<bool>vb;
typedef vector<char>vc;
typedef vector<string>vs;

void f()
{
	std::ios_base::sync_with_stdio(0);
	cin.tie(NULL); cout.tie(NULL);
}

#pragma warning (disable : 4996)
void in_out_txt()
{
	freopen("A-large.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
}
bool check(string str, int n, int &cnt)
{
	string st;
	int c;
	for (int i = 0; i <= str.length() - n; i++)
	{
		if (str[i] == '-')
		{
			c = 0;
			cnt++;
			for (int j = i; j < str.length() && c != n; j++)
			{
				c++;
				if (str[j] == '-')
					str[j] = '+';
				else
					str[j] = '-';
			}
		}
	}
	if (str.find('-')!=-1)
		return false;
	return true;
}
int main()
{
	f();
	in_out_txt();
	int t;
	cin >> t;
	string str;
	int n;
	for (int i = 0; i < t; i++)
	{
		cin >> str >> n;
		int cnt = 0;
		bool f = check(str, n, cnt);
		if (f)
			cout << "Case #" << i + 1 << ": " << cnt << endl;
		else
			cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
	}
	//system("pause");
	return 0;
}