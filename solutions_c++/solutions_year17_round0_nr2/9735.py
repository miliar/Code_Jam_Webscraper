#include <stdio.h>
#include <iostream>
#include <math.h>  

using namespace std;

int GetLength(int number){
	int length = 1;

	while(number /= 10){
		length++;
	}
	return length;
}

bool IsTidy(int number){
	int temp = 0;
	for(int i = GetLength(number); i >= 0; i--){
		int y = pow(10, i);
    	int z = number/y;
    	int x2 = number / (y * 10);
    
    	if(z - x2 * 10 < temp){
    		return false;
    	}
    	temp = z - x2 * 10;
	}
	return true;
}

int FindLastTidy(int number){
	for(int i = number; i >= 0; i--){
		if(IsTidy(i)){
			return i;
		}
	}
	return 0;
}

int main() 
{
	int lineCount, num;
  	cin >> lineCount;
  	for (int i = 1; i <= lineCount; ++i) {
    	cin >> num;
    	cout << "Case #" << i << ": " << FindLastTidy(num) << endl;
  	}
}