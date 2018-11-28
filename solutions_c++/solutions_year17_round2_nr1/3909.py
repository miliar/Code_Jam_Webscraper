#include <bits/stdc++.h>

using namespace std;

int main() {
	
	int T, N;
	long long D;
	vector<long long> K;
	vector<int> S;
	long long Ktmp, Stmp;
	long double vMax, deltaPerV;
	long double timeNeeded1, timeNeeded2;
	
	cin >> T;
	
	for (int i = 0; i < T; i++) {
		
		cin >> D;
		cin >> N;
		
		K.clear();
		S.clear();
		
		for (int j = 0; j < N; j++) {
			cin >> Ktmp;
			cin >> Stmp;
			K.push_back(Ktmp);
			S.push_back(Stmp);
			
			
		}
		
		if (N == 1) {
			deltaPerV = (long double) (D - K[0]) / S[0];
			vMax = (long double) D / deltaPerV;
			
			//cout << "dpv: " << deltaPerV << endl;
			//cout << "vmax: " << vMax << endl;
			
		} else if (N == 2) {
			//deltaLinearEq = (float) (0-K[0] - (0-K[1])) / (S[0] - S[1]);
			timeNeeded1 = (long double) (D - K[0]) / S[0];
			timeNeeded2 = (long double) (D - K[1]) / S[1];
			
			//cout << "tn1 - tn2: " << timeNeeded1 << " " << timeNeeded2 << endl;
			
			if (timeNeeded1 < timeNeeded2) {
				vMax = (long double) D / timeNeeded2;
			} else {
				vMax = (long double) D / timeNeeded1;
			}
			
			//cout << "vmax: " << vMax << endl;
			
		} else {
			
			vector<long double> v2;
			
			for (int k = 0; k < N; k++) {
				timeNeeded1 = (long double) (D - K[k]) / S[k];
				v2.push_back(timeNeeded1);
			}
			
			long double MAXV2 = v2[0];
			for (int k = 0; k < N; k++) {
				if (MAXV2 >= v2[k]) {
					MAXV2 = MAXV2;
				} else {
					MAXV2 = v2[k];
				}
			}
			
			vMax = (long double) D / MAXV2;
			
		}
		
		// Save flags/precision.
		ios_base::fmtflags oldflags = cout.flags();
		streamsize oldprecision = cout.precision();
		cout << "Case #" << i + 1 << ": ";
		cout << fixed << setprecision(6) << vMax << endl;
		//cout << "Case #" << i + 1 << ": " << vMax << endl;
		
	}
	
	return 0;
	
}