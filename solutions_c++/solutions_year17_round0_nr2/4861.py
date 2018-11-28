#include <iostream>
#include <vector>

using namespace std;

long long int digit[20];
long long int result[20];

int main() {
	long long int z;
	cin >> z;
	
	for(long long int zz = 1; zz <= z; zz++) {
		long long int number;
		cin >> number;
		
		long long int pos = 0;
		while(number > 0) {
			pos++;
			digit[pos] = number % 10;
			number /= 10;
		}
		
		for(long long int i = 1; i <= pos / 2; i++) {
			swap(digit[i], digit[pos - i + 1]);
		}
		
		result[1] = digit[1];
		
		for(long long int i = 2; i <= pos; i++) {
			if(digit[i] >= result[i - 1]) {
				result[i] = digit[i];
			} else {
				result[i - 1]--;
				
				int errorL = i - 2;
				int errorP = i - 1;
				
				while(errorL != 0  && result[errorL] > result[errorP]) {
					result[errorP] = 9;
					result[errorL]--;
					errorL--;
					errorP--;
				}
				
				
				for(int j = i; j <= pos; j++) {
					result[j] = 9;
				}
				break;
			}
		}
		bool pr = false;
		
		cout << "Case #" << zz << ": ";
		
		for(long long int i = 1; i <= pos; i++) {
			if(pr == true) {
				cout << result[i];
			} else {
				if(result[i] != 0) {
					pr = true;
					cout << result[i];
				}
			}
		}
		
		cout << endl;
	}
	
	return 0;
}
