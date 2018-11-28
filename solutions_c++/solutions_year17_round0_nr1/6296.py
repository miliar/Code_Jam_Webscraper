#include<iostream>
#include<string>
#include<cstring>
#include<cmath>
#include<cstdlib>
using namespace std;
typedef long long ll;

int main() {
	freopen("/Users/viverma/Downloads/inp.txt", "r", stdin);
	freopen("/Users/viverma/Downloads/out.txt", "w", stdout);
	ll T, k, test, siz, i, j, flips, blank;
	string pancakes;
	cin >> T;
	for (test = 1; test <= T; test++) {
		cout << "Case #" << test << ": ";
		cin>>pancakes;
		cin>>k;
		siz = pancakes.size();
		flips = 0;
		for (i = siz - 1; i >= 0; i--) {
			if (pancakes[i] == '-') {
				if ( i - k + 1 < 0 ) {
					break;
				}
				flips++;
				for (j = i; j >= i - k + 1; j--) {
					if (pancakes[j] == '+')
						pancakes[j] = '-';
					else
						pancakes[j] = '+';
				}
			}
		}
		if (i != -1 ){
			cout << "IMPOSSIBLE" <<endl;
		} else {
			blank = 0;
			for (i = 0; i < siz; i++) {
				if (pancakes[i] == '-')
					blank++;
			}
			if (blank == 0)
				cout << flips <<endl;
			else
				cout << "IMPOSSIBLE" <<endl;
		}
	}
	
	return 0;
}
