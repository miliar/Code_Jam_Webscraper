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

		int r, c;
		cin >> r >> c;

		char in[26][26];

		for(int i=0;i<r;i++) {

			for(int j=0;j<c;j++) {

				cin >> in[i][j];
			}
		}

		for(int i=0;i<r;i++) {

			for(int j=0;j<c;j++) {

				if(in[i][j] != '?') {

					int x = j+1;	
					while(x < c && in[i][x] == '?') {

						in[i][x] = in[i][j];
						x++;
					}

					
					x = j-1;	
					while(x >= 0 && in[i][x] == '?') {

						in[i][x] = in[i][j];
						x--;
					}

				}
			}
		}



		for(int i=0;i<r;i++) {

			for(int j=0;j<c;j++) {

				if(in[i][j] != '?') {

					int x = i+1;	
					while(x < r && in[x][j] == '?') {

						in[x][j] = in[i][j];
						x++;
					}

					
					x = i-1;	
					while(x >= 0 && in[x][j] == '?') {

						in[x][j] = in[i][j];
						x--;
					}

				}
			}
		}	

		cout << "Case #" << g++ << ": " << endl;
		for(int i=0;i<r;i++) {

			for(int j=0;j<c;j++) {

				cout << in[i][j];
			}
			cout << endl;
		}	
		//break;

	}	


	return 0;
}