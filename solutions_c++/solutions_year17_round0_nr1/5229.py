#include <iostream>
#include <string>
using namespace std;

int main() {
	int tc;
	cin >> tc;
	int cont = 0;
	string S; int k;
	while (tc--) {
		cont++;
		S.clear();
		cin >> S ; cin >> k;
		int flip = 0;
		for (int i = 0; i + k <= S.size(); i++) {
			if (S[i] == '-') {
				flip++;
				for (int j = 0; j < k; j++) {
					if (S[i + j] == '-') S[i + j] = '+';
					else S[i + j] = '-';
				}
			}
			//cout << S << endl;
		}
		
		bool impossible = false;
		for (int i = 0; i < S.size() && !impossible; i++) {
			if (S[i] == '-') impossible = true;
		}

		cout << "Case #" << cont << ": ";
		if (impossible) cout << "IMPOSSIBLE" << endl;
		else cout << flip << endl;
	}




}