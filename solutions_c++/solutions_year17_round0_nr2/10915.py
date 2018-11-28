#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<string>
#include<cstring>
#include<fstream>
using namespace std;
typedef long long ll;
bool ok(string s)
{
	for (int i = 1; i < s.size(); i++)
		if (s[i] < s[i - 1])return false;
	return true;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, n, i = 1;
	cin >> t;
	while (t--)
	{
		cin >> n;
		while (!ok(to_string(n)))n--;
		cout << "Case #" << i << ": ";
		cout << n << endl;
		i++;
	}
	return 0;
}