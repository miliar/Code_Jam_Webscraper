//
// Created by Leonardo de Oliveira Ramos on 4/7/17.
//
#include <iostream>
#include <string>


using namespace std;

int main()
{
	int num_cases;
    cin >> num_cases;

    // cout << num_cases << endl;


    for (int i = 0;i < num_cases; i++)
    {
    	int flipper_size;
    	int num_flips;
    	int num_pancakes;
    	string pancakes;

    	cin >> pancakes >> flipper_size;
    	num_pancakes = pancakes.size();
		num_flips = 0;

    	for (int j = 0;j < num_pancakes - flipper_size + 1; j++)
    	{
    		// Choosing most left - to flip
    		if(pancakes[j] == '-')
    		{
    			num_flips++;

    			// Flip pancakes
    			for(int k=0; k<flipper_size; k++)
    			{
    				if (pancakes[j+k] == '+')
    					pancakes[j+k] = '-';
    				else
    					pancakes[j+k] = '+';
    			}
    		}
    	}

    	int imp = 0;
    	for (int i = num_pancakes - flipper_size; i < num_pancakes; i++)
    	{
    		if (pancakes[i] == '-')
    		{
    			imp = 1;
    		}

    	}

    	if (imp)
    		cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
    	else
			cout << "Case #" << i+1 << ": " << num_flips << endl;
    }
    return 0;
}