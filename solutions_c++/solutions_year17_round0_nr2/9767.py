#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <cstring>
#include <sstream>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
int main() {
  int t;
  long n, m;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> n;
	if (n > 0){
	    stringstream ss;
        ss.str("");
	    ss << n;
	    string s = ss.str();
    	for(int j = s.length()-1; j > 0; j--){
	        string a = s.substr(j-1,1);
		    string c = s.substr(j, 1);
		    int ai = stoi(a);
		    int ci = stoi(c); 
		    if ( ai > ci) {
		        ai--;
		        ci = 9;
		        ss.str("");
		        ss << s.substr(0,j-1) << ai << ci ;
		        for (int l = j+1; l < s.length(); l++)
		         {ss << ci; }
		         //s.substr(j+1, s.length()-j);
		        s = ss.str();
		    }
	    }
	    //remove zeroes from start
	    ss.str("");
	    for(int l = 0; l < s.length(); l++){
	        int ai = stoi(s.substr(l,1));
	        if (ai != 0){ ss << s.substr(l,s.length()-l);  break;}
	    }
	    s = ss.str();
	    cout << "Case #" << i << ": " << s << endl;
    }else {
        // int ans = stoi(s);
        cout << "Case #" << i << ": " << n << endl;
        // cout knows that n + m and n * m are ints, and prints them accordingly.
        // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
    }
  }
  return 0;
}
