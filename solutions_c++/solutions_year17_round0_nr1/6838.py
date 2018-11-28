#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <typeinfo>
#include <functional>
using namespace std;

int main()
{
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		string s;
		int k;
		int num = 0;
		cin >> s >> k;

		for (int j = 0; j < s.size() - k + 1; j++)
		{
			if (s.at(j) == '-')
			{
				for (int l = 0; l < k; l++)
				{
					if (s.at(j + l) == '-')
					{
						s.at(j + l) = '+';
					}
					else
					{
						s.at(j + l) = '-';
					}
					
				}
				num++;
			}
					
		}
		cout << "Case #" << i + 1 << ": ";
		//cout << s << endl;
		if (s.find("-") != string::npos)
		{
			cout << "IMPOSSIBLE" << endl;
		}
		else
		{
			cout << num << endl;
		}

	}
	return 0;
}