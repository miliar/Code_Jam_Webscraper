#include<iostream>
#include<fstream>
#include<vector>
#include<string>

using namespace std;

int main()
{
	ifstream fin;
	fin.open("input.txt");
	ofstream fout;
	fout.open("output.txt");
	long long t;
	fin >> t;
	fin.ignore();
	for (long long i = 0; i < t; i++)
	{
		long long pos = 0;
		long long neg = 0;
		string input;
		string k_str;
		getline(fin, input);

		for (long long j = 0; j < input.length(); j++)
		{
			if (input[j] == ' ')
			{
				k_str = input.substr(j + 1, input.length() - 1 - j);
				input.resize(j);
			}
		}

		long long ans = 0;
		long long k = stoi(k_str);
			for (long long j = 0; j <= input.length() - k; j++)
			{
				if (input[j] == '-')
				{
					for (long long l = j; l < j + k; l++)
					{
						if (l < input.length())
						{
							if (input[l] == '-')
								input[l] = '+';
							else
								input[l] = '-';
						}
					}
					ans++;
				}
			}
			
			
				bool found = false;
				for (long z = 0; z < input.length(); z++)
					if (input[z] == '-')
						found = true;
				if (i < t - 1)
				{
					if (ans == 0 && found == false)
					{
						fout << "Case #" << i + 1 << ": 0" << char(10);
					}
					else
					{
						if (found == false)
							fout << "Case #" << i + 1 << ": " << ans << char(10);
						else
							fout << "Case #" << i + 1 << ": IMPOSSIBLE" << char(10);
					}
				}
				else
				{
					if (ans == 0 && found == false)
					{
						fout << "Case #" << i + 1 << ": 0" ;
					}
					else
					{
						if (found == false)
							fout << "Case #" << i + 1 << ": " << ans;
						else
							fout << "Case #" << i + 1 << ": IMPOSSIBLE";
					}
				}

		}

	return 0;
}
