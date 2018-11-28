#include <iostream>
#include <fstream>
#include <string>

using namespace std;

const string FN = "B-large.in";
// "B-small-attempt0.in";

string makeTidy (string& s) {
	int same_begin = int(s.length()) - 1;
	for (int i = s.length() -1 ; i > 0; --i) {
		if (s[i] < s[i - 1]) {
			//cout<<"Ind: " << i<<flush<<endl;
			
			s[i-1]--;
			for (int j = i; j <= same_begin; ++j) {
				//cout<<j<<" "<<same_begin<<"-"<<flush;
				s[j] = '9';
			}
			same_begin = i;
			//cout<<"N:"<<s[i-1]<<endl;
		} 
	}
	int begin = 0;
	while (begin < s.length() && s[begin]== '0') {
		begin++;
	}
	//cout << "B: "<<begin<<endl;
	if (begin == s.length()) {
		return "0";
	}
	//cout <<s.substr(begin)<<endl;
	return s.substr(begin);
}


int main() {
	ifstream input;
	input.open(FN.c_str());

	int T;
	string N;
	input >> T;

	for (int t = 1; t <=T ; ++t) {
		input>>N;
		cout<<"Case #" << t << ": " <<makeTidy(N) <<endl;
	}


	return 0;
}