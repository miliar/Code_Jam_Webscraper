#include<bits/stdc++.h>

using namespace std;

const int MAXN = 100 + 2;

int hd, ad, hk, ak, B, D;

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	int te;	cin >> te;
	for (int w = 1; w <= te; w++){
		cin >> hd >> ad >> hk >> ak >> B >> D;
		int ans = 1e9;

		for (int a = 0; a <= ak; a++)
			for (int b = 0; b <= hk; b++)
				for (int c = 1; c <= hk; c++){
					int h1 = hd, a1 = ad, h2 = hk, a2 = ak;
					bool fail = 0;
					int cnt = 0, cur = 0;


					for (int i = 0; !fail && i < a; i++, cur++){
						if (a2 - D >= h1){
							cnt++;
							h1 = hd;
							i--;
						}
						else{
							cnt = 0;
							a2 -= D;
						}

						h1 -= a2;

						if (cnt == 2) fail = 1;
						if (h1 <= 0) fail = 1;
					}
					if (fail) break;

					for (int i = 0; !fail && i < b; i++, cur++){
						if (a2 >= h1){
							cnt++;
							h1 = hd;
							i--;
						}
						else{
							cnt = 0;
							a1 += B;
						}

						h1 -= a2;
						if (cnt == 2 || h1 <= 0) fail = 1;
					}
					if (fail) continue;

					for (int i = 0; !fail && i < c; i++){
						cur++;
						if (h2 - a1 > 0 && a2 >= h1){
							cnt++;
							h1 = hd;
							i--;
						}
						else{
							cnt = 0;
							h2 -= a1;
						}

						if (h2 > 0)
							h1 -= a2;
						if (cnt == 2 || h1 <= 0) fail = 1;
						if (h2 <= 0) break;
					}

					if (fail) continue;

					if (h2 <= 0)
						ans = min(ans, cur);
				}

		if (ans > 1e8)
			cout << "Case #" << w << ": " << "IMPOSSIBLE" << "\n";
		else
			cout << "Case #" << w << ": " << ans << "\n";
	}
	return 0;
}
