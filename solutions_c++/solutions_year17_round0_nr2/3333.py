#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

typedef long long ll;

int main() {
	int T;
	cin >> T;
	for (int t=1;t<=T;t++) {
		ll N;
		cin >> N;
		int ndigit = 0;
		for (ll i=N;i>0;i/=10) ndigit++;
		ll thresh = 0;
		for (int i=0;i<ndigit;i++) thresh = thresh * 10 + 1;
		if (N < thresh) {
			printf ("Case #%d: ",t);
			for (int i=0;i<ndigit-1;i++) printf("9");
			printf("\n");
		}
		else {
			vector<int> v;
			for (ll k=N;k>0;k/=10) v.push_back(k%10);

			while (1) {
				bool done = true;
				for (int i=1;i<ndigit;i++) if (v[i] > v[i-1]) done = false;
				if (done) break;
				bool changed = false;
				for (int i=ndigit-2;i>=0;i--) {
					if (changed) v[i] = 9;
					else {
						if(v[i] < v[i+1]) {
							v[i+1] --;
							v[i] = 9;
							changed = true;
						}
					}
				}
			}
			printf ("Case #%d: ",t);
			for (int i=ndigit-1;i>=0;i--) printf("%d", v[i]);
			printf("\n");
		}
	}
}