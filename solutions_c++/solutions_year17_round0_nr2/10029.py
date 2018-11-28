#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text
int main() {
  int t, n, m;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> n;  // read n and then m.
    bool flag = true;
    while(true){
    	flag = false;
    	string s = to_string(n);
    	for(int j = 0; j < s.length()-1; j++){
    		if(s.at(j) > s.at(j+1)){
    			flag = true;
    			break;
    		}
    	}	
    	if(!flag){
    		cout << "Case #" << i << ": " << n << endl;
    		break;
    	}
    	else
    		n--;
    }
  }
}