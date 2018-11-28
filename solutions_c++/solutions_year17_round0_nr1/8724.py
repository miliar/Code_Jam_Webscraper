#include <iostream>
#include <string>
using namespace std;

int main()
{
	freopen("A-large.in.txt", "r", stdin);
	freopen ("myfile.txt","w",stdout);
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		string pancakes;
		int pan;
		cin >> pancakes >> pan;
		int tot = pancakes.length();
		int limit = tot - pan + 1;
		int count = 0;
		bool IMPOSSIBLE = false;
		for (int j = 0; j < limit; j++)
		{
			if(pancakes[j] == '-')
			{
				count ++;
				for(int k = 0; k < pan; k++)
				{
					if(pancakes[j+k] == '-')
					{
						pancakes[j+k] = '+';
					}
					else
					{
						pancakes[j+k] = '-';
					}
				}
			}		
		}
		for(int l = 0; l < pan; l++)
		{
			if(pancakes[limit+l] == '-')
			{
				IMPOSSIBLE = true;
			}
		}
		
		if(IMPOSSIBLE)
		{
			cout << "Case #" << i+1 << ": "<< "IMPOSSIBLE" << endl;
		}
		else
		{
			cout << "Case #" << i+1 << ": "<< count << endl;
		}
	}
	return 0;
}
