// ProblemA.cpp : コンソール アプリケーションのエントリ ポイントを定義します。
//

#include "stdafx.h"
#include <iostream>
#include <string>
using namespace std;

string str;
const string impossible = "IMPOSSIBLE";
int T;
int K;

int flip(string str, int p, int K, int n) {
	
	while (p<=str.size()-1&&str[p] == '+') {
		p++;
	}

	if (p == str.size()) 
	{
		return n;
	}
	else if(p<=str.size()-K)
	{
		str[p] = '+';
		for (int i = 1; i < K; i++) {
			str[p+i] = (str[p+i] == '+') ? '-' : '+';
		}
		return flip(str, p + 1, K, n + 1);
	}
	else return -1;
}

int main()
{
	cin >> T;
	for (int i = 1; i <= T;i++) {
		cin >> str >> K;
		int n=flip(str, 0, K, 0);
		if (n == -1) { cout << "Case #" << i << ": " << impossible << endl; }
		else {cout << "Case #" << i << ": " << n << endl;}
	}
    return 0;
}
