#include <iostream>
#include <string>
#include <stdlib.h>

using namespace std;

int main() {
	int t, i, j, l;
	cin >> t;
	string n;
	for(l = 0; l < t; l++){
		cin >> n;
		int index_start = 0;
		for(i = 0; i < n.length() - 1; i++) {
			if(n[i] > n[i+1]) {
				n[index_start]--;
				for(j = index_start + 1; j < n.length(); j++) {
					n[j] = '9';
				}
			} else if(n[i] < n[i+1]){
				index_start = i+1;
			}
		}
		int flag = 1;
		cout << "Case #" << l+1 << ": ";
		for(i = 0; i < n.length(); i++) {
			if(flag && n[i]-48 == 0) {
				continue;
			} else {
				flag = 0;
				cout << n[i]-48;
			}
		}
		cout << endl;
	}
	return 0;
}
