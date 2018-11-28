#include <bits/stdc++.h>

using namespace std;

int Test, ans, res;
int Hd, Hk, Ad, Ak, B, D;
int Hdc, Hkc, Adc, Akc, Bc, Dc;

int doneit(int t1, int t2){
	int res = 0;
	bool pre = 0;
	while (t2 > 0){
		if (Hd <= (Ak - D)){
			if (pre) return 2e9;
			Hd = Hdc;
			pre = 1;
		}
		else Ak -= D, t2--, pre = 0;
		Ak = max(Ak, 0);
		Hd -= Ak;
		res++;
		if (Hd <= 0) return 2e9;
	}
	while (t1 > 0){
		if (Hd <= Ak){
			if (pre) return 2e9;
			Hd = Hdc;
			pre = 1;
		}
		else Ad += B, t1--, pre = 0;
		Hd -= Ak;
		res++;
		if (Hd <= 0) return 2e9;
	}
	while (Hk > 0){
		if (Hd <= Ak && Hk > Ad){
			if (pre) return 2e9;
			Hd = Hdc;
			pre = 1;
		}
		else Hk -= Ad, pre = 0;
		if (Hk > 0) Hd -= Ak;
		res++;
		if (Hd <= 0) return 2e9;
		if (Hk <= 0) return res;
	}
	return res;
}

int main(){
//	freopen("C-small-attempt0.in", "r", stdin);
//	freopen("C-small-attempt0.out", "w", stdout);
	scanf("%d", &Test);
	for (int tt = 1; tt <= Test; tt++){
		ans = 2e9;
		scanf("%d%d%d%d%d%d", &Hdc, &Adc, &Hkc, &Akc, &Bc, &Dc);
		for (int t1 = 0; t1 <= 100; t1++)
			for (int t2 = 0; t2 <= 100; t2++){
				Hd = Hdc;
				Ad = Adc;
				Hk = Hkc;
				Ak = Akc;
				B = Bc;
				D = Dc;
				res = doneit(t1, t2);
				ans = min(ans, res);
			}
		printf("Case #%d: ", tt);
		if (ans < 2e9) printf("%d\n", ans);
		else printf("IMPOSSIBLE\n");
	}
}