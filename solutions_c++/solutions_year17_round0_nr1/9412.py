#include <string>
#include <iostream>
#include <ctime>

using namespace std;

void trans(string& s, int k, int index){
	for(int i = 0; i < k; ++i){
		s[index + i] = (s[index + i] == '+') ? '-' : '+';
	}
}

string genCase(int n, int k){
	string caseS(n, '+');
	for(int i = 0; i < n - k; ++i)
		if (rand() % 2)		
			trans(caseS, k, i);
	return caseS;
}

string process(string s, int n, int k){
	int steps = 0;
	for(int i = 0 ; i < n - k + 1 ; ++i)
		if(s[i] == '-') {trans(s, k, i); steps++;}
	if(s != string(n, '+')) return string("IMPOSSIBLE");
	return to_string(steps);
}

int main(){
	/*
	srand(time(NULL));
	const int T = 100;
	for(int i = 0 ; i < T ; ++i){
		int n = rand() % 1000 + 1;
		int k = rand() % n + 1;
		string test = genCase(n, k);
		string res = process(test, n, k);
		cout << "TEST " << test << endl << "REST " << res << endl << endl;
		if(res != string(n, '+')){
			cout << "OULALALALAAL"; return -1;
		}
	}
	*/
	int T;
	cin >> T;
	for(int i = 0 ; i < T ; ++i){
		string s; int k;
		cin >> s >> k;
		cout << "Case #" << i + 1 << ": " << process(s, s.size(), k) << endl;
	}
	return 0;
}

