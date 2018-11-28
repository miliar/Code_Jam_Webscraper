#include <bits/stdc++.h>

using namespace std;

bool isTidy(const string& in){
	for(int i=0; i<(int)in.size()-1; i++)
		if(in[i]>in[i+1]) return false;
	return true;
}

int main(){

	ios::sync_with_stdio(false);
	string input;
	
	getline(cin,input);
	int n = stoi(input);
	for(int i=0; i<n; ++i){
		getline(cin, input);
		while(1){
		if(isTidy(input)){
			 cout << "Case #"<< i+1 << ": "<< input << endl;
				break;
		}
		else input=to_string(stoi(input)-1);
		}
	}


 return 0;
}
