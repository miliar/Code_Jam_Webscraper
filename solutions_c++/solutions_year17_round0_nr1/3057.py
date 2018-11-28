#include<iostream>
#include<fstream>
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;

int main() {
	int T, K, counter, flipCount, indexToResume;
	bool containsMinus, impossible;
	string S;
	ifstream fin("inputLarge.in");
	ofstream fout("outputLarge.out");
	fin >> T;
	for (int i = 1; i <= T; i++) {
		fin >> S >> K;
		flipCount = 0;
		impossible = false;
		for (int j = 0; j < S.length(); ) {			
			if (S[j] == '-') {
				if ((S.length() - j) < K) {
					fout << "Case #" << i << ": IMPOSSIBLE"<<endl;
					impossible = true;
					break;
				}
				counter = 0;			
				//index on all '+' encounter
				indexToResume = j + K;
				//flip K
				do {
					if (S[j] == '-') {
						S[j] = '+';
					}
					else if (S[j] == '+') {
						S[j] = '-';
						//save first '-' index
						indexToResume = (indexToResume <= j) ? indexToResume : j;
					}
					j++;
					counter++;
				} while (counter < K);
				flipCount++;
				j = indexToResume;
			}
			else {
				j++;
			}
		}
		if (impossible) continue;
		containsMinus = false;
		for (int j = 0; j < S.length(); j++) {
			if (S[j] == '-') {
				containsMinus = true;
				break;
			}
		}
		if (containsMinus) {
			fout << "Case #" << i << ": IMPOSSIBLE"<<endl;
		}
		else {
			fout << "Case #" << i << ": " << flipCount << endl;
		}
	}
}