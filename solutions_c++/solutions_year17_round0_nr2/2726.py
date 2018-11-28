#include <iostream>
#include <string>
#include <vector>

using namespace std;


string max_tidy_num(string & s)
{
	string ret = "";
	int i=0;
	for (; i<s.size(); i++)
	{
		ret.push_back(s[i]);
		if (i<s.size()-1 && s[i] > s[i+1])
		{
			break;
		}
	}

	if (i<s.size()-1)
	{
		int j=i;
		while (true)
		{
			if (j==0 || ret[j] > ret[j-1])
			{
				ret[j]--;
				break;
			}
			else
			{
				ret[j] = '9';
				j--;
			}
		}
	}

	for (i++; i<s.size(); i++)
	{
		ret.push_back('9');
	}
	if (ret[0] > '0')
		return ret;
	else
		return ret.substr(1,ret.size());
}

int main()
{
	int T;

	cin >> T;
	for (int i=0; i<T; i++)
	{
		string s;
		vector<char> v;
		cin >> s;

		cout << "Case #" << i+1 << ": ";
		cout << max_tidy_num(s) << endl;
	}
	return 0;
}