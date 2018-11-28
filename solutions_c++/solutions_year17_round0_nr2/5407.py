#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <map>
#include <set>
#include <cmath>
#include <string>
#include <sstream>
using namespace std;


string solve(long long N) {
	stringstream ss;
	ss << N;
	string strn = ss.str();
	
	bool fin = false;
	
	string result = "NULL";
	while(!fin) {
		bool sorted = true;
		for(int i=1; i<strn.length(); ++i) {
			sorted &= (strn[i] >= strn[i-1]);
		}
		if(sorted) {
			result = strn;
			break;
		}
		
		//Get index of first unsorted pair
		int id = 0;
		for(int i=1; i<strn.length(); ++i) {
			if(strn[i] < strn[i-1]) {
				id = i-1;
				break;
			}
		}
		//cout << id << " ";
		//Decrease number with id and convert subsequent numbers to 0
		strn[id] = strn[id]-1;
		for(int i=id+1; i<strn.length(); ++i) {
			strn[i] = '9';
		}
		
		//cout << strn << endl;
	}
	//Removing leading 0s
	int id=-1;
	for(int i=0; i<result.length(); ++i) {
		if(result[i] != '0') {
			id = i;
			break;
		}
	}
	if(id!=0) {
		result = result.substr(id);
	}
	
	return result;
}


int main() {
	int T;
	cin >> T;
	
	long long N;
	for(int t=1; t<=T; ++t) {
		cin >> N;
		cout << "Case #" << t << ": " << solve(N) << endl;
	}
	return 0;
}