// ConsoleApplication1.cpp : Defines the entry point for the console application.
//
#ifdef _MSC_VER
#include "stdafx.h"
#endif
#include <assert.h>
#include <vector>
#include <algorithm>
#include <iostream>
#include <string>
// ConsoleApplication1.cpp : Defines the entry point for the console application.
//
#ifdef _MSC_VER
#include "stdafx.h"
#endif
#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#define X first
#define Y second
typedef long long ll;
using namespace std;
int precomputed[2010];

#ifdef WIN32
int __stdcall WinMain(int hThisInstance, int hPrevInstance, int lpszArgument, int nCmdShow)
#else
int main()
#endif
{
	int T; cin >> T;
	for (int t = 0; t < T; t++) {
		map<ll, ll>X;
		ll N, K; 
		cin >> N >> K;
		X[N]++;
		auto P = X.rbegin();
		
		do {
			P = X.rbegin();
			//cout << P->X << " " << P->Y << endl;
			if (K <= P->Y)break;
			else {
				K -= P->Y;
				if(P->X / 2 > 0);
					X[P->X / 2] += P->Y;
				if(P->X - 1 - P->X / 2>0)
				X[P->X - 1 - P->X / 2] += P->Y;
				X.erase(P->X);
			}
		} while (true);
		ll A = P->X / 2;
		ll B =P->X-1-A;
		if (A < B)swap(A, B);
		cout << "Case #" << t+1 << ": " << A<<" "<<B <<endl;
	}
	return 0;
}
/*

*/
