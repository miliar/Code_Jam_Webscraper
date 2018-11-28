#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

char S[25];
int TC, N;

int main() {
	cin >> TC;
	for(int z = 1; z <= TC; z++) {
		cin >> S;
		N = strlen(S);
		for(int i = 1; i < N; i++)
			if(S[i] < S[i-1]) {
				while(i-1 >= 0 && S[i-1] == '1')
					i--;
				if(i-1 < 0)
					N--;
				else
					S[i-1]--;
				for(int j = i; j < N; j++)
					S[j] = '9';
				S[N] = '\0';
				if(i-1 < 0)
					break;
				else	
					i -= 2;
			}
		cout << "Case #" << z << ": " << S << endl;
	}
}


