#include <stdio.h>
#include <iostream>

using namespace std;

int main(){
	int reps;
	
	long long int n;
	long long int n2;

	int cDigit;

	cin >> reps;

	for(int i = 0; i < reps; i++){
		cin >> n;	
		n2 = n;
		int c = 0;

		while(n2 >= 1){
			cDigit = n2 % 10;
			n2 = (n2 - cDigit)/10;
			c++;
		}

		int digits[c];
		n2 = n;

		for(int j = c; j >= 0; j--){
			digits[j - 1] = n2 % 10;
			n2 = (n2 - digits[j -1])/10;
		}

		for(int k = c - 2; k >= 0; k--){
			if(digits[k + 1] < digits[k]){
				digits[k] = digits[k] - 1;
				for(int m = c - 1; m > k; m--){
					digits[m] = 9;
				}
			}
		}

		cout << "Case #" << i+1 << ": ";
		for(int l = 0; l < c; l++){
            if(digits[l] == 0){
                continue;
            }
			cout << digits[l];
		}
		cout << "\n";
	}

	return 0;
}

