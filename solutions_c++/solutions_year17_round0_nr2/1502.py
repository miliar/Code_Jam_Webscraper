#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main(int argc, char** argv) {
	int t;
	cin >> t;
	for(int iter = 0; iter < t; iter++) {
		cout << "Case #" << iter + 1 << ": ";
        string number;
        cin >> number;


        int mid = 1;
        for(; mid < number.size(); mid++) {
            if (number[mid] < number[mid - 1]) {
                break;
            }
        }
        if (mid < number.size()) {
            for(int i = mid; i < number.size(); i++) {
                number[i] = '9';
            }
            for(int i = mid - 1; i >= 0; i--) {
                if (i == 0 || number[i] > number[i - 1]) {
                    number[i]--;
                    break;
                } 
                number[i] = '9';
            }
            if (number[0] == '0') {
                number = number.substr(1, number.size() - 1);
            }
        }
        cout << number << endl;
	}
	return 0;
}
