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
	freopen_s(&pF, "Text.txt", "r", stdin);

	freopen_s(&pAnsF, "will1.txt", "w", stdout);
	int C;
	cin >> C;

	for (int c = 1; c <= C; c++)
	{
		string pcake;
		int K;
		int ans = 0;
		cin >> pcake >> K;
		
		for (int i = 0; i <= pcake.size() - K; i++)
		{
			if (pcake[i] == '-')
			{
				ans++;
				for (int j = i; j < i + K; j++)
				{
					if (pcake[j] == '-')
						pcake[j] = '+';
					else
						pcake[j] = '-';
				}
			}
		}
		bool possible = true;
		for (int i = 0; i < pcake.size() ; i++)
		{
			if (pcake[i] == '-')
			{
				possible = false;
				break;
			}
		}
		if (possible)
		{
			cout << "Case #" << c << ": " << ans << endl;
		}
		else
		{
			cout << "Case #" << c << ": " << "IMPOSSIBLE" << endl;
		}	
		
	}

	return 0;
}