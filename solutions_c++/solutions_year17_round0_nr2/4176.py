#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	// your code goes here
	int t;
	string current;
	cin >> t;
	for (int l = 1; l <= t; l++) {
	    cin >> current;
	    if (current.length() == 1) {
	        cout << current << endl;
	        //cout << "Case #" << l << ": " << current << "\n";
	    } else {
	        //cout << "Case #" << l << ": ";
	        for (int x = 0; x < current.length() - 1; x++) {
	            if ((int)current[x] > (int)current[x + 1]) {
	                current[x] = (char)((int)current[x] - 1);
	                for (int i = x + 1; i < current.length(); i++) {
	                    current[i] = '9';
	                }
	                for (int i = x - 1; i >= 0; i--) {
	                    if (current[i + 1] < current[i]) {
	                        current[i] = min (current[i], current[i + 1]);
	                        current[i + 1] = '9';
	                    } else {
	                        current[i] = min (current[i], current[i + 1]);
	                    }
	                    /*if (current[i] == current[i + 1]) {
	                        current[i + 1] = '9';
	                    }*/
	                }
	                break;
	            }
	        }
	        for (int x = current.length() - 1; x > 0; x--) {
	            if (current[x] <= '0') {
	                current[x] = '9';
	                current[x - 1] = (char)((int)current[x - 1] - 1);
	            }
	        }
	        if (current[0] <= '0') {
	            for (int x = 1; x < current.length(); x++) {
	                printf ("%c", current[x]);
	            }
	        } else {
	            for (int x = 0; x < current.length(); x++) {
	                printf ("%c", current[x]);
	            }
	        }
	        printf ("\n");
	    }
	}
	return 0;
}
