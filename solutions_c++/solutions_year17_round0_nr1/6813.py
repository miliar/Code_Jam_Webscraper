#include<iostream>
#include<string>
#include<fstream>
int arr[100];
using namespace std;
int main() {
	ifstream input;
	ofstream output;
	input.open("A-large.in");
	output.open("OUT.in");
	int T, K, c = 0;
	string S;
	input >> T;
	int f = T;
	while (T--) {
		int steps = 0;
		input >> S >> K;
		for (int j = 0; j < S.size(); j++) {
			if (S[j] == '-')
				if (j + K >  S.size()) {
					steps = -1; break;
				}
				else {
					for (int v = j; v < j + K; v++) {
						if (S[v] == '-') S[v] = '+';
						else if (S[v] == '+') S[v] = '-';
					}
					steps++;
				}
		}
		arr[c] = steps; c++;
	}
	for (int i = 0; i < f; i++) {
		output << "Case #" << i + 1 << ": ";
		if (arr[i] == -1) output << "IMPOSSIBLE\n";
		else output << arr[i] << "\n";
	}
	return 0;
}