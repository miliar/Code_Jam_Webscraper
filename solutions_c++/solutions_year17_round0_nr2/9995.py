#include <iostream>  // includes cin to read from stdin and cout to write to stdout

using namespace std;  // since cin and cout are both in namespace std, this saves some text

void main() {
	int t;
	char n[20];
	char out[20];
	  
	cin >> t;
	cin.getline(n, 20);
	for (int i = 1; i <= t; ++i) {
		cin.getline(n, 20);
		int count;
		for (int j = 0; j < 20; j++) {
			if ( n[j] == '\0') {
				count = j;
				break;
			}
		}
		
		for (int j = 0; j < count; j++) {
			out[j] = n[j];
			for (int k = j+1; k < count; k++) {
				if (n[k] > n[j]) {
					break;
				} else if (n[k] < n[j]) {
					out[j] = n[j] - 1;
					break;
				}
			}
			
			// special case
			if (out[j] != n[j]) {
				for (int k = j+1; k < count; k++) {
					out[k] = '9';
				}
				break;
			}
		}
		
		cout << "Case #" << i << ": ";
        for(int j = 0; j < count; j++) {
             if (j == 0 && out[j] == '0')    continue;
			cout << out[j];
		}
		cout << endl;
	}
}