#include <iostream>
using namespace std;

int fun (string s, int size){
	int result = 0;
	for(int i=0;i<=s.length()-size;i++){
		if(s[i]=='+')
			continue;
		for(int j=0;j<size;j++){
			s[i+j]=='-'?s[i+j]='+':s[i+j]='-';
		}
		result++;
	}
	
	return s.find("-")!=string::npos?-1:result;
}

int main() {
	int amount = 0;
	string s;
	int pan = 0;
	
	cin >> amount;
	
	for(int i=0;i<amount;++i){
		cin >> s >> pan;
		int result = fun (s, pan);
		cout << "Case #" << i+1<<": ";
		result==-1?cout<< "IMPOSSIBLE" << endl:cout<<result<<endl;
	}
	
	return 0;
}