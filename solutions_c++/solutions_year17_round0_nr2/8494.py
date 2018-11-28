#include <string>
#include <iostream>

using namespace std;

bool isTidy(unsigned long long const &N)
{
	string s = to_string(N);
	bool tidy = true;
	for (int i = s.length() - 1; i > 0; i--)
	{
		if (s[i] < s[i - 1])
		{
			tidy = false; 
			break;
		};
	}
	return tidy;
}

int firstUntidy(string const &line)
{
	for (int i = 0; i < line.length(); i++)
	{
		if (line[i+1] < line[i])
		{
			int j = i;
			while (line[j] == line[i] && j > 0) j--;
			return j;
		}
	}
	return 0;
}

int getUntidyInfo(unsigned long long const &N)
{
	string s = to_string(N);
	return s.length() - 1 - firstUntidy(s) - 1;
}

void main()
{
	int T;
	unsigned long long N;
	cin >> T;
	for (auto i = 0; i < T; i++)
	{
		cin >> N;
		unsigned long long NewN = N;
		while (!isTidy(NewN))
		{
			NewN -= (NewN % unsigned long long(pow(10, getUntidyInfo(NewN))) + 1);
		}
		cout << "Case #" << i+1 << ": " << NewN << endl;
	}
}