#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define For(i, a, b) for(int i=a; i<b; i++)
#define ffi For(i, 0, N)
#define ffj For(j, 0, K)
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
ll T, N, K;
string in;

bool works(ll num) {
	int prev = 9;
	//w<< "testing" s num<<e;
	while (num != 0) {
		if (num%10 > prev) return false;
		prev = num%10;
		num /= 10;
		//w<< num<<e;
	}
	return true;
}

int main() {
	//ifstream cin ("test.in");
	ifstream cin ("Bsmallattempt0.in");
	ofstream cout ("Bsmallattempt0.out");
	cin >> T;
	For (t, 0, T) {
		cin >> N;
		//w<< N<<e;
		ll out;
		for (ll i=N; i>=0; i--) {
			if (works(i)) {
				out = i;
				break;
			}
		}
		
		w<< "Case #" << t+1<< ": ";
		w<< out<<e;
	}
	
	
	return 0;
}

