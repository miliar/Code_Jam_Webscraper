#include <bits/stdc++.h>
using namespace std;

int nx[256];

string solveSmall(int N, int R, int Y, int B) {
	assert(N == R + Y + B);
	
	string s = "";
	for (int i = 0; i < N; i++) {
		s += 'X';
	}
	
	if (R >= Y && R >= B) {
		for (int k = 0; k < N && R > 0; k += 2) {
			s[k] = 'R';
			R--;
		}
	} else if (Y >= B) {
		for (int k = 0; k < N && Y > 0; k += 2) {
			s[k] = 'Y';
			Y--;
		}
	} else {
		for (int k = 0; k < N && B > 0; k += 2) {
			s[k] = 'B';
			B--;
		}
	}
	
	for (int k = 0; k < N; k += 2) {
		if (s[k] != 'X') continue;
		
		if (R > 0) {
			s[k] = 'R';
			R--;
		} else if (Y > 0) {
			s[k] = 'Y';
			Y--;
		} else if (B > 0) {
			s[k] = 'B';
			B--;
		}
	}
	for (int k = 1; k < N; k += 2) {
		if (R > 0) {
			s[k] = 'R';
			R--;
		} else if (Y > 0) {
			s[k] = 'Y';
			Y--;
		} else if (B > 0) {
			s[k] = 'B';
			B--;
		}
	}
	
	for (int i = 0; i < N; i++) {
		assert(s[i] != 'X');
	}
	
	if (N == 1) return s; // duh
	
	// check
	for (int i = 1; i < N-1; i++) {
		if (s[i] == s[i-1] || s[i] == s[i+1]) {
			return "IMPOSSIBLE";
		}
	}
	
	if (s[0] == s[1] || s[0] == s[N-1]) return "IMPOSSIBLE";
	if (s[N-1] == s[0] || s[N-1] == s[N-2]) return "IMPOSSIBLE"; 
	
	return s;
}

string solve(int N, int R, int O, int Y, int G, int B, int V) {
	while (N > 3) {
		if (O > 0) {
			// BOB --> B
			N -= 2;
			O--;
			B--;
		} else if (G > 0) {
			// RGR --> R
			N -= 2;
			G--;
			R--;
		} else if (V > 0) {
			// YVY --> Y
			N -= 2;
			V--;
			R--;
		} else {
			// only RYB remain
			string s = solveSmall(N, R, Y, B);
			if (s == "IMPOSSIBLE") {
				return s;
			}
			// there's a solution - replace elements of s with O,G,V
		}
	}
	
	assert((N==2) || (N==3));
	
	return "";
}

int main() {
	int ncases;
	cin >> ncases;
	for (int icase = 1; icase <= ncases; icase++) {
		int N;
		int R, O, Y, G, B, V;
		
		cin >> N;
		cin >> R >> O >> Y >> G >> B >> V;
		
		if (O > 0 || G > 0 || V > 0) continue;
		
		nx['R'] = R;
		nx['O'] = O;
		nx['Y'] = Y;
		nx['G'] = G;
		nx['B'] = B;
		nx['V'] = V;
			
		
		//string ans = solve(N, R, O, Y, G, B, V);
		string ans = solveSmall(N, R, Y, B);
		cout << "Case #" << icase << ": ";
		cout << ans << endl;
		//if (!ok) {
			//cout << "IMPOSSIBLE" << endl;
		//} else {
			
		//}
	}
	return 0;
}
