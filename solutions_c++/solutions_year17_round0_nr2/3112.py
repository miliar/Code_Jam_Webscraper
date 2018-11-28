#include <iostream>
#include <string>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

int main()
{
	int numbers;
	
	cin >> numbers;
	

	
	for(int i = 1;i <= numbers;i++){
		
	
		char number;
		int lastNumber = -1;
		int size = 0;
		int seqSize = 0;
		vector<int>numberV;
		
		string pile,answer;
		
		cin >> pile;
		
		 stringstream stream(pile);

		while(stream >> number)
		{
			numberV.push_back(number - '0');
	   	}
	   	
	   	
	   	
   		for(int i = numberV.size() - 1; i >= 0;i--){
   			
   			if(lastNumber == -1)lastNumber = numberV[i];
   			else if(lastNumber < numberV[i]){

   				numberV[i]--;
   				
   				if((i == 0)&&(numberV[i] == 0)){
   					size = numberV.size() - 1;
				}
				else{
					
   					size = numberV.size() - i - 1;
				}

			}
			
			lastNumber = numberV[i];
   			

		}
   		
   		
   		
		cout << "Case #" << i << ": ";
		for(int i = 0;i < numberV.size() - size ;i++ ){
			
			if((i == 0)&&(numberV[i] == 0)){
				
			}else{
				cout << numberV[i];
			}
			
		}
		
		for(int i = 0;i < size ;i++ ){
			
			cout << "9";
			
		}
	
	
		cout << endl;
	}
			

}
