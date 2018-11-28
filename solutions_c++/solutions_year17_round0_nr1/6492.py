// ConsoleApplication6.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int pan(int s[], int size, int k) {
	if (size < k) return -1;
	else if (size == k) {
		if (s[0] == 0) {
			for (int i = 0; i < size; i++) if (s[i] == 1) return -1;
			return 1;
		}
		else {
			for (int i = 0; i < size; i++) if (s[i] == 0) return -1;
			return 0;
		}
	}
	else {
		if (s[0] == 1) {
			int tmp = pan(s + 1, size - 1, k);
			if (tmp == -1) return -1;
			else return tmp;
		}
		else {
			for (int i = 0; i < k; i++) {
				if (s[i] == 1) s[i] = 0;
				else s[i] = 1;
			}
			int tmp = pan(s + 1, size - 1, k);
			if (tmp == -1) return -1;
			else return tmp + 1;
		}
	}
}

int main()
{
	ios::sync_with_stdio(false);
	ofstream outFile("output.txt");

	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		string S;
		long long N;
		cin >> S;
		cin >> N; 
		
		int str[1005];

		int size = S.size();
		for (int j = 0; j < size ; j++) {
			if (S.at(j) == '+') str[j] = 1;
			else str[j] = 0;
		}

		int a = pan(str, S.length(), N);
		if( a == -1 )
			outFile << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
		else
			outFile << "Case #" << i << ": " << a << endl;
		
		


		
	}
	return 0;
}