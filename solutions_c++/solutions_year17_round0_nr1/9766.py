#include <iostream>
#include <string>

bool allPos(std::string testCase){
	for(int i = 0; i <=  static_cast<int>(testCase.length()); i++){
		if(testCase[i] == '-'){
			return false;
		}
	} 
	return true;
}
void flipper(std::string &testCase, int start, int end){
	for(int i = start; i < end; i++){
		if(testCase[i] == '-'){
			testCase[i] = '+';
		}
		else{
			testCase[i] = '-';
		}
	}
}
int evaluatorFunc(std::string testCase, int start, int end){
	int amount_neg = 0;
	for(int i = start; i < end; i++){
		if(testCase[i] == '-'){
			amount_neg++;
		}
	} 
	return amount_neg;
}


int main(){
	
	int number;
	std::cin>>number;
	int caseNumb = 0;
	
	int flipSize;
	std::string testCase;
	int * cases;
	int * howManyFlips = new int[number];
	
	for(int i = 0; i < number; i++){
		howManyFlips[i] = 0;
	}
	
	while(caseNumb < number){
		std::cin>>testCase;
		std::cin>>flipSize;
		cases = new int[testCase.length() - flipSize + 1];
		bool all_happy = false;
		
		
		
		while(!all_happy){
			all_happy = allPos(testCase);
			if(all_happy){
				continue;
			}
			//gives a gradient
			for(int i = 0; i <  static_cast<int>(testCase.length()) - flipSize + 1; i++){
				
				cases[i] = evaluatorFunc(testCase, i, i + flipSize);
				if(testCase[i] == '-'){
					cases[i]++;
				}
				
			}
			
			//finds the largest gradient (if it is equal to flipSize it is all negative)
			int max = 0;
			int pos_max = 0;
			for(int i = 0 ; i <  static_cast<int>(testCase.length()) - flipSize + 1; i++){
				if(cases[i] > max){
					max = cases[i];
					pos_max = i;
				}
			}
			
			//flips that position
			flipper(testCase, pos_max, pos_max + flipSize);
			
			//checks if they are all positive
			all_happy = allPos(testCase);
			howManyFlips[caseNumb]++;
			
			//if it is impossible
			if(howManyFlips[caseNumb] == static_cast<int>(testCase.length()) + 1){
				
				all_happy = true;
				howManyFlips[caseNumb] = -1;
			}
		}
		caseNumb++;
	}
	
	int count = 0;
	while(count < number){
		std::cout<<"CASE #"<<count + 1<<": ";
		if(howManyFlips[count] == -1){
			std::cout<<"IMPOSSIBLE"<<std::endl;
		}
		else{
			std::cout<<howManyFlips[count]<<std::endl;
		}
		count++;
	}
}

