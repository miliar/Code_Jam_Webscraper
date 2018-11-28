#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include <string>
#include <cstdio>
#include <set>
#include <deque>
#include <vector>
using namespace std;



int main()
{

	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	double d, n, k,s;

	double  minTime, time;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		cin >> d >> n;
		minTime = 0;
		for (int j = 0; j < n; j++) {

			cin >> k >> s;
			time = (d - k) / s;
			if (time > minTime)
				minTime = time;
		}

			
			cout<<fixed<< d / minTime<<endl;


	}

	return 0;
}

