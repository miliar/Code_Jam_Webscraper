#include "pancakes.hpp"

int flipper (std::string &pancakes, int k){
	bool traite = false;
	for (int i = 0; i < pancakes.size(); i++)
	{

		if (!traite && pancakes[i]=='-')
		{
			if (i+k > pancakes.size())
			{
				return 2;
			}else{
				for (int j = i; j < i+k; j++)
				{
					invert(pancakes[j]);
				}
			}
			return 1;
		}
	}

	return 0;
}

void invert (char &pancake){
	if (pancake=='+')
		pancake='-';
	else
		pancake='+';
}