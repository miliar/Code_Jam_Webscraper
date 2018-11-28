/*
 * pancakeflip.cc
 *
 *  Created on: Apr 8, 2017
 *      Author: maciek
 */
#include <iostream>
#include <string>

using namespace std;

string cutleading(string s){

	int i = 0;
	string newstr;
	while(i < s.length() && s.at(i) == '+') i++;
	if(i < s.length())
		newstr.append(s.substr(i, s.length()-i));
	return newstr;
}

bool validconfig(string s){
	for(char c : s)
		if(c == '-') return false;
	return true;
}

string flip(string s, int k){
	string newstr;
	for(int i = 0; i < k; i++)
		if(s.at(i) == '+')
			newstr.append("-");
		else
			newstr.append("+");
	newstr.append(s.substr(k,s.length()-k));
	return newstr;
}



int main(){
	int T;

	int k;
	string s;
	cin >> T;
	for(int i = 0; i < T; i++){
		cin >> s >> k;
		int counter = 0;
		bool found = false;

		while(s.length() >= k){
			s = cutleading(s);
			if(s.length() == 0){
				found = true;
				break;
			}else if(s.length() < k){
				break;
			}else{
				counter++;
				s = flip(s,k);
			}
		}

		cout << "Case #" << i+1 << ": ";
		if(found)
			cout << counter << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}

}



