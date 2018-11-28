#include <iostream>
#include <fstream>
using namespace std;

bool turned[1010];

int main () {
  ofstream myfile;
  ifstream input;
  input.open("input.txt");
  myfile.open ("output.txt");
  int t;
  input>>t;
  for(int i=1; i<=t; i++){
		int k;
		string s;
		input>>s>>k;
		bool valid = true;
		int count = 0;

		for(int j=0; j<s.length(); j++) {
			turned[j] = false;
		}

		for(int j=0; j<s.length(); j++) {
			if((s[j]=='+' && turned[j]) || (s[j]=='-' && !turned[j])) {
				if(j + k > s.length()) {
					valid = false;
				} else {
					for(int t=0; t<k; t++) {
						turned[j+t] = !turned[j+t];
					}
					count ++;
				}
			}
		}

		if(valid){
			myfile<<"Case #"<<i<<": "<<count<<endl;
		}else {
			myfile<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
		}

  }
  myfile.close();
  input.close();
  return 0;
}
