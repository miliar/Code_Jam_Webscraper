#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <assert.h>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <tuple>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <unordered_map>
#include <unordered_set>

using namespace std;







int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int qqq;
	cin >> qqq;
	for (int qq = 1; qq <= qqq; qq++)
	{
		cout << "Case #" << qq << ": ";
		string s;
		cin >> s;
		std::string::size_type sz = 0;
		long long x = stoll(s,&sz,0);
		
		if (x < 10)
		{
			cout << x << endl;
		}
		else
		{
			pls_dont_kill_me :
			int i = 1;
			while (i<s.length() && s[i] >= s[i - 1])
			{
				i++;
			}
			if (i != s.length())
			{
				if (i == 1 && s[i - 1] == '1')
				{
					for (int j = 1; j < s.length(); j++)
					{
						cout << 9;
					}
					cout << endl;
				}
				else
				{
					s[i-1]--;
					for (int j = i; j < s.length(); j++)
					{
						s[j] = '9';
					}
					goto pls_dont_kill_me;

				}
			}
			else
			{
				cout << s << endl;
			}

		}
		

	}
	return 0;
}