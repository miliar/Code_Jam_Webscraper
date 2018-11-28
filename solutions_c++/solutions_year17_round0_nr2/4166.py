#include <fstream>
#include <algorithm>
#include <vector>
#include <set>
#include <string>

using namespace std;

int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");

	int t;
	in >> t;
	
	for (auto tcase = 1; tcase <= t; tcase++)
	{
		string str;
		in >> str;

		auto untidyPoint = 0;
		for (auto i = 1; i < str.size(); i++)
		{
			if (str[i - 1] > str[i])
			{
				untidyPoint = i;
				break;
			}
		}

		out << "Case #" << tcase << ": ";

		if (untidyPoint == 0)
		{
			out << str << endl;
			continue;
		}
		
		for (auto i = untidyPoint; i < str.size(); i++)
			str[i] = '9';

		--str[untidyPoint - 1];

		for (auto i = untidyPoint - 1; i > 0; i--)
		{
			if (str[i - 1] > str[i])
			{
				str[i] = '9';
				--str[i - 1];
			}
			else break;
		}

		for (auto i = 0; i < str.size(); i++)
		{
			if (i == 0 && str[i] == '0')
				continue;;
			out << str[i];
		}

		out << endl;
	}
}