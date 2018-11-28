#include <iostream>
using namespace std;

string fun (string s){
	
	if(s.length()<=1)
		return s;
		
	string result = fun (s.substr(1));
	
	if(result[0]<s[0]){
		--s[0];
		for(int i=1;i<s.length();++i)
			s[i]='9';
	}
	else{
		s=s[0];
		s+=result;
	}
	
	return s;
}

int main() {
	int amount = 0;
	string s;
	
	cin >> amount;
	
	for(int i=0;i<amount;++i){
		cin >> s;
		string result = fun(s);
		result.erase(0, result.find_first_not_of('0'));
		cout << "Case #" << i+1<<": "<< result <<endl;
	}
	
	return 0;
}