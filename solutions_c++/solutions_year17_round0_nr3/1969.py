// OJ.cpp : 定义控制台应用程序的入口点。
//
#include "stdafx.h"

#include <iostream>
#include <string>
#include <cstdlib>
#include <fstream>
#include <climits>
#include <cmath>
#include <sstream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

ifstream in("C-large.in");
ofstream out("C-large.out");
streambuf *cinbuf = cin.rdbuf();
streambuf *coutbuf = cout.rdbuf();

void redirectIO() {
	cin.rdbuf(in.rdbuf());
	cout.rdbuf(out.rdbuf());
}

void recoverIO() {
	cin.rdbuf(cinbuf);
	cout.rdbuf(coutbuf);
}

void precomputeTable(vector<long long int> &tbl) {
	long long int n = 1;
	for (int i = 0; i < 63; ++i) {
		tbl.push_back(n);
		n *= 2;
	}
}

int main() {
	redirectIO();
	vector<long long int> tbl;
	precomputeTable(tbl);
	int T;
	long long int N, K;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		cin >> N >> K;
		//find minimum n satisfy 2^n >= K
		long long int powerNum = 0, startNum = N, nodeCnt, power;
		for (int j = 0; j < tbl.size(); ++j) {
			powerNum += tbl[j];
			if (powerNum >= K) {
				if (powerNum >= N) {
					cout << "Case #" << i << ": 0 0" << endl;
					goto endloop;
				}
				power = j;
				nodeCnt = powerNum - tbl[j];
				break;
			}
			startNum /= 2;
		}
		long long int sum = N - nodeCnt;
		long long int biggerIdx = tbl[power] - (startNum*tbl[power] - sum);
		long long int idx = K - nodeCnt;
		long long int curCnt;
		curCnt = (idx <= biggerIdx ? startNum : startNum - 1);
		long long int s1 = curCnt / 2, s2 = (curCnt&1 ? curCnt/2 : curCnt/2 - 1);
		cout << "Case #" << i << ": " << max(s1, s2) << " " << min(s1, s2) << endl;
	endloop:;
	}
	recoverIO();
	//system("pause");
	return 0;
}

// C-small-1 optimize
//int main() {
//	//redirectIO();
//	int T, N, K;
//	cin >> T;
//	for (int i = 1; i <= T; ++i) {
//		cin >> N >> K;
//		if (K > (N+1) / 2) {
//			cout << "Case #" << i << ": 0 0" << endl;
//			continue;
//		}
//		priority_queue<int> q;
//		q.push(N);
//		int minVal = -1, maxVal = -1;
//		for (int j = 0; j < K; ++j) {
//			int len = q.top();
//			q.pop();
//			int s1 = len / 2, s2 = (len & 1 ? len / 2 : len / 2 - 1);
//			minVal = min(s1, s2);
//			maxVal = max(s1, s2);
//			q.push(s1);
//			q.push(s2);
//		}
//		cout << "Case #" << i << ": " << maxVal << " " << minVal << endl;
//	}
//
//	//recoverIO();
//	system("pause");
//	return 0;
//}

