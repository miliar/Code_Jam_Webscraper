#include <bits/stdc++.h>

using namespace std;

void doCase(int t) {
	long long Hd, Ad, Hk, Ak, B, D;
	cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
	cout << "Case #" << t << ": ";
	
	if (Hd <= 2*Ak-3*D && Ad < Hk && (Hd <= Ak || (2*Ad < Hk && (Ad+B) < Hk))) {
		cout << "IMPOSSIBLE" << endl;
		return;
	}
	
	long long low = -1;
	long long high;
	long long Nb;
	if (B != 0) {
		high = (Hk-Ad+B-1)/B + 1;
		while (high - low > 2) {
			long long s = (high-low)/3;
			long long m1 = low + s;
			long long m2 = high-s;
		
			long long v1 = m1 + (Hk + Ad + m1*B-1)/(Ad+m1*B);
			long long v2 = m2 + (Hk + Ad + m2*B-1)/(Ad+m2*B);
			if (v1 > v2) {
				low = m1;
			} else {
				high = m2;
			}
		}
		Nb = (high+low)/2;
	} else {
		Nb = 0;
	}
	long long steps_attack = Nb + (Hk + Ad + Nb*B-1)/(Ad+Nb*B);
	
	long long steps_phase1 = 0;
	long long Hrem = Hd;
	long long best = 10000000000LL;
	long long Nd = 0;
	while (true) {
		if (Ak == 0) {
			if (steps_attack + steps_phase1 < best) best = steps_attack + steps_phase1;
			break;
		}
		long long L = (Hrem - 1)/Ak;
		long long S = (Hd - 1)/Ak - 1;
		if (S > 0) {
			long long cur;
			if (L >= steps_attack) {
				cur = steps_attack + steps_phase1;
			} else {
				cur = steps_phase1 + steps_attack + (steps_attack-L + S-2)/S;
			}
			if (cur < best) {
				best = cur;
			}
		}
		if (steps_attack == L+1) {
			if (best > steps_phase1 + steps_attack)
				best = steps_phase1 + steps_attack;
		}
		
		if (D == 0) break;
		
		Ak -= D;
		if (Ak < 0) Ak = 0;
		if (Hrem > Ak) {
			Hrem -= Ak;
			steps_phase1++;
		} else {
			Hrem = Hd - 2*Ak - D;
			steps_phase1+=2;
		}
		Nd ++;
	}
	cout << best << endl;
}

int main() {
	int T;
	cin >> T;
	for (int i=0; i<T; i++)
		doCase(i+1);
	return 0;
}
