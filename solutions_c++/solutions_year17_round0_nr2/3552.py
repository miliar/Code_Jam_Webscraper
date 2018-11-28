#include <iostream>

using namespace std;
int main(){
	int numOfCases;
	cin >> numOfCases;
	for (int cases = 1; cases <= numOfCases; cases++){
		string n;
		cin >> n;
		string output(1, n[n.length() - 1]);
		int set_all_to_nine = n.length();
		for (int i = n.length() - 2; i >= 0; i--) {
			if (n[i]<= n[i + 1]){
				output = n[i] + output;
			} else {
				output = char(n[i] - 1) + output;
				n[i] = char(n[i] - 1);
				set_all_to_nine = i + 1;
			}
		}
		cout << "Case #" << cases << ": ";
		bool leading_zero = true;
		for (int i = 0; i < set_all_to_nine; i++){
			if (leading_zero && output[i] - '0' == 0){
				continue;
			}
			leading_zero = false;
			cout << output[i];
		}
		for (int i = set_all_to_nine; i < output.length(); i++) {
			cout << '9';
		}
		cout << endl;
	}
	return 0;
}