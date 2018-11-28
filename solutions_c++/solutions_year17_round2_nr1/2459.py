#include<iostream>
#include<cstring>
#include<fstream>
#include<algorithm>
#include<cstdio>
#include<ctime>
#include<climits>
#include<bits/stdc++.h>
#include<string.h>
#include<stdlib.h>

using namespace std;

#define MAX 9999999
#define INF 99999999999
#define MOD 1000000007



typedef long L;
typedef long long LL;

//global program variables


//functions


int main() {

	L t;
	cin >> t;
	int g = 1;
	cout << setprecision(11);
	while(t--) {

		LL d; 
		LL n;
		cin >> d >> n;

		double mxt = 0;
		for(LL i=0;i<n;i++) {

			LL k,s;
			cin >> k >> s;
			double tmp= (double)(d-k)/s;
			if(tmp > mxt)
				mxt = tmp;

		}




		cout << setprecision(8) << "Case #" << g++ << ": " << (double)(d/mxt) << endl;
	}

	return 0;
}