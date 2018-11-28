#include <iostream>
using namespace std;

bool issorted(long long int n) {
    
    if(n%10 == 0) return false;
    
    int last = n%10;
    while(n) {
        if(n%10 <= last) {
            last = n%10;
        }
        else {
            return false;
        }
        n = n/10;
    }
    return true;
}

int main() {
	
	int t; cin >> t;
	for(int i=1;i<=t;i++) {
	    
	    long long int n; cin >> n;
	    
	    while(n) {
	        if(issorted(n)) {
	            cout << "Case #" << i << ": " << n << "\n";
	            break;
	        }
	        n--;
	    }
	    
	}
	
	return 0;
}

