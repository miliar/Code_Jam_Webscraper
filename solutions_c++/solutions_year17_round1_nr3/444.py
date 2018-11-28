#include <cstdio>
bool cure;
int T, Hd, Ad, Hk, Ak, B, D, ans, turn, DEC, INC;
int HD, AD, HK, AK;
int main (){
	freopen ("C-small-attempt1.in", "r", stdin);
	freopen ("C-small-attempt1.out", "w", stdout);
	scanf("%d", &T);
	for (int i = 1; i <= T; i++){
		scanf("%d %d %d %d %d %d", &Hd, &Ad, &Hk, &Ak, &B, &D);
		HD = Hd;
		AD = Ad;
		HK = Hk;
		AK = Ak;
		ans = -1;
		for (int dec = 0; dec <= 100; dec++){
			for (int inc = 0; inc <= 100; inc++){
				DEC = dec;
				INC = inc;
				if (D == 0)
					DEC = 0;
				if (B == 0)
					INC = 0;
				
				turn = 0;
				cure = false;
				while (Hk > 0){
					turn++;
					if (Hk <= Ad){
						Hk -= Ad;
						cure = false;
					} else if (DEC > 0 && Hd > Ak - D){
						Ak -= D;
						if (Ak < 0)
							Ak = 0;
						DEC--;
						cure = false;
					} else if (Hd <= Ak){
						if (cure){
							turn = -1;
							Hk = 0;
						} else {
							Hd = HD;
							cure = true;
						}
					} else if (DEC){
						Ak -= D;
						if (Ak < 0)
							Ak = 0;
						DEC--;
						cure = false;
					} else if (INC){
						Ad += B;
						INC--;
						cure = false;
					} else {
						Hk -= Ad;
						cure = false;
					}
					
					if (Hk > 0){
						Hd -= Ak;
						if (Hd <= 0){
							turn = -1;
							Hk = 0;
						}
					}
				}
				
				if (turn != -1){
					if (ans == -1)
						ans = turn;
					else if (ans > turn)
						ans = turn;
				}
				
				Hd = HD;
				Ad = AD;
				Hk = HK;
				Ak = AK;
			}
		}
		if (ans == -1)
			printf("Case #%d: IMPOSSIBLE\n", i);
		else 
			printf("Case #%d: %d\n", i, ans);
	}
	fclose (stdin);
	fclose (stdout);
	return 0;
}
