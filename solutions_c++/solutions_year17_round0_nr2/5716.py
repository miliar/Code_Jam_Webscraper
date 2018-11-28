#include <iostream>
#include <string>
#include <sstream>

using namespace std;

bool checkTidy(string s){
	bool tidy;
	int previous = -1;
	for (int i = 0; i < s.length(); i++){
		ostringstream os;
		os << s[i];
		string a = os.str();
		istringstream ss{a};
		int ab;
		ss >> ab;
		if (ab < previous){
			return false;
		}
		previous = ab;
	}
	return true;
}

int getTidy(string s){
	bool tidy;
	int previous = -1;
	for (int i = 0; i < s.length(); i++){
		ostringstream os;
		os << s[i];
		string a = os.str();
		istringstream ss{a};
		int ab;
		ss >> ab;
		if (ab < previous){
			return i;
		}
		previous = ab;
	}
	return -1;
}

string returnTidy(string s){
	string a = s;
	while(!checkTidy(a)){
		istringstream ss{a};
		long long ab;
		ss >> ab;
		ab--;
		ostringstream os{};
		os << ab;
		a = os.str();
		// cout << ab << endl;
	}
	return a;
}

string returnTidy2(string s){
	int a = getTidy(s);
	while(a != -1){
		ostringstream os;
		for (int i = a; i < s.length(); i++){
			os << s[i];
		}
		string st = os.str();
		istringstream ss {st};
		long long int val;
		ss >> val;
		val++;
		istringstream sa {s};
		long long int value;
		sa >> value;
		value -= val;
		ostringstream ot;
		ot << value;
		s = ot.str();
		a = getTidy(s);
	}
	return s;	
}

int main(){
	int num;
	cin >> num;
	for (int i = 1; i <= num; i++){
		string s;
		cin >> s;
		cout << "Case #" << i << ": " << returnTidy2(s) << endl;
	}
}
