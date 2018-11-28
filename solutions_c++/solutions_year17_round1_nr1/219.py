#include <bits/stdc++.h>

#define FI(i,a,b) for(int i=(a);i<=(b);i++)
#define FD(i,a,b) for(int i=(a);i>=(b);i--)

#define LL long long
#define Ldouble long double
#define PI 3.1415926535897932384626

#define PII pair<int,int>
#define PLL pair<LL,LL>
#define mp make_pair
#define fi first
#define se second

using namespace std;

int t, r, c, oo[27];
char s[27][27];

void solve(){
	//fix rows
	FI(i, 1, r){
		int fir = -1;
		FI(j, 1, c) if(s[i][j] != '?'){
			fir = j;
			break;
		}
		if(fir == -1) continue;
		FI(j, 1, fir - 1) s[i][j] = s[i][fir];
		FI(j, fir + 1, c) if(s[i][j] != '?'){
			FI(k, fir + 1, j - 1) s[i][k] = s[i][j];
			fir = j;
		}
		FI(j, fir + 1, c) s[i][j] = s[i][fir];
	}
	//fix columns
	int fir = -1;
	oo[0] = -1;
	FI(i, 1, r){
		if(s[i][1] == '?') oo[i] = oo[i - 1];
		else{
			oo[i] = i;
			if(fir == -1) fir = i;
		}
	}
	FI(i, 1, r) if(oo[i] == -1) oo[i] = fir;
	FI(i, 1, r){
		FI(j, 1, c) printf("%c", s[oo[i]][j]);
		printf("\n");
	}
	return;
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A2.out", "w", stdout);
	scanf("%d", &t);
	FI(i, 1, t){
		printf("Case #%d:\n", i);
		scanf("%d %d", &r, &c);
		FI(j, 1, r) scanf("\n%s", s[j] + 1);
		solve();
	}
	return 0;
}

