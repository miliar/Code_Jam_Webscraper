#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;

FILE* pF;

FILE* pAnsF;

int main()
{
	freopen_s(&pF, "Text2.txt", "r", stdin);

	freopen_s(&pAnsF, "will2.txt", "w", stdout);
	int C;
	cin >> C;

	for (int c = 1; c <= C; c++)
	{
		string num;	
		string ans;
		cin >> num;
		vector<int>v;
		for (int i = 0; i < num.size(); i++)
		{
			v.push_back(num[i] - 48);
		}
		while (1)
		{
			bool modified = false;
		
			for (int i = 0; i < v.size() - 1; i++)
			{
				if (v[i] > v[i + 1])
				{
					modified = true;
					if (v[i] == 0)
					{
						v[i] = 9;
					}
					else
					{
						v[i] = v[i] - 1;
					}
					for (int j = i + 1; j < v.size(); j++)
					{
						v[j] = 9;
					}
					break;
				}				
			}
			if (modified == false)
				break;
		}
		int start = 0;
		for (int i = 0; i < v.size(); i++)
		{
			if (v[i] == 0)
				start = i + 1;
			else
				break;
		}
		for (int i = start; i < v.size(); i++)
		{
			ans.push_back(v[i] + 48);
		}
		cout << "Case #" << c << ": " << ans << endl;
		
	}

	return 0;
}