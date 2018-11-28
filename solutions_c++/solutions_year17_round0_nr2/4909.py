#include <iostream>
using namespace std;

bool sorted(string& N){
	for(int i = N.length()-1; i>0; i--){
		if(N[i-1]>N[i]) {
			N[i-1]--;
			for(;i<N.length();i++)
				N[i]='9';
			return false;
		}
	}
	return true;
}

string solve(string N){
	while(!sorted(N)){}
	return N;
}

int main(){
	int T;
	string N;
	cin >> T;
	for (int i = 1; i <= T; i++){
		cin >> N;
		string s = solve(N);
		if(s[0]=='0')
			cout << "Case #" << i << ": " << s.substr(1,s.length()-1) << endl;
		else 
			cout << "Case #" << i << ": " << s << endl;
	}
	return 0;
}