/*
 * tidyNumbers.cpp
 *
 *  Created on: Apr 8, 2017
 *      Author: pnueli
 */


#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool is_increasing(string ss){
	for (unsigned long long i=0; i<ss.size()-1; i++){
		if( ss[i] > ss[i+1]){
			return false;
		}
	}
	return true;
}

int main(){
	int tries, count;
	string ss = string();
	vector<char> output;
	cin >> tries;
	count = 1;
	bool did_abort;
	while (count <= tries){
		did_abort = false;
		cin >> ss;
		output.clear();
		cout << "Case #" << count << ": ";
		count++;
		if (is_increasing(ss)){
			cout << ss << endl;
			continue;
		}
		for (unsigned long long i = ss.size()-1; i>0; i--){
			char right_c = ss[i];
			char left_c = ss[i-1];
			if (right_c >= left_c ){
				continue;
			}
			left_c--;
			ss[i-1] = left_c;
			if (left_c == '0' && i==1){
				for (unsigned long long k=ss.size()-1; k > i-1; k--){
					cout << '9';
				}
				cout << endl;
				did_abort = true;

			}
			for (unsigned long long j = i; j< ss.size(); j++){
				if (ss[j] == '9'){
					break;
				}
				ss[j] = '9';
			}
		}
		if(! did_abort){
			cout << ss << endl;
		}

	}
}




