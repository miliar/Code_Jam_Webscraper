#include <bits/stdc++.h>
using namespace std;

int t, k, b, flips, poss = 1;
char c;
int p[1000], store[100];

int main()
{
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		for (int j = 0; j < 1000; j++) p[j] = -1;
		k = 0;
		b = 0;
		flips = 0;
		poss = 1;
		while (k == 0)
		{
			cin >> c;		
			if (c == '+')
			{
				p[b] = 1;
				//cout << "p[" << b << "] = " << p[b] << endl;
			}
			else if (c == '-')
			{
				p[b] = 0;
			}
			else
			{
				k = c-48;
			}
			b++;
		}
		for (int j = 0; j < b-k+1; j++)
		{
			if (p[j] == 0)
			{
				flips++;
				for (int g = j; g < j+k; g++)
				{
					if (p[g] == 0)
					{
						p[g] = 1;
					}
					else p[g] = 0;
				}
			}
		}
		for (int j = b-k+1; j < b+1; j++)
		{
			if (p[j] == 0)
			{
				poss = 0;
				break;
			}
		}
		if (poss == 1)
		{
			store[i] = flips;
		}
		else
		{
			store[i] = -1;
		}
	}
	for (int i = 0; i < t; i++)
	if (store[i] == -1)
		{
			cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
		}
		else
		{
			cout << "Case #" << i+1 << ": " << store[i] << endl;
		}
}