#include <bits/stdc++.h>
#define ll long long
#define int ll
#define mod 1000000007
using namespace std;

main(){
  ios::sync_with_stdio(0);
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  
	int cases, k;
	string pancakes;
	int states[1010];
	
	cin >> cases;
	for(int t = 1; t <= cases; t++) {
		cin >> pancakes >> k;		
		cout << "Case #" << t << ": ";
		
		int pancakeCount = pancakes.length();
		
		for(int i = 0; i < pancakeCount; i++) {
			states[i] = (pancakes[i] == '-') ? 0 : 1;
		}
		
		int flips = 0;
		for(int i = 0; i <= pancakeCount - k; i++) {
			if(states[i] == 0) {
				for(int j = 0; j < k; j++) {
					states[i+j] ^= 1;
				}
				flips++;
			}
		}
		
		bool impossible = false;
		for(int i = 1; i <= k; i++) {
			if(states[pancakeCount - i] == 0) {
				impossible = true;
				break;
			}
		}
		
		if(impossible) {
			cout << "IMPOSSIBLE" << endl;
		} else {
			cout << flips << endl;
		}
	}
}

