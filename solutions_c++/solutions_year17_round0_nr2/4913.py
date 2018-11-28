#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

int minBefore[20];

int main () {
  ofstream myfile;
  ifstream input;
  input.open("input.txt");
  myfile.open ("output.txt");
  int t;
  input>>t;
  for(int i=1; i<=t; i++){
    string s;
		input>>s;

    bool valid = false;
    bool redo = false;

		for(int j=0; j<s.length(); j++) {
			if (j == 0) {
        minBefore[1] = (int)(s[j]-'0');
      } else {
        int val = (int)(s[j]-'0');
        if (val < minBefore[j]) {
          s[j] = '9';
          s[j-1]--;
          for(int x=j; x<s.length(); x++) {
            s[x] = '9';
          }
          redo = true;
        }
        minBefore[j+1] = max((int)(s[j]-'0'), minBefore[j]);
      }
      if (redo) {
        redo = false;
        j = 0;
      }
		}

    myfile<<"Case #"<<i<<": ";
    for(int j=0; j<s.length(); j++) {
		  if (valid || (s[j]!='0')){
			  myfile<<s[j];
        valid = true;
		  }
    }
    myfile<<endl;
  }
  myfile.close();
  input.close();
  return 0;
}
