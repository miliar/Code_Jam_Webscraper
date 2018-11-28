#include <iostream>
using namespace std;
int T, N, lastTidyNumber;

bool tidy(int x) {
	string s = "";
	while(x>0) {
		s+= char(x%10);
		x/= 10;
	}
	for(int i=0; i<s.length(); i++)
		if(s[i] < s[i+1])
			return false;
	return true;
}

int main() {
	cin >> T;
	for(int i=0; i<T; i++) {
		cin >> N;
		for(int j=1; j<= N; j++)
			if(tidy(j))
				lastTidyNumber = j;
		cout << "Case #" << i+1 << ": " << lastTidyNumber << "\n";
		lastTidyNumber = 0;
	}
	return 0;
}