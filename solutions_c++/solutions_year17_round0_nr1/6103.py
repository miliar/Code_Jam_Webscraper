#include <iostream>
using namespace std;

int main() {
	int T, K;
	string S;

	cin >> T;

	for(int i=1 ; i<=T ; ++i) {
		int min = 0;
		cin >> S >> K;
		
		for(int x=0 ; x<S.length()-K+1 ; ++x) {
			if(S[x] == '-') {
				min++;
				for(int y=x ; y<x+K ; ++y) {
					S[y] = S[y] == '-' ? '+' : '-';
				}
			}
		}
		
		for(int x=S.length()-K ; x<S.length() ; ++x) {
			if(S[x] == '-') {
				min = -1;
			}
		}
		
		if (min==-1) {
			cout << "Case #" << i << ": IMPOSSIBLE" << endl;
		} else {
			cout << "Case #" << i << ": " << min << endl;
		}
	}
	return 0;
}