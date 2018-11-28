#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	int t;
	string n;
	cin >> t;
	for(int i = 0; i < t; i++) {
		char min;
		int pos;
		cin >> n;
		while(1) {
			min = n[n.size()-1];
			pos = n.size()-1;
			for(int j = n.size()-2; j >= 0; j--) {
				if(n[j] > min) {
					pos = j;
					break;
				}
				else if(n[j] < min) {
					min = n[j];
				}
			}
			if(pos == n.size()-1) {
				break;
			}
			else {
				if(n[pos] == '0')
					n[pos] = '9';
				else
					n[pos] = n[pos] - 1;
				for(int j = pos+1; j < n.size(); j++) {
					n[j] = '9';
				}
			}
		}
		if (n[0] == '0') {
			n = n.substr(1,n.size()-1);
		}
		cout << "Case #" << i+1 << ": " << n << endl;

	}
	return 0;
}