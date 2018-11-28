#include <iostream>
#include <string>
#include <vector>

using namespace std;
//bool tidy = true;

int main(){

	string tempForVector;
	int numberOfInput;
	cin >> numberOfInput;
	vector<string> inputVector(numberOfInput);
	// vector<int> answer;

	for (int i = 0; i < numberOfInput; ++i){

		// cout << numberOfInput << endl;
		cin >> tempForVector;
		inputVector[i] = tempForVector;
		// cout << i << endl;

	}

	// cout << inputVector[0] <<  " "  << inputVector.size() << endl;
	int index = 0;
	while(index != numberOfInput){

		bool flag = false;
		// index++;
		if (inputVector[index][0] == '1'){

			for (int i = 0; i < inputVector[index].size() - 1; ++i){

				if (inputVector[index][i] != '1'){
					break;
				}
				if (inputVector[index][i+1] == '0'){
					cout << "Case #" << index+1 << ": ";
					for (int i = 0; i < inputVector[index].size()-1; ++i){
						cout << 9;
					}
					cout << endl;
					// tidy = true;
				flag = true;
				break;
				}
			}
			if(flag){
				index++;
				continue;
			}
		}

// 2221   2219    2199   1999

		for(int i = 0; i < inputVector[index].size()-1; i++){

			if((inputVector[index][i]) - 48 > (inputVector[index][i+1]) - 48){

				int temp = inputVector[index][i] - 48;
				// cout << temp << endl;
				for(int j = i+1; j < inputVector[index].size(); j++)
					inputVector[index][j] = '9';
				for(int k = i; k > -1; k--){
					if((inputVector[index][k] == temp + '0' && inputVector[index][k-1] == temp + '0')/* || (inputVector[index][k] == temp + '0' && k == 0)*/){
						// inputVector[index][k] = (temp-1) + '0';
						inputVector[index][k] = '9';
					}
					else{
						inputVector[index][k] = (temp-1) + '0';
						break;
					}
				}
				// flag = true;
			}
			// if()
		}
			cout << "Case #" << index+1 << ": ";
			cout << inputVector[index] << endl;
		// cout << "EH" << endl;
		index++;
	}

	return 0;
}