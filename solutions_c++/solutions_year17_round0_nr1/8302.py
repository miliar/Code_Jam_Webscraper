#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long int ullint;

int T;
int _case;
int K;
int ris=0;
bitset <15> S;

void palata (int pos);

int main() {
	int i, j, elem;
	char c;
	bool ok, fatto;
	
	cin >> T;
	
	for (_case=1; _case<=T; _case++) {
		S.reset();
		cin.get();
		c = cin.get();
		for (i=0; c!=' '; i++) {
			if (c=='+') {
				S[i] = true;
			}
			c = cin.get();
		}
		elem = i;
		cin >> K;
		//cout << S << " " << endl;
		
		ris=0;
		
		fatto = false;
		while (!fatto) {
			fatto = true;
			for (i=0; i<=elem-K && fatto; i++) {
				//cout << i << ") " << S[i] << endl;
				if (!S[i]) {
					fatto = false;
					palata(i);
					//cout << S << endl;
				}
			}
		}
		
		fatto = true;
		for (i=0; i<elem && fatto; i++) {
			if (!S[i])
				fatto=false;
		}
		
		if (fatto)
			cout << "case #" << _case << ": " << ris << "\n";
		else
			cout << "case #" << _case << ": IMPOSSIBLE\n";
	}
	
	return 0;
}

void palata (int pos) {
	int j;
	for (j=0; j<K; j++) {
		S[pos+j] = !S[pos+j];
	}
	ris++;
}

/*
			for (; i<elem && fatto; i++) {
				if (!S[i]) {
					fatto = false;
				}
			}*/
			
/*
					ok = true;
					for (j=1; j<K; j++) {
						if (S[i+j]) {
							ok = false;
						}
					}
					if (ok) {
						palata(i);
					}
					*/
