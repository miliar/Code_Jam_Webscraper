#include <iostream>
#include <cstring>
#include <fstream>
#define pos [Hd][Ad][Hk][Ak]
#define mn(a, b) ((a)<(b)?(a):(b))
#define mn4(a, b, c, d) mn(mn(a, b), mn(c, d))
#define inf (0x3f3f3f3f)
using namespace std;
int T, B, D, Ho;
int dp[105][105][105][105];
//int pp[105][105][105][105];
int recur(int Hd, int Ad, int Hk, int Ak) {
	if (Ak<=0) Ak=0;
	Hd-=Ak;
	//printf("%d %d %d %d\n", Hd, Ad, Hk, Ak);
	if (Hk<=0) {
		//printf("gottem\n");
		return 0;
	}
	if (Hd<=0) return inf;
	if (dp pos==-2) return inf;
	if (dp pos!=-1) return dp pos;
	dp pos=-2;
	// attack
	int a=recur(Hd, Ad, Hk-Ad, Ak);
	// buff
	int b;
	if (Ad<Hk&&B>0) {
		b=recur(Hd, Ad+B, Hk, Ak);
	} else b=inf;
	// cure
	int c=recur(Ho, Ad, Hk, Ak);
	// debuff
	int d;
	if (Ak>0&&D>0) {
		d=recur(Hd, Ad, Hk, Ak-D);
	} else d=inf;
	//printf("****%d %d %d %d %d\n", Hd, Ad, Hk, Ak, (mn4(a, b, c, d)+1));
	//if (a==mn4(a, b, c, d)) pp[Hd][Ad][Hk][Ak]=1;
	//if (b==mn4(a, b, c, d)) pp[Hd][Ad][Hk][Ak]=2;
	//if (c==mn4(a, b, c, d)) pp[Hd][Ad][Hk][Ak]=3;
	//if (d==mn4(a, b, c, d)) pp[Hd][Ad][Hk][Ak]=4;
	return dp[Hd][Ad][Hk][Ak]=(mn4(a, b, c, d)+1)>inf?inf:(mn4(a, b, c, d)+1);
}
int main() {
    ifstream cin("s3in.txt");
    ofstream cout("s3out.txt");
	cin>>T;
	for (int t=1; t<=T; t++) {
		int Hd, Ad, Hk, Ak;
		cin>>Hd>>Ad>>Hk>>Ak>>B>>D;
		for (int i=0; i<105; i++) {
			for (int j=0; j<105; j++) {
				for (int k=0; k<105; k++) {
					for (int l=0; l<105; l++) {
						dp[i][j][k][l]=-1;
					}
				}
			}
		}
		Ho=Hd;
		int ans=recur(Hd+Ak, Ad, Hk, Ak);
		if (ans<inf) cout<<"Case #"<<t<<": "<<ans<<"\n";
		else cout<<"Case #"<<t<<": IMPOSSIBLE\n";
		Hd+=Ak;
		/*int tt=0;
		while (Hk>0) {
			if (Ak<=0) Ak=0;
			Hd-=Ak;
			printf("%d", pp[Hd][Ad][Hk][Ak]);
			if (pp[Hd][Ad][Hk][Ak]==1) Hk-=Ad;
			else if (pp[Hd][Ad][Hk][Ak]==2) Ad+=B;
			else if (pp[Hd][Ad][Hk][Ak]==3) Hd=Ho;
			else if (pp[Hd][Ad][Hk][Ak]==4) Ak-=D;
			tt++;
		}
		printf("\n%d", tt);*/
		printf("Case #%d: %d\n", t, ans);
	}
}
