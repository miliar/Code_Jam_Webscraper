#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main()
{
	int t, k, limit, flip = 0;
	char cake[1001];
	bool isPos = true;
	cin >> t;
	for(int time = 1; time <= t; time++)
	{ 
		flip  = 0;
		isPos = true;
		cin >> cake >> k;
		if(k > strlen(cake))
		{
			for(int i = 0; i < strlen(cake); i++)
			{
				if(cake[i] == '-') 
				{
					isPos  = false;
					continue;
				}
			}
			if(isPos)
				cout << "Case #" << time << ": 0" << endl;
			else 
				cout << "Case #" << time << ": IMPOSSIBLE" << endl;
			continue;;
		}
		//cout << t << cake << k << strlen(cake);
		limit = strlen(cake) - k;
		for(int i = 0; i <= limit; i++)
		{
			if(cake[i] == '-')	
			{
				for(int j = i; j < i + k; j++)
				{
					if(cake[j] == '+')
						cake[j] = '-';
					else cake[j] = '+';			
				}
				flip++;
			}
		}
		for(int i = limit + 1; i < strlen(cake); i++)
		{
			if(cake[i] != cake[limit])
				isPos = false;
		}
		if(isPos)
		{
			//printf("Case #%d: %d\n", time, flip + 1);
			cout << "Case #" << time << ": " << flip << endl;
		}
		else //printf("Case #%d: IMPOSSIBLE\n", time);
		cout << "Case #" << time << ": IMPOSSIBLE" << endl;
	}
}
