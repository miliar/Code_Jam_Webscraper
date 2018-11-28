#include<iostream>
#include<string>
using namespace std;

void display_tidy(string N) {
	for(int i = N.length() - 1; i >= 1; i--) {
		if(N[i] < N[i - 1]) {
			for(int j = i; j < N.length(); j++) {
				N[j] = '9';
			}
			N[i - 1]--;
		}
	}
	int j = 0;
	while(N[j] == '0') {
		j++;
	}
	while(j < N.length()) {
		cout << N[j];
		j++;
	}
	cout << endl;
}

int main() {
	int T;
	string N;
	cin >> T;
	for(int i = 1; i <= T; i++)	{
		cin >> N;
		cout << "Case #" << i << ": ";
		display_tidy(N);
	}
	return 0;
}