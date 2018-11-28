// q1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "iostream"
#include "string"
using namespace std;


int main()
{
	int T;
	string S;
	int K;

	cin >> T;

	for (int Tl = 1; Tl <= T; ++Tl){
		cin >> S;
		cin >> K;
		int f = 0;
		int i = 0;

		for (; i < S.length() ; ++i) {
			if (S[i] == '-') {
				f++;
				if (i <= S.length() - K) {
					for (int flip = 0; flip < K; ++flip) {
						S[flip + i] = S[flip + i] == '-' ? '+' : '-';
					}
				}else{
					break;
				}
			}
		}
		cout << "Case #" << Tl << ": ";
		if (i == S.length()) cout << f; else cout << "IMPOSSIBLE";
		cout << endl;
	}
	return 0;
}

