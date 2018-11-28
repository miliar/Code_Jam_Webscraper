#include <iostream>
#include<string>

using namespace std;

int main()
{
	int t, pan, k=0, flips = 0, flag = 1;
	string pancakes;
	
	cin >> t;
	
	for(int i = 0; i < t; i++)
	{
		getline(cin, pancakes);	
		cin >> pancakes;
		cin >> pan;
			
		for(int j = 0; j < (pancakes.size() - (pan-1)) ; j++) 
		{
			if(pancakes[j] == '-')
			{
				flips ++;
				//cout << "flip here" << endl;
				while(k != pan)
				{
					if(pancakes[j+k]== '-')
						pancakes[j + k] = '+';
					else
						pancakes[j + k] = '-';
					k++;
					//cout << pancakes << " j=" << j << "flips=" << flips << endl;
				}
				k = 0;
			}
			//else cout << " j=" << j << "flips=" << flips << endl;
		}
		for(int j = 0; j < pancakes.size() ; j++)
		{
			if(pancakes[j] == '-') flag = 0;
		}
		if(flag) cout << "Case #" << i+1 << ": " << flips << endl;
		else cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
		flag = 1;
		flips = 0;
	}
}
