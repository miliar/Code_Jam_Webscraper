#include<bits/stdc++.h>
using namespace std;

int main() {
	int T; cin >> T;
	for(int C=1; C<=T; C++) {
		
		double d;
		int n;
		cin >> d >> n;
		
		double p[n];
		double s[n];
		
		double maxTime = 0.0000001;
		for(int i=0; i<n; i++) {
			cin >> p[i] >> s[i];
			double t = (d-p[i])/s[i];
			maxTime = max( maxTime, t );
		}
		
		double annie = d / maxTime;
		cout << "Case #" << C << ": ";
		printf("%.6f", annie);
		cout << endl;
	}
}