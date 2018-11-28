#include <iostream>
using namespace std;

bool isTidy(long long int);

int main(){

	long long int dataNum = 0;
	cin >> dataNum;
	for (int i = 1; i <= dataNum; i++){
		int tidyNum = 0;
		int maxNum = 0;
		cin >> maxNum;

		for (int n = maxNum; n > 0; n--){
			if (isTidy(n)){
				tidyNum = n;
				break;
			}
		}

		cout << "Case #" << i << ": " << tidyNum << endl;
	}

	return 0;
}

bool isTidy(long long int number){

	while(number > 9){
		long long int preNumber = number / 10;
		if (number % 10 < preNumber % 10)
			return false;
		number = preNumber;
	}

	return true;
};