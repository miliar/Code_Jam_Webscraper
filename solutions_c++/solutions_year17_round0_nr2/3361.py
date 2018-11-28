
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

int main(void)
{
	int t;
	long long n;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i)
	{
		string ret;
		cin >> n;  // read n.
		string str = to_string(n);
		int size = str.size();
		int index = 0;
		int j = 0;
		for (; j < size - 1; ++j)
		{
			if (str[j] > str[j + 1])
			{
				index = j;
				while (index > 0 && str[index] == str[index - 1])
				{
					--index;
				}
				break;
			}
		}
		if (j == size - 1)
		{
			ret = str;
		}
		else
		{
			if (index == 0 && str[0] == '1')
			{
				ret.assign(size - 1, '9');
			}
			else
			{
				ret = str;
				--ret[index];
				for (int j = index + 1; j < size; ++j)
				{
					ret[j] = '9';
				}
			}
		}
		cout << "Case #" << i << ": " << ret.c_str() << endl;
	}
	return 0;
}