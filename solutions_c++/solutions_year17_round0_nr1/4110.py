#include <iostream>
#include <string>
using namespace std;

void oneRun(){
	string in;
	int k;
	cin >> in >> k;
	int count = 0;
	for(int i=0; i < in.size(); i++) {
		if(in[i] == '-') {
			count++;
			if(i+k > in.size()) {
				cout << "IMPOSSIBLE";
				return;
			}
			for(int j = i; j < (i+k); j++) {
				if(in[j] == '+') in[j] = '-';
				else in[j] = '+';
			}
		}
	}
	cout << count;
}

int main(){
	int nums;
	cin >> nums;
	for(int i=1; i <= nums; i++) {
		cout << "Case #" << i << ": ";
		oneRun();
		cout << endl;
	}
		
	return 0;
}