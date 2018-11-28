#include <bits/stdc++.h>
using namespace std;

int T, R, C;
vector <string> S;

struct limits {
	int r1, r2, c1, c2;
	limits() { r1=100; r2=0; c1=100; c2=0; }
	bool intersect(limits &L) {
		return (r1 <= L.r2 && L.r1 <= r2 && c1 <= L.c2 && L.c1 <= c2);
	}
};

map <char, limits> M;
map <char, bool> seen;

bool found;

bool go(char ch, int filled) {
	if (filled == R*C) 
		return true;

	while (ch <= 'Z' && !seen[ch]) ch++;
	if (ch > 'Z') return false;

	limits L;
	limits Mch = M[ch];
	for (L.r1=0; L.r1<=Mch.r1; L.r1++)
		for (L.c1=0; L.c1<=Mch.c1; L.c1++)
			for (L.r2=Mch.r2; L.r2<R; L.r2++)
				for (L.c2=Mch.c2; L.c2<C; L.c2++) {
					bool ok = true;
					for (auto &m:M)
						if (m.first != ch && m.second.intersect(L)) {
							ok = false;
							break;
						}
					if (ok) {
						M[ch] = L;
						if (go(ch+1, filled + (L.r2-L.r1+1)*(L.c2-L.c1+1))) return true;
						M[ch] = Mch;
					}
				}
	return false;
}

int main() {	
	cin >> T;
	for (int t=1; t<=T; t++) {
		cin >> R >> C;
		S.resize(R);
		M.clear();
		seen.clear();
		found = false;
		
		for (int r = 0; r < R; r++) {
			cin >> S[r];
			for (int c = 0; c < C; c++) {
				char ch = S[r][c];
				if (ch != '?') {
					seen[ch] = true;
					auto &Mch = M[ch];
					Mch.r1 = min(Mch.r1, r);
					Mch.r2 = max(Mch.r2, r);
					Mch.c1 = min(Mch.c1, c);
					Mch.c2 = max(Mch.c2, c);
				}
			}
		}

		go('A', 0);

		for (char ch='A'; ch<='Z'; ch++)
			if (seen[ch]) {
				for (int r=M[ch].r1; r<=M[ch].r2; r++)
					for (int c=M[ch].c1; c<=M[ch].c2; c++)
						S[r][c] = ch;
			}

		cout << "Case #" << t << ":" << endl;
		for (int r = 0; r < R; r++)
			cout << S[r] << endl;
	}
}
