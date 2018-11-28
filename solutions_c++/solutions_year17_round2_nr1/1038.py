#include <iostream>
#include <string>
#include <iomanip>
#include <algorithm>

using namespace std;

int main(){
	int T;
	cin >> T;
	for (int K = 1; K <= T; K++){
		double d, t, k, s;
		int n;
		cin >> d >> n;
		cin >> k >> s;
		t = (d - k) / s;
		while (--n){
			cin >> k >> s;
			t = max(t, (d - k) / s);
		}
		double ans = d / t;
		cout << "Case #" << K << ": " << fixed << setprecision(6) << ans << endl;
	}
	
	return 0;
}
