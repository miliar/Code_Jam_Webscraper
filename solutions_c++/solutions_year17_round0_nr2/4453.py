#include <iostream>
#include <fstream>
#include <algorithm>
#include <list>
#include <stack>
#include <vector>
#include <string>
#include <cstring>
#include <cstdio>
#include <unordered_map>

using namespace std;

int main(int ac, char **av)
{
	int T;
	cin >> T;
	char N[100];
	for (int i = 0 ; i < T; i++) {
		cin >> N;
		//cout << "N: " << N << endl;
		int L = strlen(N);
		for (int l = L; l > 1; l--) {
			bool fill_nine = false;
			for (int j = 0; j < l-1; j++) {
				if (fill_nine)
					N[j] = N[j+1] = '9';
				else if (N[j] > N[j+1]) {
					N[j]--;
					N[j+1] = '9';
					fill_nine = true;
				}
			}
			if (!fill_nine) break;
		}
		const char * P = N;
		for (int j = 0; j < L; j++) {
			if (*P == '0') P++;
		}
		cout << "Case #" << (i+1) << ": " << P << endl;
	}
	return 0;
}

