#include <iostream>
#include <iomanip>
using namespace std;
int main() {
    int T;
    cin >> T;
	for(int t = 1; t <= T; t++) {
	    int D, N;
	    cin >> D >> N;
	    double k, s, m = 0;
	    for(int i = 0; i < N; i++) {
	        cin >> k >> s;
	        m = max(m, ((double)D - k) / s);
	    }
	 cout <<fixed<<setprecision(6);
	 cout << "Case #" <<t << ": " << (double)D / m << endl;
	    
	}
	return 0;
}
