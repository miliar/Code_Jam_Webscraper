#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <sstream>

using namespace std;


string convertInt2Str(long long number)
{
   stringstream ss;
   ss << number;
   return ss.str();
}


int main() {
 // cin >> noskipws; 
  int t, no;
  int left, right;
  long long numberInt;
  string number, ans;
  char c;
  bool tidy;
  char dummy; //for new line read in
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
 
  for (int caseNo = 1; caseNo <= t; ++caseNo) {
  	cin >> numberInt;
  	ans.clear();
  	while(numberInt > 0){
  		number = convertInt2Str(numberInt);
  		no = number.length();
  		tidy = 1;
  		for(int i = 1; i<no; i++){
  			left = number[i-1] - '0';
  			right = number[i] - '0';
  			if(left > right){
  				//not tidy
  				tidy = 0;
  				break;
  			}
  		}
  		if(tidy == 1){
  			ans = number;
  			break;
  		}
  		--numberInt;
  		
  	}

   cout << "Case #" << caseNo << ": " << ans << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
}