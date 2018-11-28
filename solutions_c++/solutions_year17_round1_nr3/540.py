#include <bits/stdc++.h>
using namespace std;

int simulate(int Hd, int Ak, int D, int d, int attacks){
	int a = 0;
	int rounds = 0;
	int ds = 0;
	int h = Hd;
	while(a < attacks){
		if(a == attacks - 1){
			a++;
		}
		else{
			if((h <= Ak - D && ds < d) || (h <= Ak && ds >= d)){
				h = Hd;
			}
			else{
				if(ds < d){
					Ak -= D;
					ds++;
				}
				else{
					a++;
				}
			}
			h -= Ak;
		}
		rounds++;
		if(h <= 0){
			return -1;
		}
		if(rounds > 1000) return -1;
	}
	return rounds;
}

int main()
{
	int T;
	cin >> T;
	for(int testCase = 1; testCase <= T; testCase++){
		cout << "Case #" << testCase << ": ";
		int Hd, Ad, Hk, Ak, B, D;
		cin >> Hd;
		cin >>  Ad;
		cin >>  Hk;
		cin >>  Ak;
		cin >>  B;
		cin >> D;
		double bestX = B > 0 ? (sqrt(double(Hk) * B) - Ad) / B : 0;
		if(bestX < 0) bestX = 0;
		int attacks = 1000000;
		int x = floor(bestX);
		attacks = min(double(attacks), x + ceil(double(Hk) / (B * x + Ad)));
		x = ceil(bestX);
		attacks = min(double(attacks), x + ceil(double(Hk) / (B * x + Ad)));
		int mr = 1000000;
		for(int d = 0; d <= 1000; d++){
			int r = simulate(Hd, Ak, D, d, attacks);
			if(r >= 0) mr = min(mr, r); 
		}
		if(mr == 1000000) cout << "IMPOSSIBLE";
		else cout << mr;

		cout << endl;
	}
  return 0;
}
