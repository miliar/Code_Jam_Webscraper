#include <iostream>
#include<string>
using namespace std;

string Solve(string s)
{
	int n = s.size();
	char *res = new char[n+1];
	res[n] = '\0';
	res[n - 1] = s[n - 1];
	for (int i = n - 2; i >= 0; i--)
	{
		if (s[i] > res[i + 1])
		{
			res[i] = s[i] - 1;
			for (int j = i + 1; j < n; j++) res[j] = '9';
		}
		else res[i] = s[i];
	}
	if (res[0] == '0') return string(&res[1]);
	else return string(res);
}

int main()
{
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		string s;
		cin >> s;
		cout<<"Case #"<<i<<": "<< Solve(s) << endl;
	}
	return 0;
}

