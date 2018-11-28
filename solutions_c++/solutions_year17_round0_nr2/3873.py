#include <iostream>
#include<string>
#include<vector>

/*
Tidy numbers
*/

using namespace std;

void backtrack(string& s, int k){
	//backtrack string s from integer k
	//after k it's ok
	//s[k] cannot be 0	
	int n = s.size();
	if (k<0 || k>=n) return;

	// 2 cases :
	// s[i] = 1 : need to backtrack until the beginning
	s[k]-=1;
	int i = k-1;
	while(i>=0 && s[i]>s[i+1]){
		s[i+1]='9';
		if (s[i]>'0' && s[i] <='9'){ 
			s[i]-=1;
		}else{
			cerr << "FATAL ERROR" << endl;
			break;
		}
		i--;
	}	
}
void tidy(string& s){
	//transform s into the closest smaller tidy number
	int n = s.size();
	for (int i = 0; i<n-1; ++i){
		//check s is tidy from left to right
		if (s[i+1]<s[i]){
			//detected what breaks tidy property
			//correction : 
			//1. fill the rest with 9
			//2. backtrack
			for (int j = i+1; j<n; ++j){
				s[j] = '9';
			}
			backtrack(s, i);
			//cout << "backtrack at index " << i << endl; 
		}
	}
}


int main(){
	int n; //number of test cases
	cin >> n; cin.ignore();
	vector<string> tests =  vector<string>(n);
	for (int i = 0; i<n ; ++i){
		cin >> tests[i]; cin.ignore();
	}

	for (int i = 0; i<n ; ++i){
		tidy(tests[i]);
		string& s = tests[i];
		int n = s.size();
		if (s[0]=='0') {
			//remove leading zeros
		        s.erase(0, s.find_first_not_of('0')); 
		}
		cout << "Case #"<<i+1<< ": " << s << endl;
	}
}
