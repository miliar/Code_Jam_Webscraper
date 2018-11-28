// ConsoleApplication6.cpp : �ܼ� ���� ���α׷��� ���� �������� �����մϴ�.
//

#include "stdafx.h"
#include <fstream>
#include <iostream>

using namespace std;


bool isTidy(int n) {
	int a, b, c;

	if (n < 10) return true;
	else if (n < 100) {
		b = n / 10;
		c = n % 10;
		if (b <= c) return true;
		else return false;
	}
	else {
		a = n / 100;
		b = n / 10 - a * 10;
		c = n % 10;
		if (a <= b && b <= c) return true;
		else return false;
	}
}
int main()
{
	ios::sync_with_stdio(false);
	ofstream outFile("output.txt");

	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		
		long long N;
		cin >> N;
		
		if (N == 1000) N = 999;

		for (int j = N; j >= 1; j--) {
			if (isTidy(j)) {
				outFile << "Case #" << i << ": " << j << endl;
				break;
			}
		}







	}
	return 0;
}