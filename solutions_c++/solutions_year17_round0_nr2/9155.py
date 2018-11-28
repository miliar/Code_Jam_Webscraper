#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

int main() {
  int t, len;
  string n;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cin >> n;
    len = n.length();
    if(len > 1){
    	for(int j = 0; j < len - 1; j++){
    		if(n[j] > n[j+1]){
    			n[j]--;
    			for(int k = j + 1; k < len; k++){
    				n[k] = '9';
				}
				
				for(int k = j - 1; k >= 0; k--){
					if(n[k] > n[k+1]){
						n[k]--;
						n[k+1] = '9';
					}
				}
			}
		}
	}    
    
    cout << "Case #" << i << ": " << n.substr(n.find_first_not_of('0')) << endl;
  }
}
