#include <iostream>
#include <algorithm>
using namespace std;

string S;
int TC, K, N;
int p[1000], flips, ok;

int main() {
	cin >> TC;
	for(int z = 1; z <= TC; z++) {
		cin >> S >> K;
		N = S.length();
		for(int i = 0; i < N; i++)
			if(S[i] == '-')
				p[i] = 0;
			else
				p[i] = 1;
		
		flips = 0;
		for(int i = 0; i <= N - K; i++) {
			if(p[i]==0) {
				flips++;
				for(int j = i; j < i + K; j++)
					p[j] = !p[j];
			}
		}
		
		ok = 1;
		for(int i = N - K; i < N; i++)
			if(p[i]==0)
				ok = 0;
		
		if(ok)
			cout << "Case #" << z << ": " << flips << endl;
		else	
			cout << "Case #" << z << ": IMPOSSIBLE" << endl;
	}
}


