#include <iostream>
#include <string>
#include <iostream>
#include <sstream>

using namespace std;
int main()
{
	int numbers;
	
	cin >> numbers;
	

	
	for(int i = 1;i <= numbers;i++){
		
	
		int flipper = 0;

		char last = '.';
		char side;
		
		string pile;
		
		cin >> pile;
		cin >> flipper;
		bool pancakes[pile.size()];
		
		 stringstream stream(pile);

		int r = 0;
		
		while(stream >> side)
		{
	    	
	    	if(side == '+')pancakes[r] = 1;
	    	else pancakes[r] = 0;
	    	
	    	r++;
	    	
	   	}
   		
		int flips = 0;
		
		for(int j = 0;j <= pile.size() - flipper;j++){
			
			if(pancakes[j] == 0){
				
				flips++;
				
				for(int a = 0;a < flipper;a++){
					pancakes[j+a] = !pancakes[j+a];
				}
			}
		}
   		
   		for(int j = pile.size() - flipper;j < pile.size();j++){
   			if(pancakes[j] == 0){
   				
   				flips = -1;
				break;		
		   }
   		}
   		
   		if(flips == -1)
   		cout << "Case #" << i << ": IMPOSSIBLE" << endl;
   		else
		cout << "Case #" << i << ": " << flips << endl;
	
	}
	
	

		

}
