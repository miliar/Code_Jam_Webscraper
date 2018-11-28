#include <iostream>
#include <fstream>
#include <string>

using namespace std;

inline bool isStrInclM(string s)
{
	for (int i = 0; i < s.length(); i++)
	{
		if (s[i] == '-')
			return true;
	}
	return false;
}

inline void reverse(string& s, int k,int position)
{
	for (int i=position; i < position + k; i++)
	{
		if (s[i] == '-')
		{
			s[i] = '+';
			continue;
		}
		if (s[i] == '+') s[i] = '-';
	}
}

int main()
{
	string str;
	int T;
	int K;
	int i = 1;
	int counter = 0;
	ifstream fin("A-large.in");
	ofstream fout("output.out");
	fin >> T;
	while (i <= T)
	{
		fin >> str >> K;
		if (!isStrInclM(str))
		{
			fout << "Case #" << i << ": " << 0 << endl;
			i++;
			continue;
		}
		for (int j = 0; j < str.length()-K+1; j++)
		{
			if (str[j]=='-')
			{
				reverse(str, K, j);
				counter++;
			}
		}
		if (isStrInclM(str))
		{
			fout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
			i++;
			counter = 0;
			continue;
		}
		fout << "Case #" << i << ": " << counter << endl;
		counter = 0;
		i++;
	}
	fin.close();
	fout.close();

	return 0;
}