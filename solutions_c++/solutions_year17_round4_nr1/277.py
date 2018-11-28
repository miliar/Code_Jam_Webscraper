#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
	int T; cin >> T;
	for(int z = 0; z < T; z++) {
		int count[4]; for(int i = 0; i < 4; i++) count[i] = 0;
		int ans;
		int N, P; cin >> N >> P;
		for(int i = 0; i < N; i++) {int entry; cin >> entry; count[entry%P]++;}
		if(P == 2) {
			ans = count[0] + (count[1]+1)/2;
		} else if (P == 3) {
			int left = max(count[1], count[2]) - min(count[1], count[2]);
			ans = count[0] + min(count[1], count[2]) + (left + 2)/3;
		} else {
			int left = max(count[1], count[3]) - min(count[1], count[3]);
			ans = count[0] + (count[2]+1)/2 + min(count[1], count[3]);
			if(count[2]%2 == 1) {
				left -= 2;
				ans += (left + 3)/4;
			} else {
				ans += (left + 3)/4;
			}
		}
		cout << "Case #" << z+1 << ": " << ans << endl;
	}
}