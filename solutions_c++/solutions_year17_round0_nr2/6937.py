#include <iostream>
#include <fstream>
using namespace std;

bool checkTidy(double num){
	string S = to_string(num);
	string::iterator it = S.begin();
	while(*(it+1) != '.'){
		if(*it > *(it+1))
			return false;
		it++;
	}
	return true;
}

int main(){
	int T;
	double num, lastTidy;
	ifstream testcase("testcase.in");
	ofstream output("output");
	//cin >> T;
	testcase >> T;
	for(int i = 1; i <= T; i++){
		//cin >> num;
		testcase >> num;
		//cout << "Case #" << i << ": ";
		output << "Case #" << i << ": ";
		for(double j = num; j >= 1; j--){
			if(checkTidy(j)){
				lastTidy = j;
				break;
			}
		}
		//cout << (int) lastTidy << endl;
		output << (int) lastTidy << endl;
	}
}
