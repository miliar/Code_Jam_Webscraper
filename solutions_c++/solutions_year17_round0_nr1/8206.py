#include <iostream>
#include <string.h>
#include <algorithm>
using namespace std;
char Pancake[1000] = { };

void flip(int i, int k) {
	for (int j = i; j < i + k; j++)
		(Pancake[j] == '-') ? Pancake[j] = '+' : Pancake[j] = '-';
}

int main() {
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		int K;
		int count = 0;
		memset(Pancake, 0, sizeof(Pancake));
		cin >> Pancake;
		cin >> K;
		for (int pn = 0; pn <= strlen(Pancake) - K; pn++) {
			if (Pancake[pn] == '-') {
				flip(pn, K);
				count++;
			}
		}
		if (find(Pancake, Pancake + strlen(Pancake), '-')
				== (Pancake + strlen(Pancake)))
			cout << "Case #" << t + 1 << ": " << count<<endl;
		else
			cout << "Case #" << t + 1 << ": IMPOSSIBLE"<<endl;

	}
}
