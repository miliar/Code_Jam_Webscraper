#include<iostream>
#include<string>
#include<fstream>
using namespace std;
char flip(char c)
{
	if (c == '-')return '+';
	return '-';
}
int main()
{
	/*ifstream input;
	input.open("A-large.in");
	ofstream output;
	output.open("pancakes_output.txt");*/
	int t, flipper, res;
	string s;
	cin >> t;
	for (int test = 0; test < t; test++)
	{
		res = 0;
		cin >> s >> flipper;
		for (int i = 0; i < s.size() - flipper +1; i++)
		{
			if (s[i] == '-')
			{
				for (int j = 0; j < flipper; j++)
				{
					s[i + j] = flip(s[i + j]);
				}
				res++;
			}
		}
		bool impossible = 0;
		for (int i = 0; i < s.size(); i++)
		{
			if (s[i] == '-')
			{
				impossible = true;
				break;
			}
		}
		cout << "Case #" << test + 1 << ": ";
		if (impossible)cout << "IMPOSSIBLE";
		else cout << res;
		if (test != t - 1)cout << "\n";

		/*output << "Case #" << test + 1 << ": ";
		if (impossible)output << "IMPOSSIBLE";
		else output << res << "";
		if (test != t - 1)output << "\n";*/
	}
}