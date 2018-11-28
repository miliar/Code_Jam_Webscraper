#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <sstream>

using namespace std;

char flipPan (char side){
	if(side == '-'){
		return '+';
	}else{
		return '-';
	}
}

bool pancakeCheck (string const& pancakes, int noPans){
	for(int i = 0; i < noPans; ++i){
		if(pancakes[i] == '-'){
			return 0;
		}
	}
	return 1;
}

string convertInt2Str(int number)
{
   stringstream ss;
   ss << number;
   return ss.str();
}


int main() {
  cin >> noskipws; 
  int t, n, noPans, noFlips;
  int left, right;
  string pancakes, ans;
  char c;
  char dummy; //for new line read in
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  cin >> dummy;
  for (int caseNo = 1; caseNo <= t; ++caseNo) {
  	pancakes.clear();
  	noPans = 0;
    while(cin >> c){
    	if(c == ' '){
    		cin >> n;
    		cin >> dummy;
    		break;
    	}
    	pancakes.push_back(c);
    	++ noPans;	
    }  // read n and then m.
  /*  cout << pancakes[0] << endl;
    cout << noPans << " " << n << endl;
    cout << pancakes[noPans-1] << endl;
	*/
    left =0;
    right = noPans-1;
    noFlips = 0;
	for(int i = 0; i < (noPans/2 + 1);++i){
		left = i;
		right = noPans - 1 - i;
		if(right <= left ){
			if(pancakeCheck(pancakes, noPans)){
				ans = convertInt2Str(noFlips);
				break;
			}else{
				ans = "IMPOSSIBLE";
				break;				
			}
		}else{
			if(pancakes[left] == '-'){
				++noFlips;
				for(int j = 0; j < n; ++j){
				if(left+j < noPans)
				pancakes[left+j] = flipPan(pancakes[left+j]);
				}
			}

			if(pancakes[right] == '-'){
				++noFlips;
				for(int j = 0; j < n; ++j){
				if(right-j >=0){
				pancakes[right -j] = flipPan(pancakes[right-j]);
			}
				}
			}
		}
	}

   cout << "Case #" << caseNo << ": " << ans << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
}