#include <iostream>
#include <string>

using namespace std;

void allnones(string &n, int i){
	for(; i < n.size(); ++i){
		n[i] = '9';
	}
}

void continueTidy(string &n, int i){
	for(; i > 0; --i){
		if(n[i] < n[i - 1]){
			n[i] = '9';
			n[i - 1] = ((9 + (n[i - 1] - '0')) % 10) + '0';
		}
	}
}

string lastTidy(string n){
	for(int i = 1; i < n.size(); ++i){
		if(n[i] < n[i - 1]){
			n[i - 1] = ((9 + (n[i - 1] - '0')) % 10) + '0';
			allnones(n, i);
			continueTidy(n, i - 1);
		}
	}
	return (n[0] == '0') ? n.substr(1) : n;
}

int main(){
	int t;
	string num;
	cin >> t;
	for(int i = 1; i <= t; i++){
		cin >> num;
		cout << "Case #" << i << ": " << lastTidy(num) << endl;
	}
	return 0;
}