#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;


int getCount (string s, int k);
bool isValid (string s);

int main () {
	
	int T;
	int tc;
	cin >> T;
	
	char c;
	bool fn;
	string s;
	int k;
	int count;

	getchar();
	
	for (tc = 1; tc <= T; tc++ ) {
        fn = false;
        s = "";
        count = 0;
        do {
           c = getchar();
           
           if (c == '-' && !fn) {
              fn = true;
           }
           
           if (fn && (c == '+' || c == '-')) {
              s += c;
           }
           
           
        } while(c == '-' || c == '+');
        
        // cout << "string: " << s << endl;

        cin >> k;
        
        getchar();

        // cout << "k: " << k << endl;
        
        count = getCount(s,k);

        // cout << "count: " << count << endl;

        if (count == -1) {
           cout << "Case #" << tc << ": " << "IMPOSSIBLE" << endl;
        } else {
           cout << "Case #" << tc << ": " << count << endl;  
        }
        
    }
	
	return 0;
}

int getCount (string s, int k) {
    
    int count = 0;
    
    if (s.size() == 0) {
       return count;
    } else if (k > s.size()) {
    	return -1;
    }
    
    for (int i = 0; i < s.size() - k + 1; i++) {
        if ( s[i] == '-' ) {
             for (int j = i; j < i+k ; j++) {
                 if (s[j] == '-' ) {
                    s[j] = '+';
                 } else {
                   s[j] = '-';
                 }
             }
             count++;
        }
    }
    
    if (isValid(s)) {
       return count;
    } else {
       return -1;
    }
}

bool isValid (string s) {
    for (int i = 0;i < s.size();i++) {
        if (s[i] == '-') {
           return false;
        }
    }
    
    return true;
}

