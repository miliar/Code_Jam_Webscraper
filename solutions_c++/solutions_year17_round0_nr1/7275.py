#include<stdio.h>
#include<iostream>
#include<string>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int n = 0; n < T; n++) {
		int K, pivot = 0, score = 0;
		string str;
		cin >> str >> K;
		while (1) {
			//cout <<"Pivot "<< pivot << " Str " << str << " K " << K << endl;

			if (pivot == (int)str.size() - 1 && str[pivot] == '+') {
				cout << "Case #" << n + 1 << ": " << score << endl;
				break;
			}
			else if (str[pivot] == '-') {
				if (pivot + K > (int)str.size()) {
					cout << "Case #" << n + 1 << ": " << "IMPOSSIBLE" << endl;
					break;
				}
				else {
					score++;
					for (int i = pivot; i < pivot + K; i++) {
						if (str[i] == '-') {
							str[i] = '+';
						}
						else {
							str[i] = '-';
						}
					}
				}
			}
			pivot++;
		}
	}
}