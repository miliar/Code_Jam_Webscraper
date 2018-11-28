#include<iostream>
#include<cstdlib>

using namespace std;

int main() {
	int test;
	cin >> test;
	for(int i=1; i<=test; ++i) {
		string pancake;
		int k;
		cin >> pancake >> k;
		int ans = 0;
		for(int j=0; j<=pancake.length()-k; ++j) {
			if(pancake[j] == '+') 
				continue;
			ans += 1;
			for(int m=0; m<k; ++m) {
				if(pancake[j+m] == '-')
					pancake[j+m] = '+';
				else
					pancake[j+m] = '-';
			}	
		}
		bool flag = true;
		for(int j=pancake.length()-k+1; j<pancake.length(); ++j) {
			if(pancake[j] == '-') {
				flag = false;
				break;
			}
		}
		if(flag) 
			cout << "Case #" << i << ": " << ans << endl;
		else
			cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
	}

	return 0;
}
