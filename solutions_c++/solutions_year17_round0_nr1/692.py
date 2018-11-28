#include <iostream>
#include <cstring>

using namespace std;

void flip(string &s, int i, int k){
	for(int j = i; j < i+k; j++){
		s[j] = s[j] == '-' ? '+' : '-';
	}
}


int main(){
	int nt;

	cin>>nt;

	for(int test = 0 ; test < nt; test++){

		bool solved = true;
		int res = 0;

		int k;
		string s;

		cin>>s>>k;
		int ls = s.length();
		
		for(int j = 0; j < ls - k + 1; j++){

			if (s[j] == '-'){
				res++;
				flip(s, j, k);
			}
		}

		for(int i = 0; i < ls && solved; i++){
			solved = s[i] == '+';
		}

		cout<<"Case #"<<test+1<<": ";
		if (!solved)
			cout<<"IMPOSSIBLE";
		else
			cout<<res;
		cout<<endl;
	}

	return 0;
}