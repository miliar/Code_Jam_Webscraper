#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <fstream>
using namespace std;

int main()
{

	ifstream cin("in.txt");
	ofstream cout("out.txt");

	int n;
	cin >> n;

	for (int f = 0; f < n; ++f)
	{
		string s;
		cin >> s;
		int k;
		cin >> k;

		int q = 0;
		for (int i = s.size() - 1; i >= k - 1; --i)
		{
			if (s[i] == '-')
			{
				q++;
				for (int j = i; j > i - k; --j)
					s[j] = s[j] == '+' ? '-' : '+';
			}
		}

		bool kek = 1;
		for (int i = 0; i < s.size(); ++i)
		{
			if (s[i] == '-')
				kek = 0;
		}

		cout << "Case #" << f + 1 << ": ";
		if (kek)
			cout << q;
		else
			cout << "IMPOSSIBLE";

		cout << endl;
			
	}
	return 0;
}