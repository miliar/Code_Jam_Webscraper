#include <iostream>
using namespace std;

bool isTidy(int inp) {
	int rem = 9;
	while(inp>0) {
		if(rem>=inp%10) {
			rem = inp%10;
			inp = inp/10;	
		} else {
			return false;
		}
	}
	return true;
}

int getLastTidy(int inp) {
	while(inp>0) {
		if(isTidy(inp))
			return inp;
		inp--;
	}
}

int main() {
	// your code goes here
	int tc;
	cin >> tc;
	for(int i=0;i<tc;i++) {
		int inp, ans;
		cin >> inp;
		cout << "Case #" << i+1 << ": " << getLastTidy(inp) << endl;
	}
	return 0;
}
