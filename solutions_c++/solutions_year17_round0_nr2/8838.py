// Example program
#include <string>
#include <sstream>
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text

void resetArray(int arr[], int length){
	for(int i =0; i < length; i++){
		arr[i] = -1;
	}
}
void maskWithNines(int arr[],int length){
	for(int i = 0; i <= length; i++){
		arr[i] = 9;
	}
}
string arrtoString(int arr[], int digits){
	stringstream output;
	bool started = false;
	for(int i = digits-1; i >= 0; i--){
	    if (arr[i] != 0){
	         started = true;
	    }
	    if(started == true){
	        output << arr[i];    
	    }
	}
	return output.str();
}
int* returnNumber(int arr[], int digits){
	int current = arr[digits-1];
	int temp;
	for(int i = digits-1; i >= 0; i--){
		temp = arr[i];
		if(temp < current){
			arr[i+1] = arr[i+1]-1;
			maskWithNines(arr,i);
			arr = returnNumber(arr,digits);
		}
		current = arr[i];		
	}
	return arr;
}

int main() {
	int t;
	long long input;
	string output;
	int arr[18];
	resetArray(arr,18);
	int digits = 0;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		cin >> input;  // read n and then m.
		while(input > 0){
			arr[digits] = input%10;
			input = input/10;
			digits++;
		}
		cout << "Case #" << i << ": " << arrtoString(returnNumber(arr,digits),digits) << endl;
		resetArray(arr,18);
		digits = 0;
	}
}
