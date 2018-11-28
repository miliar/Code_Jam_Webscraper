#include <fstream>
#include <iostream>
#include <string>
#include <cstring>

using namespace std;

flip(char* s, int k)
{
	int i;
	for(i = 0; i < k; i++)
	{
		s[i] = s[i] ^ 6;
	}
}

int solve(string str, int K)
{
	int count = 0;
	char * s = new char [str.length()+1];
	std::strcpy (s, str.c_str());
	int i;
	for(i = 0; i < str.length() - K + 1; i++)
	{
		if(s[i] == '-')
		{
			flip(&s[i], K);
			count++;
		}
	}
	for(;i < str.length(); i++)
	{
		if(s[i] == '-')
			return -1;
	}
	return count;
}

int main()
{
	int K;
	int T;
	ifstream cin("A-large.in", ifstream::in);
	ofstream cout("A-large.out", ofstream::out);
	cin >> T;
	string s;
	int i;
	for(i = 1; i <= T; i++)
	{
		cin >> s;
		cin >> K;
		int result = solve(s, K);
		cout << "Case #" << i << ": ";
		if(result == -1)
		{
			cout << "IMPOSSIBLE" << endl;
		}
		else
		{
			cout << result << endl;
		}
	}
	return 0;
}