// C-small-1
//int main() {
//	redirectIO();
//	int T, N, K;
//	cin >> T;
//	for (int i = 1; i <= T; ++i) {
//		cin >> N >> K;
//		
//		vector<bool> occupy(N + 2, false);
//		occupy[0] = occupy[N + 1] = true;
//		
//		vector<int> leftStall(N + 2, 0);
//		for (int j = 1; j <= N; ++j) {
//			leftStall[j] = j - 1;
//		}
//
//		vector<int> rightStall(N + 2, 0);
//		for (int j = 1; j <= N; ++j) {
//			rightStall[j] = N - j;
//		}
//
//		for (int j = 0; j < K; ++j) {
//			int minVal = -1, maxVal = -1, oidx = -1;
//			for (int k = 1; k <= N; ++k) {
//				if (!occupy[k]) {
//					int Ls = leftStall[k], Rs = rightStall[k];
//					if (min(Ls, Rs) > minVal) {
//						oidx = k;
//						minVal = min(Ls, Rs);
//						maxVal = max(Ls, Rs);
//					}
//					else if (min(Ls, Rs) == minVal && max(Ls, Rs) > maxVal) {
//						oidx = k;
//						maxVal = max(Ls, Rs);
//					}
//				}
//			}
//			occupy[oidx] = true;
//			for (int k = oidx + 1; k <= N && !occupy[k]; ++k) {
//				leftStall[k] = k - oidx - 1;
//			}
//			for (int k = oidx - 1; k >= 1 && !occupy[k]; --k) {
//				rightStall[k] = oidx - k - 1;
//			}
//			if (j == K - 1) {
//				cout << "Case #" << i << ": " << maxVal << " " << minVal << endl;
//			}
//		}
//	}
//	recoverIO();
//	//system("pause");
//	return 0;
//}

//long long int getBase(long long int n) {
//	long long int base = 1;
//	while (n / 10) {
//		base *= 10;
//		n /= 10;
//	}
//	return base;
//}
//
//string LLtoString(long long int n) {
//	stringstream s;
//	s << n;
//	string ret;
//	s >> ret;
//	return ret;
//}
//
//long long int StringtoLL(string str) {
//	stringstream s;
//	s << str;
//	long long int ret;
//	s >> ret;
//	return ret;
//}

// B-large
//int main() {
//	redirectIO();
//	int T;
//	long long int N, base;
//	string str;
//	cin >> T;
//	for (int i = 1; i <= T; ++i) {
//		cin >> N;
//		base = getBase(N);
//		str = LLtoString(N);
//		char last = '1', ch;
//		int invalid = -1;
//		for (int j = 0; j < str.length(); ++j) {
//			if (str[j] < last) {
//				invalid = j - 1;
//				ch = str[j - 1];
//				for (; j < str.length(); ++j) {
//					str[j] = '0';
//				}
//			}
//			last = str[j];
//		}
//		if (invalid != -1) {
//			while (invalid-1 >= 0 && str[invalid-1] == ch) {
//				str[invalid] = '0';
//				--invalid;
//			}
//			cout << "Case #" << i << ": " << StringtoLL(str) - 1 << endl;
//		}
//		else {
//			cout << "Case #" << i << ": " << StringtoLL(str) << endl;
//		}
//		
//	}
//	recoverIO();
//	//system("pause");
//	return 0;
//}

// A-small and A-large
//int main() {
//	redirectIO();
//	int T, K;
//	string S;
//	cin >> T;
//	for (int i = 1; i <= T; ++i) {
//		cin >> S >> K;
//		int cnt = 0;
//		int slen = S.length();
//		for (int j = 0; j <= slen - K; ++j) {
//			if (S[j] == '-') {
//				++cnt;
//				for (int k = 0; k < K; ++k) {
//					S[k + j] = (S[k + j] == '+' ? '-' : '+');
//				}
//			}
//		}
//		if (S == string(slen, '+')) {
//			cout << "Case #" << i << ": " << cnt << endl;
//		}
//		else {
//			cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
//		}
//	}
//	recoverIO();
//	//system("pause");
//	return 0;
//}

// B-small
//bool check(int n) {
//	int base = 1, tmp = n;
//	while (tmp/10) {
//		tmp /= 10;
//		base *= 10;
//	}
//	tmp = n;
//	int last = -1, cur;
//	while (base) {
//		cur = tmp / base;
//		if (cur < last) {
//			return false;
//		}
//		last = cur;
//		tmp %= base;
//		base /= 10;
//	}
//	return true;
//}
//
//int main() {
//	redirectIO();
//	int T, N;
//	cin >> T;
//	for (int i = 1; i <= T; ++i) {
//		cin >> N;
//		while (!check(N)) --N;
//		cout << "Case #" << i << ": " << N << endl;
//	}
//	recoverIO();
//	return 0;
//}