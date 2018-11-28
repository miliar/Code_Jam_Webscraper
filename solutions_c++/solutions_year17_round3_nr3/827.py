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
#include <cstdio>
#include <cmath>
#include <iomanip>
using namespace std;

# define M_PI           3.14159265358979323846  /* pi */

ifstream in("C-small-1-attempt3.in");
ofstream out("C-small-1-attempt3.out");
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

int main() {
	redirectIO();
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		int N, K;
		double arr[64];
		double U;
		cin >> N >> K >> U;
		for (int i = 0; i < N; i++) {
			cin >> arr[i];
		}
		sort(arr, arr + N);
		double cur = arr[0];
		int p = 0;
		while (p < N && U > 0) {
			while (p < N && arr[p] == cur) p++;
			if (p == N) {
				break;
			}
			double m = min(U, (arr[p] - cur) * p);
			U -= m;
			for (int i = 0; i < p; i++) {
				arr[i] += m / p;
			}
			cur = arr[p];
		}
		for (int i = 0; i < N; i++) {
			arr[i] += U / N;
		}
			
		double res = 1;
		for (int i = 0; i < N; i++) {
			res *= arr[i];
		}
		cout << fixed << setprecision(6);
		cout << "Case #" << i << ": "<<res<<endl;
	}
	recoverIO();
	//system("pause");
	return 0;
}

//int main() {
//	redirectIO();
//	int T;
//	cin >> T;
//	for (int i = 1; i <= T; i++) {
//		int N, K;
//		vector<double> arr(64, 0);
//		double U;
//
//		cin >> N >> K >> U;
//		for (int i = 0; i < N; i++) {
//			cin >> arr[i];
//		}
//
//		sort(arr.begin(), arr.end());
//		cout << fixed << setprecision(6);
//		double cur = arr[0];
//		int pvar = 0;
//		while (pvar < N && U > 0) {
//			while (pvar < N && arr[pvar] == cur) pvar++;
//			if (pvar == N) {
//				break;
//			}
//			double mval = min(U, (arr[pvar] - cur) * pvar);
//			U -= mval;
//			for (int i = 0; i < pvar; i++)
//				arr[i] += mval / pvar;
//			cur = arr[pvar];
//		}
//		for (int i = 0; i < N; i++) {
//			arr[i] += U / N;
//		}
//		double res = 1;
//		for (int i = 0; i < N; i++) {
//			res *= arr[i];
//		}	
//		cout << "Case #" << i << ": "<<res<<endl;
//	}
//	recoverIO();
//	//system("pause");
//	return 0;
//}


//struct interval {
//	int begin;
//	int end;
//	int type;
//	interval(int b, int e, int t):begin(b),end(e), type(t){}
//};
//
//bool cmp(const interval &a, const interval &b) {
//	return a.begin < b.begin;
//}



//int main() {
//	redirectIO();
//	int T;
//	cin >> T;
//	for (int i = 1; i <= T; ++i) {
//		int Ac, Aj;
//		cin >> Ac >> Aj;
//		int Ci, Di, Ji, Ki;
//		vector<interval> cvec, jvec, vec;
//		for (int j = 0; j < Ac; ++j) {
//			cin >> Ci >> Di;
//			vec.push_back(interval(Ci, Di, 0));
//		}
//		for (int j = 0; j < Aj; ++j) {
//			cin >> Ji >> Ki;
//			vec.push_back(interval(Ji, Ki, 1));
//		}
//
//		sort(vec.begin(), vec.end(), cmp);
//
//		int sumc = 0, sumj = 0;
//		for()
//
//		//sort(cvec.begin(), cvec.end(), cmp);
//		//sort(jvec.begin(), jvec.end(), cmp);
//
//		/*int sumc = 0, sumj = 0;
//		for (int j = 0; j < cvec.size(); ++j) {
//			sumj += cvec[j].end - cvec[j].begin;
//		}
//		for (int j = 0; j < jvec.size(); ++j) {
//			sumc += jvec[j].end - jvec[j].begin;
//		}
//		int remc = 720 - sumc, remj = 720 - sumj;
//		
//		int sizec = cvec.size();
//		int sizej = jvec.size();
//
//		if(cvec[sizej-1].begin)*/
//	}
//	recoverIO();
//	//system("pause");
//	return 0;
//}