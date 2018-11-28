#include <iostream>
#include <string>
using namespace std;

int main() {
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
	    string s; int k, count = 0;
	    cin >> s >> k;
	    for(int i = 0; i <= s.size() - k; i++) {
	        if(s[i] == '-') {
	            count ++;
	            for(int j = i; j < i + k; j++) {
	                if(s[j] == '-') {
	                    s[j] = '+';
	                }
	                else {
	                    s[j] = '-';
	                }
	            }
	        }
	    }
	    int f = 0;
	    for(int i = 0; i < s.size(); i++) {
	        if(s[i] == '-') {
	            f = 1;
	        }
	    }
	    cout << "Case #"<<t<<": ";
	    if(f == 0) {
	        cout << count << endl;
	    }
	    else {
	        cout << "IMPOSSIBLE" << endl;
	    }
	}
	return 0;
}
