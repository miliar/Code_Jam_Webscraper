#include<iostream>
#include<string>
using namespace std;

void min_flip(string S, int K) {
	int i = 0, c = 0;
	while(i + K <S.length()) {
		if(S[i] == '-') {
			for(int j = i; j < i + K; j++) {
				if(S[j] == '-') {
					S[j] = '+';
				} else {
					S[j] = '-';
				}
			}
			c++;
		}
		i++;
	}
	while(i < S.length() - 1) {
		if(S[i] != S[i+1]) {
			cout << "IMPOSSIBLE" << endl;
			return;
		}
		i++;
	}
	if(S[i] == '-') {
		c++;
	}
	cout << c << endl;
}

int main() {
	short T, K;
	string S;
	cin >> T;
	for(int i = 1; i <= T; i++)	{
		cin >> S >> K;
		cout << "Case #" << i << ": " ;
		min_flip(S, K);
	}
	return 0;
}