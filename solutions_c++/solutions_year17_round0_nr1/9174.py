#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define For(i, a, b) for(int i=a; i<b; i++)
#define ffi For(i, 0, N-K+1)
#define ffj For(j, i, i+K)
#define ffa ffi ffj
#define s <<" "<<
#define w cout
#define e endl
#define pb push_back
#define mp make_pair
#define a first
#define b second
//500,000,000 operations
//Global Variables
int T, N, K;
string in;

int main() {
	//ifstream cin ("test.in");
	ifstream cin ("A-large.in");
	ofstream cout ("A-large.out");
	cin >> T;
	For (t, 0, T) {
		cin >> in >> K; N = in.length();
		
		int out = 0;
		ffi {
			if (in[i] == '-') {
				out++;
				ffj {
					if (in[j] == '-') in[j] = '+';
					else in[j] = '-';
				}
			}
		}
		bool good = true;
		For (i, 0, N) {
			if (in[i] == '-') good = false;
		}
		w<< "Case #" << t+1<< ": ";
		if (good) w<< out<<e;
		else w<< "IMPOSSIBLE"<<e;
	}
	
	
	return 0;
}

