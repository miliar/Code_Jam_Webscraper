#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
	long t;
	cin >> t;
	int x = t;
	long n, k;
	int i;
	long div[10000], mmax, pos;
	while(t--) {
		cin >> n;
		cin >> k;
		mmax = 0;
		pos = 0;
		div[0] = n;
		for(i = 1; i <= k; i++) {
			mmax = 0; pos = 0;
			for(int j = 0; j < i; j++) {
				 if(div[j] > mmax) { mmax = div[j]; pos = j;}
			}
			div[pos] = (mmax-1)/2;
			div[i] = (mmax-1) - div[pos];
			if(i == k) break;
		}
		cout << "Case #" << x-t << ": " << max(div[pos], div[i]) << " " << min(div[pos], div[i]) << endl;
	}
	
  return 0;
}
