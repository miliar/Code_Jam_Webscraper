#include <iostream>
using namespace std;

int main() {
	int T;
	string N;

	cin >> T;

	for(int t=1 ; t<=T ; ++t) {
		cin >> N;

		for(int x=0, len = N.length() ; x<len-1 ; ++x) {
			if(N[x] > N[x+1]) {
				for(int y=x+1 ; y<len ; ++y) {
					N[y] = '9';
				}

				N[x]--;
				for(int y=x-1 ; y>=0 ; --y) {
					if(N[y+1] == '0') {
						N[y+1] = '9';
						N[y]--;
					}

					if(N[y] > N[y+1]) {
						N[y]--;
						N[y+1] = '9';
					}
				}
				break;
			}
		}

		for(int y=0, len = N.length() ; y<len ; ++y) {
			if(N[y] != '0') {
				cout << "Case #" << t << ": " << N.substr(y,N.length()) << endl;
				break;
			}
		}
	}
	return 0;
}
