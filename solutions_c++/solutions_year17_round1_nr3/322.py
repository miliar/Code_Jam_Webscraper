#include<cstdio>
#include<algorithm>
using namespace std;

const int KMAX = 100;
int dp[KMAX + 1][KMAX + 1][KMAX + 1][KMAX + 1]; // myH, knightH, myAtk, knightAtk
int Hd, Ad, Hk, Ak, B, D;

const int IMP = -1;
const int VIS = -2;
const int UND = -3;

void upd(int &x, int y){
	if (x == IMP || x == VIS){
		if (y == IMP) x = y;
		else x = y + 1;
	}
	else{
		if (y == IMP) return;
		else x = min(x, y + 1);
	}
}

int back(int myH, int yourH, int myBuff, int yourDebuff){
	myH = max(0, myH);
	// printf("%d %d %d %d\n", myH, yourH, myBuff, yourDebuff);
	int &ret = dp[myH][yourH][myBuff][yourDebuff];
	if (ret >= IMP) return ret;
	int myAtk = myBuff*B + Ad;
	int yourAtk = max(0, Ak - D*yourDebuff);

	ret = VIS;
	if (myH <= 0)
		return ret = IMP;
	if (myAtk >= yourH)
		return ret = 1;

	// atk
	upd(ret, back(myH - yourAtk, yourH - myAtk, myBuff, yourDebuff));

	// buff
	if (myBuff < KMAX)
		upd(ret, back(myH - yourAtk, yourH, myBuff + 1, yourDebuff));

	// debuff
	if (yourDebuff < KMAX && yourAtk){
		int nextAtk = max(0, yourAtk - D);
		if(myH >= nextAtk)
			upd(ret, back(myH - nextAtk, yourH, myBuff, yourDebuff + 1));
	}

	// heal
	if (Hd >= yourAtk && dp[Hd - yourAtk][yourH][myBuff][yourDebuff] != VIS)
		upd(ret, back(Hd - yourAtk, yourH, myBuff, yourDebuff));

	upd(ret, IMP);
	return ret;
}

int process(){
	for (int i = 0; i <= KMAX; i++)for (int j = 0; j <= KMAX; j++)for (int k = 0; k <= KMAX; k++)for (int l = 0; l <= KMAX; l++)
		dp[i][j][k][l] = UND;

	return back(Hd, Hk, 0, 0);
}

int main(){
	freopen("small.in", "r", stdin);
	freopen("small.out", "w", stdout);

	int T; scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++){
		printf("Case #%d: ", tc);

		scanf("%d%d%d%d%d%d", &Hd, &Ad, &Hk, &Ak, &B, &D);
		int ret = process();
		if (ret == IMP) printf("IMPOSSIBLE\n");
		else printf("%d\n", ret);
		fprintf(stderr, "Case #%d done.\n", tc);
	}
}