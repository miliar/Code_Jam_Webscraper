#include <iostream>

using namespace std;

typedef unsigned long long int lli;

int main() {
	int T, cont = 1;

	cin >> T;

	while(T--) {
		lli N;
		int n[20], tam = 0;

		cin >> N;
		for(int i = 0; N != 0; i++) {
			n[i] = N % 10;
			N = N / 10;
			tam++;
		}

		for(int i = 0; i < tam/2; i++) {
			int troca = n[i];
			n[i] = n[tam - i - 1];
			n[tam - i - 1] = troca;
		}

		if(tam == 1)
			cout << "Case #" << cont++ << ": " << n[0] << endl;
		else {
			for(int i = 1; i < tam; i++) {
				if(n[i] < n[i - 1]) {
					n[i - 1]--;
					for(int j = i; j < tam; j++)
						n[j] = 9;
					if(i > 1)
						i -= 2;
				}
			}

			cout << "Case #" << cont++ << ": ";

			int t = 0;
			while(!n[t])
				t++;
			for(int i = t; i < tam; i++)
				cout << n[i];
			cout << endl;
		}
	}
	
	return 0;
}