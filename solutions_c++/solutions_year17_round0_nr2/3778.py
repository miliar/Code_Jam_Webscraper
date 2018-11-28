#include <iostream>
#include <cstdio>
#include <sstream>

using namespace std;

int main(int argc, char const *argv[])
{
	int T;
	string inp;
	getline(cin,inp);
	istringstream iss(inp);
	iss >> T;
	for(int a0=1; a0<=T; a0++){
		getline(cin,inp);
		int len = inp.size();
		int nine = len;
		int carry = 0;
		for(int a1=len-1; a1>0; a1--){
			// pre process
			if(carry){
				if(inp[a1]=='0'){
					nine = a1;
					continue;
				}else{
					inp[a1]--;
					carry = 0;
				}
			}
			// compare
			if(inp[a1]<inp[a1-1]){
				nine = a1;
				carry = 1;
			}
		}
		if(carry){
			inp[0]--;
		}
		printf("Case #%d: ",a0);
		int zero = 1;
		for(int a1=0; a1<nine; a1++){
			if(!zero||(inp[a1]!='0')){
				zero = 0;
				cout << inp[a1];
			}
		}
		for(int a1=nine; a1<len; a1++){
			cout << '9';
		}
		cout << endl;
	}
	return 0;
}