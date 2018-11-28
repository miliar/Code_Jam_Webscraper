#include <iostream>
#include <string>
using namespace std;


	


int main() {
	int t;
	string n = "";
	cin >> t;
	cin.ignore();
	for(int i=1; i<= t; i++) {
		getline(cin,n);
		int current_char = n.length() - 1;
		while(current_char > 0) {
			if(n[current_char] < n[(current_char - 1)]) {
				n[(current_char - 1)] = n[(current_char - 1)] - 1;
				for(int j = current_char; j < n.length(); j++) {
					n[j] = '9';
				}
			}
			current_char--;
		}
		while(n[0] == '0') {
			n = n.substr(1, n.length()-1);
		}
		cout << "Case #" << i << ": " << n << endl;
		n.clear();
	}
	return 0;
}