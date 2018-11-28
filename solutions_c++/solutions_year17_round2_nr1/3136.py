#if 1
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

	freopen_s(&pAnsF, "output.txt", "w", stdout);
	
	int Cases;	

	cin >> Cases;
	int D, N;
	for (int c = 1; c <= Cases; c++)
	{
		cin >> D >> N;
		float  time = 0.0;
		int start, speed;
		float temp = 1.0;
		if (c == 19)
		{
			int a = 0;
		}
		for (int i = 1; i <= N; i++)
		{
			cin >> start >> speed;

			if (time < (D - start)*(temp) / speed)
			{
				time = (D - start)*(temp) / speed;
			}
		}
		
		cout << "Case #" << c << ": ";
		printf("%2.6f", (D*temp) / (temp*time));
		cout << endl;

	}

	return 0;
}
#endif