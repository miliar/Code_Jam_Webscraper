#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
#include <algorithm>
#include <map>
#include <queue>
#include <stack>
#include <vector>
#include <fstream>

using namespace std;

bool isTidy(int N)
{
	string str;
	stringstream out;
	out << N;
	out >> str;

	bool res = true;
	for(int i = 1; i < str.size(); ++i)
	{
		if(str[i] < str[i-1])
		{
			res = false;
			break;
		}
	}

	return res;
}

bool isTidy(string str)
{
	bool res = true;
	for(int i = 1; i < str.size(); ++i)
	{
		if(str[i] < str[i-1])
		{
			res = false;
			break;
		}
	}

	return res;
}

string format(string str)
{
	int i = 0;
	while(i < str.size() && str[i] == '0'){ i++; }

	if(i < str.size())
	{
		return str.substr(i, str.size() - i);
	}

	return "0";
}

int main(int argc, char* argv[])
{
	freopen("in.txt", "r+", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	cin >> T;

	for(int t = 0; t < T; ++t)
	{
		/*
		int N;
		cin >> N;

		
		for(int i = N; i >= 1; --i)
		{
			bool b = isTidy(i);
			if(b)
			{
				cout << "Case #" << (t + 1) << ": " << i << endl;
				break;
			}
		}
		*/

		string str;
		cin >> str;

		for(int i = str.size() - 2; i >= 0; --i)
		{
			if(str[i] > str[i+1])
			{
				int n = (int)(str[i] - '0');
				--n;
				for(int j = i + 1; j < str.size(); ++j)
				{
					str[j] = '9';
				}

				str[i] = char(n + '0');
			}
		}

		cout << "Case #" << (t + 1) << ": " << format(str) << endl;

	}

	return 0;
}