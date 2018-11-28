#include<iostream>
#include<fstream>
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;

int main() {
	int T;
	string S;
	ifstream fin("inputLarge.in");
	ofstream fout("outputLarge.out");
	fin >> T;
	for (int i = 1; i <= T; i++) {
		fin >> S;
		for (int j = 0; j < S.length()-1; j++) {
			if (S[j] > S[j + 1]) {
				//make all digits after 'j' = 9
				int k = j+1;
				while (k < S.length()) {
					S[k++] = '9';
				}
				//make digit at 'j' 1 lesser, if it is not zero and recursively check that previous is smaller or same
				do {
					if (S[j] > '0') {
						S[j]--;
						//check previous digits
						if (j>0 && S[j - 1] > S[j]) {
							S[j] = '9';
							j--;
							continue;
						}
					}
					else {
						S[j] = '9';
						j--;
						continue;
					}
					//control comes here if previous digits tidy
					break;
				} while (j >= 0);
				break; //all digits taken care in one go
			}
		}
		//remove all leading zeroes from result
		int zeroIndex = 0;
		for (int j = 0; j < S.length(); j++) {
			if (S[j] != '0') {
				zeroIndex = j;
				break;
			}
		}
		S.erase(0, zeroIndex);
		//Cases for final result
		//1. if string becomes empty
		if (S.length() == 0) {
			fout << "Case #" << i << ": " << 0<<endl;
		}
		else {
			fout << "Case #" << i << ": " << S<<endl;
		}
	}
}