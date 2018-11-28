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
	freopen("B-small-attempt3.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
}
bool sorted(string str)
{
	string st = str;
	sort(st.begin(), st.end());
	if (st.compare(str) == 0)
		return true;
	return false;
}
void check(string &str)
{
	int num;
	while (!(sorted(str)))
	{
		num = stoi(str);
		num--;
		stringstream ss;
		ss << num;
		str = ss.str();
	}
}
int main()
{
	f();
	in_out_txt();
	int t;
	cin >> t;
	string n, str;
	for (int i = 0; i < t; i++)
	{
		cin >> n;
		if (n.length() == 1)
			cout << "Case #" << i + 1 << ": " << n << endl;
		else
		{
			check(n);
			cout << "Case #" << i + 1 << ": " << n << endl;
		}
	}
	//system("pause");
	return 0;
}