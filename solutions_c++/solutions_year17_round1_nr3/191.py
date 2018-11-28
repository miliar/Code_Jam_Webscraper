#include <bits/stdc++.h>

using namespace std;

int main(){
	freopen("test.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin.sync_with_stdio(0); cin.tie(0);
	int T; cin >> T;

	for (int pp=1; pp<=T; ++pp){
		int oHd, oAd, oHk, oAk, oB, oD;
		int Hd, Ad, Hk, Ak, B, D;
		cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
		oHd = Hd; oAd = Ad; oHk = Hk; oAk = Ak;

		int minattackturns = 1e9, nbuffs = 0;
		for (int t=0;t<=100; ++t){
			int xturns = (int)ceil(double(Hk)/(Ad + B*t)) + t;
			if (xturns < minattackturns){
				minattackturns = xturns;
				nbuffs = t;
			}
		}
		int ans = 1e9;
		for (int nd=0; nd<=100; ++nd){
			Hd = oHd, Ad = oAd, Hk = oHk, Ak = oAk;
			int turns = 0;
			int curd = 0, curbuffs = 0;
			int fk = 0;
			bool fail = false;
			while (curd < nd){
				if (Hd - (Ak - D) <= 0){
					Hd = oHd;
				}
				else{
					curd++;
					Ak -= D;
				}
				Hd -= Ak;
				turns++;
				fk++;
				if (fk > 200){
					fail = true;
					break;
				}
			}
			fk = 0;
			if (fail) continue;
			while (curbuffs < nbuffs){
				if (Hd - Ak <= 0){
					Hd = oHd;
				}
				else{
					curbuffs++;
					Ad += B;
				}
				Hd -= Ak;
				turns++;
				fk++;
				if (fk > 200){
					fail = true;
					break;
				}
			}
			if(fail) continue;
			fk = 0;
			while (true){
				turns++;
				if (Hk - Ad <= 0){
					break;
				}
				else if (Hd - Ak <= 0){
					Hd = oHd;
				}
				else{
					Hk -= Ad;
				}
				Hd -= Ak;
				fk++;
				if (fk > 200){
					fail = true;
					break;
				}
			}
			if(fail) continue;
			ans = min(ans, turns);

		}

		if (ans == 1e9)
			printf("Case #%d: IMPOSSIBLE\n", pp);
		else
			printf("Case #%d: %d\n", pp, ans);
	}
	return 0;
}