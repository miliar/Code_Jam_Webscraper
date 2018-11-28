#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <iomanip>

using namespace std;

int main(){
	int T;
	cin >> T;
	for (int K = 1; K <= T; K++){
		int n, p;
		cin >> n >> p;
		int q[105], ans = 0;
		for (int i = 0; i < n; i++) cin >> q[i];
		if (p == 2){
			int a1 = 0, a2 = 0;
			for (int i = 0; i < n; i++){
				if (q[i] % 2) a1++;
				else a2++;
			}
			ans = a2 + (a1 + 1) / 2;
		} else if (p == 3){
			int a1, a2, a3;
			a1 = a2 = a3 = 0;
			for (int i = 0; i < n; i++){
				if (q[i] % 3 == 1) a1++;
				else if (q[i] % 3 == 2) a2++;
				else a3++;
			}
			if (a1 < a2) swap(a1, a2);
			ans = a3 + a2 + (a1 - a2 + 2) / 3;
		} else {
			
		}
		cout << "Case #" << K << ": ";
		cout << ans << endl;
	}
	
	return 0;
}
