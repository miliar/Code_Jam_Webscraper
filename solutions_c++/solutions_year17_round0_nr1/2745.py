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

		char s[1005];
		int k;
		cin >> s;
		cin >> k;
		int co = 0;
		int l = strlen(s);
		for(int i=0;i<=l-k;i++) {

			if(s[i] == '-') {

				co++;
				s[i] = '+';

				for(int j = 1; j<k; j++) {

					int p = i+j;
					if(s[p] == '-')
						s[p] = '+';
					else 
						s[p] = '-';
				}
			}
		}

		int fl = 0;
		for(int i=l-k+1;i<l;i++)
			if(s[i] == '-') {
				fl = 1;
				break;
			}


		cout << "Case #" << g << ": ";	
		if(fl == 0) {

			cout << co << endl; 
		}	
		else {

			cout << "IMPOSSIBLE" << endl;
		}
		g++;
	}
	return 0;
}