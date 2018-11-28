#include <iostream>
#include <string>
#include <vector>
#include <utility>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> pii; 
#define sz(a) int((a).size()) 
#define pb push_back 
#define mp make_pair 

int main() {
	int tests, t;
	cin >> tests;
	for(t = 1; t <= tests; t++) {
		int c, r;
		string l;
		cin >> r >> c;
		vector<string> cake(r);
		for(int i = 0; i < r; i++) {
			//for(int j = 0; j < c; j++) {
				cin >> l;
				cake[i] = l;
			//}
		}
		char ch = '?';
		int i, j, k;
		bool b = false;
		bool b2 = false;
		int m;
		for(i = 0; i < r; i++) {
			for(j = 0; j < c; j++) {
				if(cake[i][j] == '?') {
					b2 = true;
				}
			}
			if(b2) {
				for(j = 0; j < c; j++) {
					if(cake[i][j] != '?') {
						ch = cake[i][j];
						break;
					}
				}
				if (j < c) {
					for(k = 0; k < j; k++)
						cake[i][k] = ch;
				}
				for(j = j+1; j < c; j++) {
					if(cake[i][j] == '?')
						cake[i][j] = ch;
					else {
						ch = cake[i][j];
					}
				}
				b2 = false;
			}

		}
		for(i = 0; i < r-1; i++) {
			if(cake[i][0] == '?') {
				for(k = i+1; k < r; k++) {
					if (cake[k][0] != '?')
						break;
				}
				if(k >= r) {
					k = i-1;
				}
				for(j = 0; j < c; j++) {
					cake[i][j] = cake[k][j];
				}
			}
		}
		if(cake[r-1][0] == '?') {
			for(j = 0; j < c; j++) {
				cake[r-1][j] = cake[r-2][j];
			}
		}
		cout << "Case #" << t << ":" << endl;
		for(i = 0; i < r; i++) {
			for(j = 0; j < c; j++) {
				cout << cake[i][j];
			}
			cout << endl;
		}
	}
	return 0;
}