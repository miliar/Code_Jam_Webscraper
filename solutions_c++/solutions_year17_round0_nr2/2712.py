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

		char s[20];
		cin >> s;

		int l = strlen(s);
		while(1) {
			
			for(int i=1;i<l;i++) {
				if(i >= 1) {

					if(s[i] < s[i-1]) {

						s[i-1] -= 1;

						for(int j=i;j<l;j++) {

							s[j] = '9';
						}
						i -= 2;
					}
				}
			}
			break;
		}



		LL ans = atoll(s);
		cout << "Case #" << g << ": " << ans << endl;	
		
		g++;
	}


	return 0;
}