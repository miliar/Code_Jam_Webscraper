#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	ifstream fin("input.in");
	ofstream fout("output.out");

	int t;

	fin >> t;

	for (int test = 0; test < t; test++)
	{
		string s;
		int k;

		fin >> s >> k;
		int ans = 0;
		for (int i = 0; i < s.size() - k; i++)
		{
			if (s[i] == '-')
			{
				for (int j = i; j < i + k; j++)
				{
					if (s[j] == '-') s[j] = '+'; else s[j] = '-';
				}
				ans++;
			}
		}

		bool poss = true;
		for (int i = s.size() - k; i < s.size() - 1; i++)
		{
			if (s[i] != s[i + 1]) poss = false;
		}


		if (poss == true)
		{
			if (s[s.size() - 1] == '-')
			{
				fout << "Case #" << test + 1 << ": " << ans + 1 << endl;
			}
			else fout << "Case #" << test + 1 << ": " << ans << endl;
		}
		if (poss == false) fout << "Case #" << test + 1 << ": " << "IMPOSSIBLE" << endl;

	}

	fin.close();
	fout.close();

	return 0;
}