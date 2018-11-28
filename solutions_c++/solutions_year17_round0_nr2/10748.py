#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cmath>

using namespace std;

int main(){
	
	ifstream input;
	input.open("input.in");
	int t;
	input >> t;
	
	ofstream file;
	file.open("result.txt");

	for (int i = 0; i< t; i++){
		
		string number;
	
		input >> number;
		int numberInt = atoi(number.c_str());
		int orjNumber = numberInt;
		
		bool isChanged = false;
		
		int req = 0;
		for(int j = 0; j < number.length()-1; j++){
						
			if(number[j] <= number[j+1]){
				if(number[j] == number[j+1])
					req++;
				else
					req = 0;
					
 				continue;
			}
			
			isChanged = true;
			
			int multipler = (int) pow(10,number.length()-j-1+req);
			numberInt = numberInt / multipler;
			numberInt = numberInt * multipler;
			
			break;
		}
		file << "Case #" << i+1 << ": " << numberInt - (isChanged ? 1 : 0) << endl;
	}
	
	input.close();
	file.close();
}
