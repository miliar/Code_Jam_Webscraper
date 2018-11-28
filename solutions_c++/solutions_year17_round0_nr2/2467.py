#include <iostream>
using namespace std;

int main() {
	int t; cin >> t;
	for (int c = 1; c <= t; c++) {
	    string s;
	    cin >> s;
	    int r = s.size();
	    while(true) {
	        int i;
    	    for (i = 1; i < r; i++) {
    	        if (s[i] < s[i - 1]) {
    	            s[i - 1]--;
    	            break;
    	        }
    	    }
    	    if (i == r) break;
    	    r = i;
	    }
	    for (int i = r; i < s.size(); i++) {
	        s[i] = '9';
	    }
	    while (s[0] == '0') s.erase(s.begin());

	    cout << "Case #" << c << ": ";
	    cout << s;
	    cout << endl;
	}
	return 0;
}
