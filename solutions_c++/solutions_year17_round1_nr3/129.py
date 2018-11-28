#include <iostream>

using namespace std;

typedef long long ll;

ll INF = 0x1fffffffffffffff;
ll Hd,Ad,Hk,Ak,B,D;
ll Dct,Bct;

ll turns() {
	ll Hdc=Hd,Adc=Ad,Hkc=Hk,Akc=Ak;
	ll Tct=0;
	for (int i=0; i<Dct; i++) {
		if (Hdc <= Akc-D) {
			Tct++;
			Hdc = Hd - Akc;
		}

		//If I still can't hit, caught in infinite loop
		if (Hdc <= Akc-D)
			return INF;

		Akc = max(ll(0),Akc-D);
		Hdc -= Akc;
		Tct++;
	}

	for (int i=0; i<Bct; i++) {
		if (Hdc <= Akc) {
			Tct++;
			Hdc = Hd - Akc;
		}

		if (Hdc <= Akc)
			return INF;

		Adc += B;
		Hdc -= Akc;
		Tct++;
	}

	while (Hkc > 0) {
		if (Hdc <= Akc && Hkc > Adc) {
			Tct++;
			Hdc = Hd - Akc;
		}

		if (Hdc <= Akc && Hkc > Adc)
			return INF;
	
		Hkc -= Adc;
		Hdc -= Akc;
		Tct++;
	}

	return Tct;		
}

int main()
{
	int TM;
	cin >> TM;
	for (int T=1; T<=TM; T++) {
		cin >> Hd >> Ad >> Hk >> Ak >> B >> D;

		ll Tct = INF;
		for (int i=0; i<=100; i++) {
			for (int j=0; j<=100; j++) {
				Dct = i;
				Bct = j;
				//if (turns() < Tct)
				//	cout << i << " " << j << " " << turns() << endl;
				Tct = min(Tct,turns());
			}
		}

		if (Tct != INF)
			cout << "Case #" << T << ": " << Tct << "\n"; 
		else
			cout << "Case #" << T << ": IMPOSSIBLE\n";

	}
}
