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

	int t;
	cin >> t;
	int g = 1;
	while(t--) {

		LL n, k;
		cin >> n >> k;

		LL powT = 2;

		while((powT-1) < k) {

			powT *= 2;
		}	

		LL sub = (powT/2)-1;

		n -= sub;

		LL r = n % (sub+1);

		n /= (sub+1);

		k -= sub;

		cout << "Case #" << g << ": ";
		if(k <= r) {
			if(k == 0) {

				cout << "k is zero what to do" << endl;
			}
			else {

				if(n%2 == 0) {

					n /= 2;
					cout << n << " " << n << endl;
				}
				else {

					n /= 2; 
					cout << n+1 << " " << n << endl;	
				}
			}
		}
		else {

			n--;
			
			if(n%2 == 0) {
				n /= 2;
				cout << n << " " << n << endl;
			}
			else {
				n /= 2;
				cout << n+1 << " " << n << endl;	
			}	
		}
		//cout << powT/2-1 << endl;
		g++;
	}

	return 0;
}