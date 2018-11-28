#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;


void flip(string &s, int index, int k){
	if (index + k > s.length()){
		return;
	}
	for (int i = index; i < index + k; i++){
		if(s[i] == '-'){
			s[i] = '+';
		}else{
			s[i] = '-';
		}
	}
}

bool isComplete(const string &s){
	for (int i = 0; i < s.length(); i++){
		if (s[i] == '-'){
			return false;
		}
	}
	return true;
}

int oversize(string s, int k){
	int counter = 0;
	for (int i = 0; i < s.length(); i++){
		if (s[i] == '-'){
			flip(s, i, k);
			counter++;
		}
	}
	if (isComplete(s)){
		return counter;
	}else{
		return -1;
	}
}

int main(){
	int numbCases;
	cin >> numbCases;
	for (int i = 1; i <= numbCases; i++){
		string s;
		int k;
		cin >> s;
		cin >> k;
		int h = oversize(s, k);
		if (h == -1){
			cout << "Case #" << i << ": IMPOSSIBLE" << endl;
		}else{
			cout << "Case #" << i << ": " << h << endl;
		}
	}

}
