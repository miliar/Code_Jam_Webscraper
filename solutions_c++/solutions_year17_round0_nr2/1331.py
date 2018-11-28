#include <cstdlib>
#include <iostream>
#include <cmath>
#include <vector>
//#include <boost/multiprecision/cpp_int.hpp>

using namespace std;
//using namespace boost::multiprecision;
string processNaive(string N);
string processOpti(string N);

int main() {
	/*
	for(int i = 0 ; i < 1000 ; ++i){
		long l = rand()%9999999;
		string s = to_string(l);
		if(processNaive(s) != processOpti(s)){
			cout << "OULALALALAL" << endl;
			return -1;
		}
		else cout << "OUIIIIIIIIII " << i << endl;
	}*/
	int T;
	cin >> T;
	for(int l = 0 ; l < T ; l++) {
		string s;
		cin >> s;
		//TRAITEMENT
		cout << "Case #" << l + 1 << ": " << processOpti(s) << endl;
		///////////
	}
	return 0;
}

bool ordered(string s){
	for(unsigned i = 1 ; i < s.size() ; ++i)
		if(s[i] < s[i - 1]) return false;
	return true;
}

string processNaive(string s){
	while(!ordered(s)){
		long a = stol(s);
		s = to_string(--a);
	}
	return s;
}

string processOpti(string s){
	cerr << "Bonjour" << endl;
	while(!ordered(s)) {
		bool fill = false;
		for(unsigned i = 0 ; i < s.size() ; ++i){
			if(fill)
				s[i] = '9';
			else if(i > 0 and s[i] < s[i-1]){
				fill = true;
				s[i-- - 1]--;
			}
		}
	}
	int i = 0;
	for(; i < s.size() && s[i] == '0'; ++i);
	return s.substr(i);
}
