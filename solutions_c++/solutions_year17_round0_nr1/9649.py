#include <iostream>
#include <string>

using namespace std;

string flipPancakes(string pancakes , int flipper) {
	if (pancakes.length() < flipper) {
		return "IMPOSSIBLE";
	}

	int flipCounts = 0;

	for (long i = 0; i < pancakes.length()-flipper+1; i++) {
		if (pancakes[i] == '-') {
			flipCounts++;
			for (auto j = i; j < i+flipper; j++) {
				pancakes[j] = pancakes[j] == '-' ? '+' : '-';
			}
		}
	}
	//cout << pancakes.substr(pancakes.length() - flipper, pancakes.length()) << endl;
	if ((pancakes.substr(pancakes.length() - flipper, pancakes.length())).find('-') != string::npos) {
		return "IMPOSSIBLE";
	}
	else {
		return to_string(flipCounts);
	}

	return pancakes;

}


int main() {

	long _totalTestCase = 0;
	//get number of test cases
	cin >> _totalTestCase ;
	cin.clear();
	for (long long i = 0; i <= _totalTestCase; i++) {

		string ds = "";
		string pancakes = "";
		int flipper = 0;
		//get test case input
		getline(cin, ds);
		if (i == 0)continue;
		//get pankakes
		pancakes =  ds.substr(0, ds.find(" "));
		//get flipper size
		flipper = atoi((ds.substr((ds.find(" ")+1) , ds.length()-1)).c_str());

		string res = flipPancakes(pancakes, flipper);
		cout << "Case #" << i << ": "  <<res<< endl;

	}

	return 0;
}