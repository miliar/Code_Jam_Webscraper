#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>

using namespace std;

int main() {
	FILE *fin = freopen("A-large.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("A-large.out", "w", stdout);
	int T;
	string S;
	int K;
	int out;
	cin >> T;

	for(int t = 0; t < T; t++){
		// Get N
		cin >> S >> K;
		out=0;
		for (int s=0; s<(int)S.size()-K+1; s++) {
			if (S[s]=='-') {
				for (int k=0; k<K; k++) {
					if (S[s+k]=='-')
						S[s+k]='+';
					else
						S[s+k]='-';
				}	
				out++;
			}	
		}
		//cerr << S <<endl;
		
		bool impossible=false;
		for (int k=0; k<K; k++) {
			if (S[	(int)S.size()-K+k] == '-') {
				impossible=true;
				break;
			}
		}
		if (impossible)
			cout << "Case #" << t+1 << ": IMPOSSIBLE" << endl;
		else
			cout << "Case #" << t+1 << ": " << out << endl;
	}
	return 0;
}
