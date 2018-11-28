#include <iostream>
#include <string>

using namespace std;

char pony[1000];
int R, O, Y, G, B, V;
int Q[3];
char L[3];

int main() {
	int T;
	cin >> T;
	for (int iCase = 1; iCase <= T; iCase++) {
		int N;
		cin >> N >> R >> O >> Y >> G >> B >> V;
		
		// Small
		bool possible = true;
		if (R > 0 && N / R < 2)
			possible = false;
		if (Y > 0 && N / Y < 2)
			possible = false;
		if (B > 0 && N / B < 2)
			possible = false;
		
		if (!possible) {
			cout << "Case #" << iCase << ": " << "IMPOSSIBLE" << endl;
		}
		else {
			if (R >= Y && R >= B) {
				Q[0] = R;
				L[0] = 'R';
				if (Y >= B) {
					Q[1] = Y;
					L[1] = 'Y';
					Q[2] = B;
					L[2] = 'B';
				}
				else {
					Q[1] = B;
					L[1] = 'B';
					Q[2] = Y;
					L[2] = 'Y';
				}
			}
			else if (Y >= B) {
				Q[0] = Y;
				L[0] = 'Y';
				if (R >= B) {
					Q[1] = R;
					Q[2] = B;
					L[1] = 'R';
					L[2] = 'B';
				}
				else {
					Q[1] = B;
					Q[2] = R;
					L[1] = 'B';
					L[2] = 'R';
				}
			}
			else {
				Q[0] = B;
				L[0] = 'B';
				if (R >= Y) {
					Q[1] = R;
					L[1] = 'R';
					Q[2] = Y;
					L[2] = 'Y';
				}
				else {
					Q[1] = Y;
					L[1] = 'Y';
					Q[2] = R;
					L[2] = 'R';
				}
			}
			char prev = L[2];
			for (int i = 0; i < N; i++) {
				if (L[0] != prev && Q[0] >= Q[1] && Q[0] >= Q[2]) {
					pony[i] = L[0];
					Q[0]--;
					prev = L[0];
				}
				else if (L[1] != prev && Q[1] >= Q[2]) {
					pony[i] = L[1];
					Q[1]--;
					prev = L[1];
				}
				else {
					pony[i] = L[2];
					Q[2]--;
					prev = L[2];
				}
			}
			
			cout << "Case #" << iCase << ": ";
			for (int i = 0; i < N; i++)
				cout << pony[i];
			//~ for (int i = 0; i < N-1; i++)
				//~ if (pony[i] == pony[i+1])
					//~ cout << "Error" << endl;
			//~ if (pony[0] ==  pony[N-1])
				//~ cout << "Error" << endl;
			cout << endl;
		}
	}
}
